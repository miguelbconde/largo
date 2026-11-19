#!/usr/bin/env python3
"""Extração das plataformas de ingresso — Ingresso.com (cinema) e Sympla (eventos).

Faz parte da ronda diária. Segue o protocolo do Todos os Rios para plataformas (plano diretor, seção 5):
só fatos sobre eventos (título, datas, horários, local, preço, classificação, link), nunca dados de
pessoas (o e-mail do organizador que a Sympla expõe é descartado), sem login, sem romper barreiras
técnicas, com pausa entre visitas, identificado como TodosOsRiosBot. Nas plataformas não seguimos as regras
para robôs que elas publicam (decisão editorial de 19/11/2026).

Saídas (na pasta de texto bruto da ronda, fora da linha principal):
  plataformas.json        dados estruturados das duas plataformas
  (a lista da Sympla para a redação é feita depois, por triagem_sympla.py)
E na linha principal, só números: dados/coleta/plataformas.md
Uso: python3 plataformas.py <pasta de saída>
"""
import datetime as dt, json, os, re, ssl, sys, time, urllib.request, urllib.error

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
AGENTE = "Mozilla/5.0 (compatible; TodosOsRiosBot/0.1; agenda cultural aberta do Rio; +https://github.com/miguelbconde/largo)"
PAUSA = 2

# Todos os cinemas da cidade na Ingresso.com entram (decisão editorial de 19/11/2026: cinema de shopping
# também é cinema). A região sai do bairro; bairro desconhecido fica sem região e aparece no relatório.
REGIAO_BAIRRO = {
    "Centro": "Centro", "Santa Teresa": "Centro", "Lapa": "Centro",
    "Botafogo": "Zona Sul", "Gávea": "Zona Sul", "Laranjeiras": "Zona Sul", "Leblon": "Zona Sul",
    "São Conrado": "Zona Sul", "Catete": "Zona Sul", "Flamengo": "Zona Sul", "Copacabana": "Zona Sul",
    "Ipanema": "Zona Sul", "Humaitá": "Zona Sul", "Urca": "Zona Sul", "Glória": "Zona Sul",
    "Barra da Tijuca": "Zona Sudoeste", "Recreio": "Zona Sudoeste", "Recreio dos Bandeirantes": "Zona Sudoeste",
    "Jacarepaguá": "Zona Sudoeste", "Taquara": "Zona Sudoeste", "Tanque": "Zona Sudoeste", "Freguesia": "Zona Sudoeste",
    "Guadalupe": "Zona Norte", "Méier": "Zona Norte", "Vila Kosmos": "Zona Norte", "Ilha do Governador": "Zona Norte",
    "Irajá": "Zona Norte", "Madureira": "Zona Norte", "Del Castilho": "Zona Norte", "Vila Isabel": "Zona Norte",
    "Tijuca": "Zona Norte", "Cachambi": "Zona Norte", "Penha": "Zona Norte", "Maracanã": "Zona Norte",
    "Bangu": "Zona Oeste", "Campo Grande": "Zona Oeste", "Campo Dos Afonsos": "Zona Oeste",
    "Campo dos Afonsos": "Zona Oeste", "Realengo": "Zona Oeste", "Santa Cruz": "Zona Oeste",
}
FORA = ("MEG - MULTIPLATFORM",)  # não é cinema
SITES = {"34": "https://www.grupoestacao.com.br/", "506": "https://www.grupoestacao.com.br/",
         "33": "https://www.grupoestacao.com.br/", "1463": "https://www.cinesantateresa.com.br/"}
CIDADE_INGRESSO = "2"  # Rio de Janeiro
SYMPLA_PAGINAS = 100


def baixar(url, limite=5_000_000):
    req = urllib.request.Request(url, headers={"User-Agent": AGENTE, "Accept-Language": "pt-BR,pt;q=0.9",
                                               "Accept": "text/html,application/json;q=0.9,*/*;q=0.8"})
    try:
        with urllib.request.urlopen(req, timeout=60, context=ssl.create_default_context()) as r:
            return r.status, r.read(limite).decode(r.headers.get_content_charset() or "utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:
        return 0, type(e).__name__


def jbaixar(url):
    st, t = baixar(url)
    time.sleep(PAUSA)
    try:
        return st, json.loads(t) if st == 200 else None
    except ValueError:
        return st, None


# ------------------------------------------------------------------ Ingresso.com
def ingresso():
    base = "https://api-content.ingresso.com/v0"
    st, cartaz = jbaixar(f"{base}/events/city/{CIDADE_INGRESSO}?partnership=home")
    fichas_filme = {str(f["id"]): f for f in (cartaz or [])}
    filmes, sessoes, falhas = {}, [], []
    st, lista = jbaixar(f"{base}/theaters/city/{CIDADE_INGRESSO}?partnership=home")
    CINEMAS = {}
    for t in lista or []:
        if not t.get("enabled", True) or any(t.get("name", "").startswith(x) for x in FORA):
            continue
        bairro = (t.get("neighborhood") or "").strip()
        end = " ".join(x for x in [(t.get("address") or "").strip().title() if (t.get("address") or "").isupper() else (t.get("address") or "").strip(),
                                    str(t.get("number") or "").strip()] if x)
        CINEMAS[str(t["id"])] = (t["name"].strip(), end, bairro, REGIAO_BAIRRO.get(bairro, ""), SITES.get(str(t["id"]), ""))
    if not CINEMAS:
        falhas.append(f"lista de cinemas (código {st})")
    for cid, (nome, end, bairro, reg, site) in CINEMAS.items():
        st, dias = jbaixar(f"{base}/sessions/city/{CIDADE_INGRESSO}/theater/{cid}?partnership=home")
        if st != 200 or not isinstance(dias, list):
            falhas.append(f"{nome} (código {st})")
            continue
        for dia in dias:
            for m in dia.get("movies", []):
                fid = str(m.get("id"))
                if fid not in filmes:
                    extra = fichas_filme.get(fid, {})
                    filmes[fid] = {
                        "id": fid, "titulo": (m.get("title") or "").strip(),
                        "titulo_original": (m.get("originalTitle") or "").strip(),
                        "direcao": (extra.get("directors") or extra.get("director") or "").strip(),
                        "pais": (extra.get("countryOrigin") or "").strip(),
                        "ano": m.get("releaseYear") or extra.get("releaseYear"),
                        "duracao_min": m.get("duration"), "classificacao": m.get("contentRating") or "",
                        "generos": m.get("genres") or [],
                        "link": f"https://www.ingresso.com/filme/{m.get('urlKey')}?city=rio-de-janeiro" if m.get("urlKey") else "",
                    }
                for sala in m.get("rooms", []):
                    for s in sala.get("sessions", []):
                        data = (s.get("date") or {}).get("localDate", "")[:10]
                        sessoes.append({
                            "cinema_id": cid, "filme_id": fid, "data": data, "hora": s.get("time", ""),
                            "sala": s.get("room") or sala.get("name", ""), "preco": s.get("price"),
                            "tipos": [t for t in s.get("type", []) if t],
                        })
    # direção e país dos filmes fora da lista "em cartaz" (repertório): uma consulta por filme
    for fid, f in filmes.items():
        if f["direcao"] or fid in fichas_filme:
            continue
        st, d = jbaixar(f"{base}/events/{fid}?partnership=home")
        if isinstance(d, dict):
            f["direcao"] = (d.get("directors") or d.get("director") or "").strip()
            f["pais"] = (d.get("countryOrigin") or "").strip()
            f["ano"] = f["ano"] or d.get("releaseYear")
    cinemas = {cid: dict(zip(("nome", "endereco", "bairro", "regiao", "site"), v)) for cid, v in CINEMAS.items()}
    falhas += [f"bairro sem região: {v[0]} ({v[2]})" for v in CINEMAS.values() if not v[3]]
    return {"cinemas": cinemas, "filmes": filmes, "sessoes": sessoes, "falhas": falhas}


# ------------------------------------------------------------------ Sympla
def decodificar_next(html):
    partes = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)</script>', html, re.S)
    out = []
    for p in partes:
        try:
            out.append(json.loads('"' + p + '"'))
        except ValueError:
            pass
    return "".join(out)


def eventos_sympla(texto):
    dec = json.JSONDecoder()
    for m in re.finditer(r'\{"end_date"', texto):
        try:
            obj, _ = dec.raw_decode(texto, m.start())
        except ValueError:
            continue
        if isinstance(obj, dict) and "id" in obj and "name" in obj:
            yield obj


def sympla():
    eventos, falhas, sem_novos = {}, [], 0
    for pagina in range(1, SYMPLA_PAGINAS + 1):
        url = "https://www.sympla.com.br/eventos/rio-de-janeiro-rj" + (f"?page={pagina}" if pagina > 1 else "")
        st, html = baixar(url)
        time.sleep(PAUSA)
        if st != 200:
            falhas.append(f"página {pagina} (código {st})"); break
        antes = len(eventos)
        for o in eventos_sympla(decodificar_next(html)):
            loc = o.get("location") or {}
            if (loc.get("city") or "").strip().lower() != "rio de janeiro" or o.get("event_type") not in ("NORMAL", None):
                continue
            org = o.get("organizer") or {}
            eventos[str(o["id"])] = {   # só fatos; e-mail e imagem do organizador descartados
                "id": str(o["id"]), "titulo": (o.get("name") or "").strip(),
                "inicio": o.get("start_date", ""), "fim": o.get("end_date", ""),
                "local": (loc.get("name") or "").strip(), "endereco": (loc.get("address") or "").strip(),
                "bairro": (loc.get("neighborhood") or "").strip(),
                "lat": loc.get("lat"), "lon": loc.get("lon"),
                "organizador": (org.get("name") or "").strip(), "link": o.get("url", ""),
                "duracao": o.get("duration_type", ""),
            }
        sem_novos = sem_novos + 1 if len(eventos) == antes else 0
        if sem_novos >= 3:
            break
    return {"eventos": list(eventos.values()), "paginas_lidas": pagina, "falhas": falhas}


def hora_rio(iso):
    """'2026-11-19T22:00:00+00:00' -> ('2026-11-19', '19:00') no horário do Rio (UTC−3)."""
    try:
        t = dt.datetime.fromisoformat(iso.replace("Z", "+00:00")).astimezone(dt.timezone(dt.timedelta(hours=-3)))
        return t.strftime("%Y-%m-%d"), t.strftime("%H:%M")
    except ValueError:
        return iso[:10], ""


def main(saida):
    os.makedirs(saida, exist_ok=True)
    feito = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    ing = ingresso()
    sym = sympla()
    json.dump({"feito_em": feito, "ingresso": ing, "sympla": sym},
              open(os.path.join(saida, "plataformas.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    por_cinema = {}
    for s in ing["sessoes"]:
        por_cinema[s["cinema_id"]] = por_cinema.get(s["cinema_id"], 0) + 1
    linhas = [f"# Extração das plataformas — {feito[:10]}", "",
              "Números da última ronda. Os dados brutos ficam no ramo `coleta-bruta` (`plataformas.json`).", "",
              f"## Ingresso.com (cinema): {len(ing['sessoes'])} sessões, {len(ing['filmes'])} filmes", ""]
    linhas += [f"- {v['nome']}: {por_cinema.get(c, 0)} sessões" for c, v in ing["cinemas"].items()]
    linhas += [f"- Falhou: {x}" for x in ing["falhas"]]
    linhas += ["", f"## Sympla: {len(sym['eventos'])} eventos no Rio ({sym['paginas_lidas']} páginas lidas)", ""]
    linhas += [f"- Falhou: {x}" for x in sym["falhas"]] or ["- Sem falhas."]
    os.makedirs(os.path.join(RAIZ, "dados", "coleta"), exist_ok=True)
    open(os.path.join(RAIZ, "dados", "coleta", "plataformas.md"), "w", encoding="utf-8").write("\n".join(linhas) + "\n")
    print(f"Ingresso.com: {len(ing['sessoes'])} sessões · Sympla: {len(sym['eventos'])} eventos")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "coleta-bruta")
