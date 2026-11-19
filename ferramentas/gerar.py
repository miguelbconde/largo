#!/usr/bin/env python3
"""Gerador do Largo — Agenda cultural do Rio de Janeiro.

Lê a base de uma edição (dados/edicoes/<id>/eventos.json) e, se existir, o relatório
do conferente (conferencia.json). Aplica as conferências mecânicas e gera:
  docs/index.html            site (um único arquivo, sem rastreadores)
  docs/calendarios/*.ics     calendários assináveis (geral, por área, por região, grátis)
  docs/dados/eventos.json    dados abertos (ODbL)
  docs/dados/eventos.csv
  dados/edicoes/<id>/relatorio.md  relatório de exceções da edição
Uso: python3 ferramentas/gerar.py 2026-11-15
"""
import csv, json, os, re, sys, unicodedata, datetime as dt
from collections import Counter

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AREAS = ["Música", "Teatro", "Artes Visuais", "Cinema", "Livros & Debates", "Festas & Feiras", "Infantil"]
REGIOES = ["Centro", "Zona Sul", "Zona Sudoeste", "Zona Norte", "Zona Oeste"]
POPULAR = 40  # teto do preço popular (inteira), decisão editorial de 15/11/2026


def slug(s):
    s = unicodedata.normalize("NFD", s.lower()).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def faixa(e):
    if e["gratis"]:
        return "gratis"
    if e["preco_max"] is None:
        return "nao_informado"
    inteira = e["preco_max"]
    if inteira <= POPULAR:
        return "popular"
    return "ate80" if inteira <= 80 else "acima80"


def conferencia_mecanica(ed, eventos):
    """Regras sem IA. Devolve lista de (id, problema, gravidade)."""
    ini, fim = ed["inicio"], ed["fim"]
    probs, vistos = [], {}
    for e in eventos:
        i = e["id"]
        if not e["endereco"] or not e["bairro"]:
            probs.append((i, "Endereço ou bairro ausente", "alta"))
        if e["regiao"] not in REGIOES:
            probs.append((i, "Região inválida ou ausente", "alta"))
        if not set(e["areas"]) <= set(AREAS):
            probs.append((i, f"Área fora do padrão: {e['areas']}", "alta"))
        if e["tipo"] == "evento":
            if not e["sessoes"]:
                probs.append((i, "Evento sem sessões", "alta"))
            for s in e["sessoes"]:
                if not (ini <= s["data"] <= fim):
                    probs.append((i, f"Sessão fora da edição: {s['data']}", "alta"))
                if not re.fullmatch(r"([01]\d|2[0-3]):[0-5]\d", s["hora"] or ""):
                    probs.append((i, f"Horário inválido: {s['hora']}", "alta"))
                elif not ("08:00" <= s["hora"] <= "23:59"):
                    probs.append((i, f"Horário incomum: {s['hora']}", "media"))
        if e["gratis"] and (e["preco_max"] or 0) > 0:
            probs.append((i, "Marcado como grátis, mas tem preço", "alta"))
        if not e["gratis"] and e["preco_max"] is None:
            probs.append((i, "Preço não informado na fonte", "baixa"))
        if e["preco_min"] is not None and e["preco_max"] is not None and e["preco_min"] > e["preco_max"]:
            probs.append((i, "Preço mínimo maior que o máximo", "alta"))
        if not e["link"].startswith("http"):
            probs.append((i, "Link oficial ausente", "media"))
        chave = (slug(e["titulo"]), slug(e["local"]))
        if chave in vistos:
            probs.append((i, f"Possível duplicata de {vistos[chave]}", "alta"))
        vistos[chave] = i
    return probs


PUBLICOS = ("municipal", "Municipal", "Arena", "Areninha", "Biblioteca", "Muhcab", "Museu", "Memorial",
            "Centro Cultural", "Centro Municipal", "Centro da Música", "Centro Coreográfico", "Cidade das Artes",
            "Teatro de", "Sesc", "CCBB", "Espaço Cultural")


def validar_destaques(eventos, destaques):
    """Regras públicas de curadoria. Uma regra só é cobrada se o dia oferece opções para cumpri-la."""
    por_id = {e["id"]: e for e in eventos}
    alertas = []
    for dia, lista in destaques["dias"].items():
        pool = [e for e in eventos if e["tipo"] == "evento" and e["status"] == "conferido"
                and any(x["data"] == dia for x in e["sessoes"])]
        esc = []
        for d in lista:
            e = por_id.get(d["id"])
            if not e:
                alertas.append((dia, f"ID inexistente: {d['id']}")); continue
            if e["status"] != "conferido":
                alertas.append((dia, f"“{e['titulo']}” não está conferido e não pode ser destaque"))
            if not any(x["data"] == dia for x in e["sessoes"]):
                alertas.append((dia, f"“{e['titulo']}” não tem sessão neste dia"))
            esc.append(e)
        def possivel(n):  # o dia permite atingir n?
            return min(n, len(lista))
        regs = {e["regiao"] for e in esc}; regs_pool = {e["regiao"] for e in pool}
        if len(regs) < possivel(min(3, len(regs_pool))):
            alertas.append((dia, f"Só {len(regs)} região(ões); o dia oferecia {len(regs_pool)}"))
        areas = {a for e in esc for a in e["areas"]}; areas_pool = {a for e in pool for a in e["areas"]}
        if len(areas) < possivel(min(3, len(areas_pool))):
            alertas.append((dia, f"Só {len(areas)} área(s); o dia oferecia {len(areas_pool)}"))
        baratos = sum(e["faixa"] in ("gratis", "popular") for e in esc)
        if esc and baratos * 2 < len(esc) and sum(e["faixa"] in ("gratis", "popular") for e in pool) >= len(esc) / 2:
            alertas.append((dia, f"Só {baratos} de {len(esc)} destaques grátis ou a preço popular"))
        locais = [e["local"] for e in esc]
        if len(set(locais)) < len(locais):
            alertas.append((dia, "Mais de um destaque no mesmo espaço"))
        if esc and not any(any(k in e["local"] for k in PUBLICOS) for e in esc):
            alertas.append((dia, "Nenhum espaço público, comunitário ou sem fins lucrativos"))
    return alertas


# ---------------------------------------------------------------- calendários
def ics_escape(s):
    return s.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")


def ics_fold(linha):
    b = linha.encode("utf-8")
    if len(b) <= 74:
        return linha
    partes, atual = [], ""
    for ch in linha:
        if len((atual + ch).encode("utf-8")) > 73:
            partes.append(atual)
            atual = " " + ch
        else:
            atual += ch
    partes.append(atual)
    return "\r\n".join(partes)


def utc(data, hora):  # Rio: UTC−3, sem horário de verão
    t = dt.datetime.strptime(f"{data} {hora}", "%Y-%m-%d %H:%M") + dt.timedelta(hours=3)
    return t.strftime("%Y%m%dT%H%M%SZ")


def preco_legivel(e):
    if e["gratis"]:
        return e["preco_texto"] or "Grátis"
    return e["preco_texto"] or "Preço não informado"


def ics(nome, eventos, carimbo, so_sessoes=None):
    L = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Largo//Agenda cultural do Rio de Janeiro//PT-BR",
         "CALSCALE:GREGORIAN", "METHOD:PUBLISH", f"X-WR-CALNAME:{ics_escape(nome)}",
         "X-WR-TIMEZONE:America/Sao_Paulo", "REFRESH-INTERVAL;VALUE=DURATION:PT12H",
         "X-PUBLISHED-TTL:PT12H"]
    for e in eventos:
        if e["tipo"] != "evento":
            continue
        for k, s in enumerate(e["sessoes"]):
            if so_sessoes is not None and (e["id"], s["data"]) not in so_sessoes:
                continue
            ini = utc(s["data"], s["hora"])
            fim = (dt.datetime.strptime(ini, "%Y%m%dT%H%M%SZ") + dt.timedelta(hours=2)).strftime("%Y%m%dT%H%M%SZ")
            desc = f"{e['sinopse']}\n\n{preco_legivel(e)}"
            if e["classificacao"]:
                desc += f" · {e['classificacao']}"
            if e.get("status") == "a_confirmar":
                desc += "\n\nATENÇÃO: informação a confirmar na fonte."
            desc += f"\n\nFonte: {e['link']}\nLargo — agenda cultural aberta do Rio"
            L += ["BEGIN:VEVENT", f"UID:{e['id']}-{k}@largo.rio.br", f"DTSTAMP:{carimbo}",
                  f"DTSTART:{ini}", f"DTEND:{fim}", f"SUMMARY:{ics_escape(e['titulo'])}",
                  f"LOCATION:{ics_escape(e['local'] + ', ' + e['endereco'] + ' – ' + e['bairro'])}",
                  f"DESCRIPTION:{ics_escape(desc)}", f"URL:{e['link']}",
                  f"CATEGORIES:{ics_escape(','.join(e['areas']))}", "END:VEVENT"]
    L.append("END:VCALENDAR")
    return "\r\n".join(ics_fold(x) for x in L) + "\r\n"


# ---------------------------------------------------------------- principal
def main(edicao_id):
    pasta = os.path.join(RAIZ, "dados", "edicoes", edicao_id)
    base = json.load(open(os.path.join(pasta, "eventos.json"), encoding="utf-8"))
    ed, eventos = base["edicao"], base["eventos"]

    conf_path = os.path.join(pasta, "conferencia.json")
    conf = json.load(open(conf_path, encoding="utf-8")) if os.path.exists(conf_path) else {"resultado": []}
    mec = conferencia_mecanica(ed, eventos)

    problemas_ia = {}
    for r in conf.get("resultado", []):
        problemas_ia.setdefault(r["id"], []).append(r)
    graves = {i for i, _, g in mec if g == "alta"}
    for e in eventos:
        e["faixa"] = faixa(e)
        ia = [r for r in problemas_ia.get(e["id"], []) if not r.get("resolucao")]
        e["status"] = "a_confirmar" if (ia or e["id"] in graves) else "conferido"

    dest_path = os.path.join(pasta, "destaques.json")
    destaques = json.load(open(dest_path, encoding="utf-8")) if os.path.exists(dest_path) else {"dias": {}}
    alertas_dest = validar_destaques(eventos, destaques)
    sess_dest = {(d["id"], dia) for dia, l in destaques["dias"].items() for d in l}

    out = os.path.join(RAIZ, "docs")
    os.makedirs(os.path.join(out, "calendarios"), exist_ok=True)
    os.makedirs(os.path.join(out, "dados"), exist_ok=True)
    carimbo = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    # calendários: geral, grátis, por área, por região
    feeds = {"largo-geral.ics": ("Largo · Agenda cultural do Rio", eventos),
             "largo-gratis.ics": ("Largo · Grátis", [e for e in eventos if e["gratis"]])}
    feeds["largo-na-rua.ics"] = ("Largo · Na rua", [e for e in eventos if e.get("na_rua")])
    for a in AREAS:
        if not any(a in e["areas"] for e in eventos):
            continue
        feeds[f"largo-{slug(a)}.ics"] = (f"Largo · {a}", [e for e in eventos if a in e["areas"]])
    for r in REGIOES:
        feeds[f"largo-{slug(r)}.ics"] = (f"Largo · {r}", [e for e in eventos if e["regiao"] == r])
    for nome, (titulo, lista) in feeds.items():
        open(os.path.join(out, "calendarios", nome), "w", encoding="utf-8", newline="").write(ics(titulo, lista, carimbo))
    feeds = {"largo-destaques.ics": ("Largo · A boa (destaques)", []), **feeds}
    open(os.path.join(out, "calendarios", "largo-destaques.ics"), "w", encoding="utf-8", newline="").write(
        ics("Largo · A boa (destaques)", eventos, carimbo, so_sessoes=sess_dest))

    # dados abertos
    publicos = [{k: v for k, v in e.items() if k != "nota_redacao"} for e in eventos]
    json.dump({"edicao": ed, "licenca": "ODbL 1.0 (dados) · CC BY-SA 4.0 (textos)", "eventos": publicos},
              open(os.path.join(out, "dados", "eventos.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    with open(os.path.join(out, "dados", "eventos.csv"), "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["id", "titulo", "areas", "tipo", "datas_horarios", "local", "endereco", "bairro", "regiao",
                    "preco", "faixa", "classificacao", "acessibilidade", "na_rua", "sinopse", "link", "fonte", "status"])
        for e in eventos:
            dh = " | ".join(f"{s['data']} {s['hora']}" for s in e["sessoes"]) if e["tipo"] == "evento" else \
                f"em cartaz até {e['cartaz']['fim'] or '—'} · {e['cartaz']['horario']}"
            w.writerow([e["id"], e["titulo"], " / ".join(e["areas"]), e["tipo"], dh, e["local"], e["endereco"],
                        e["bairro"], e["regiao"], preco_legivel(e), e["faixa"], e["classificacao"],
                        e["acessibilidade"], "sim" if e.get("na_rua") else "", e["sinopse"], e["link"], e["fonte"], e["status"]])

    # site
    modelo = open(os.path.join(RAIZ, "ferramentas", "modelo.html"), encoding="utf-8").read()
    dados_site = json.dumps({"edicao": ed, "eventos": publicos, "destaques": destaques["dias"],
                             "feeds": {k: v[0] for k, v in feeds.items()}}, ensure_ascii=False)
    dados_site = dados_site.replace("</", "<\\/")
    html = modelo.replace("/*__DADOS__*/null", dados_site)
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(html)

    # relatório de exceções
    n_sess = sum(len(e["sessoes"]) for e in eventos)
    reg = Counter(e["regiao"] or "(sem região)" for e in eventos)
    linhas = [f"# Relatório da edição — {ed['titulo']}", "",
              f"- Eventos e exposições: **{len(eventos)}** ({sum(e['tipo']=='evento' for e in eventos)} eventos com "
              f"{n_sess} sessões; {sum(e['tipo']=='cartaz' for e in eventos)} em cartaz)",
              f"- Grátis: **{sum(e['gratis'] for e in eventos)}** · preço popular (até R$ {POPULAR}): "
              f"**{sum(e['faixa']=='popular' for e in eventos)}**",
              f"- Conferidos sem ressalva: **{sum(e['status']=='conferido' for e in eventos)}** · "
              f"a confirmar: **{sum(e['status']=='a_confirmar' for e in eventos)}**", "",
              "## Distribuição por região", ""]
    linhas += [f"- {r}: {reg.get(r, 0)}" for r in REGIOES + ["(sem região)"] if reg.get(r, 0)]
    linhas += ["", "## Conferente independente (IA)", ""]
    if conf.get("resultado"):
        for r in conf["resultado"]:
            res = f" → **{r['resolucao']}**" if r.get("resolucao") else " → **pendente (sai como “a confirmar”)**"
            linhas.append(f"- **{r['titulo']}** ({r['id']}) · {r['campo']} · *{r['veredito']}* — {r['detalhe']}{res}")
    else:
        linhas.append("- Nenhuma divergência registrada." if os.path.exists(conf_path) else "- Conferência ainda não executada.")
    linhas += ["", "## Conferência mecânica (regras)", ""]
    nomes = {e["id"]: e["titulo"] for e in eventos}
    linhas += [f"- [{g}] **{nomes[i]}** ({i}) — {p}" for i, p, g in mec] or ["- Nenhum problema."]
    linhas += ["", "## Destaques (A boa)", ""]
    for dia, l in destaques["dias"].items():
        linhas.append(f"- **{dia[8:10]}/{dia[5:7]}**: " + "; ".join(nomes.get(d["id"], d["id"]) for d in l))
    linhas += ["", "Regras de curadoria:"] + ([f"- ⚠️ {d[8:10]}/{d[5:7]} — {a}" for d, a in alertas_dest] or ["- Todas as regras cumpridas."])
    linhas += ["", "## Notas de redação", ""]
    linhas += [f"- **{e['titulo']}** — {e['nota_redacao']}" for e in eventos if e.get("nota_redacao")]
    open(os.path.join(pasta, "relatorio.md"), "w", encoding="utf-8").write("\n".join(linhas) + "\n")
    print(f"{len(eventos)} eventos · {len(feeds)} calendários · {len(mec)} alertas mecânicos · "
          f"{len(conf.get('resultado', []))} apontamentos do conferente · {len(sess_dest)} destaques · {len(alertas_dest)} alertas de curadoria")
    for a in alertas_dest:
        print("  curadoria:", *a)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "2026-11-19")
