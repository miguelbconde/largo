#!/usr/bin/env python3
"""Fichas de cinema montadas sem IA, a partir da extração da Ingresso.com.

Lê o plataformas.json da ronda (ramo coleta-bruta) e grava dados/edicoes/<edição>/cinema.json:
uma ficha por filme e por cinema, com as sessões que caem dentro da edição. A ficha só traz fatos
(título, direção, país, ano, duração, classificação, datas, horários, sala, preço) e uma linha
descritiva montada desses fatos; nenhum texto da plataforma é copiado. O gerador do site junta
estas fichas às da redação.
Uso: python3 cinema.py <edição AAAA-MM-DD> <caminho do plataformas.json>
"""
import json, os, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def reais(v):
    return ("R$ %.2f" % v).replace(".", ",").replace(",00", "")


def descricao(f):
    partes = []
    if f.get("direcao"):
        partes.append(f"Direção de {f['direcao']}.")
    dados = [x for x in (f.get("pais"), str(f["ano"]) if f.get("ano") else "",
                         f"{f['duracao_min']} min" if f.get("duracao_min") else "") if x]
    if dados:
        partes.append(", ".join(dados) + ".")
    if f.get("titulo_original") and f["titulo_original"].lower() != f["titulo"].lower():
        partes.insert(0, f"Título original: {f['titulo_original']}.")
    return " ".join(partes) or "Sessões de cinema."


def main(edicao, caminho):
    pasta = os.path.join(RAIZ, "dados", "edicoes", edicao)
    ed = json.load(open(os.path.join(pasta, "eventos.json"), encoding="utf-8"))["edicao"]
    p = json.load(open(caminho, encoding="utf-8"))
    ing = p["ingresso"]
    grupos = {}
    for s in ing["sessoes"]:
        if not (ed["inicio"] <= s["data"] <= ed["fim"]) or not s["hora"]:
            continue
        grupos.setdefault((s["cinema_id"], s["filme_id"]), []).append(s)
    fichas = []
    for (cid, fid), ss in sorted(grupos.items(), key=lambda x: (ing["cinemas"][x[0][0]]["nome"], ing["filmes"][x[0][1]]["titulo"])):
        c, f = ing["cinemas"][cid], ing["filmes"][fid]
        ss = sorted(ss, key=lambda s: (s["data"], s["hora"]))
        sess, vistos = [], set()
        for s in ss:
            if (s["data"], s["hora"]) not in vistos:
                vistos.add((s["data"], s["hora"])); sess.append({"data": s["data"], "hora": s["hora"]})
        precos = sorted({s["preco"] for s in ss if isinstance(s.get("preco"), (int, float)) and s["preco"] > 0})
        if precos:
            texto = reais(precos[0]) if len(precos) == 1 else f"{reais(precos[0])} a {reais(precos[-1])}"
            pmin, pmax = precos[0], precos[-1]
        else:
            texto, pmin, pmax = "", None, None
        trecho = f"Ingresso.com · {c['nome']} · {f['titulo']} · " + "; ".join(
            f"{s['data']} {s['hora']} {s.get('sala','')} {reais(s['preco']) if s.get('preco') else ''}".strip() for s in ss)
        fichas.append(dict(
            titulo=f["titulo"], areas=["Cinema"], tipo="evento", local=c["nome"], endereco=c["endereco"],
            bairro=c["bairro"], regiao=c["regiao"], sessoes=sess, cartaz=None,
            preco_texto=(texto + " (preço da plataforma)") if texto else "", preco_min=pmin, preco_max=pmax,
            gratis=False, classificacao=f.get("classificacao", ""), acessibilidade="", na_rua=False,
            sinopse=descricao(f), fonte="Ingresso.com (extração do Largo)",
            link=f.get("link") or c.get("site") or "", link_espaco=c.get("site", ""),
            trecho_fonte=trecho[:1500],
            nota_redacao="Ficha montada automaticamente a partir dos dados da Ingresso.com, sem redação de IA.",
            automatica=True, id=f"{edicao}-cine-{cid}-{fid}"))
    json.dump({"feito_em": p.get("feito_em"), "fichas": fichas},
              open(os.path.join(pasta, "cinema.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(fichas), "fichas de cinema,", sum(len(x["sessoes"]) for x in fichas), "sessões")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
