#!/usr/bin/env python3
"""Traduções das sinopses para inglês e espanhol (os títulos nunca são traduzidos).

As traduções ficam em dados/traducoes.json, presas ao texto em português por um código (hash):
se a sinopse mudar, a tradução antiga deixa de valer e a ficha volta a aparecer como pendente.
Uso:
  python3 traduzir.py pendentes <edição> [saída.json]   lista as sinopses e os "por que ir" dos destaques sem tradução (id, pt)
  python3 traduzir.py gravar <arquivo.json>             grava traduções: [{"pt": ..., "en": ..., "es": ...}, ...]
As fichas automáticas de cinema se traduzem sozinhas (ferramentas/redacao/cinema.py).
"""
import hashlib, json, os, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARQ = os.path.join(RAIZ, "dados", "traducoes.json")


def chave(pt):
    return hashlib.sha1(" ".join(pt.split()).encode("utf-8")).hexdigest()[:16]


def carregar():
    return json.load(open(ARQ, encoding="utf-8")) if os.path.exists(ARQ) else {}


def gravar(novas):
    base = carregar()
    for t in novas:
        if t.get("pt") and t.get("en") and t.get("es"):
            base[chave(t["pt"])] = {"pt": t["pt"], "en": t["en"], "es": t["es"]}
    json.dump(dict(sorted(base.items())), open(ARQ, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return len(base)


if __name__ == "__main__":
    if sys.argv[1] == "pendentes":
        base = carregar()
        ev = json.load(open(os.path.join(RAIZ, "dados", "edicoes", sys.argv[2], "eventos.json"), encoding="utf-8"))["eventos"]
        p = [{"id": e["id"], "pt": e["sinopse"]} for e in ev if e.get("sinopse") and chave(e["sinopse"]) not in base]
        dest = os.path.join(RAIZ, "dados", "edicoes", sys.argv[2], "destaques.json")
        if os.path.exists(dest):
            for l in json.load(open(dest, encoding="utf-8"))["dias"].values():
                p += [{"id": d["id"], "pt": d["porque"]} for d in l if d.get("porque") and chave(d["porque"]) not in base]
        if len(sys.argv) > 3:
            json.dump(p, open(sys.argv[3], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(len(p), "sinopses sem tradução")
    elif sys.argv[1] == "gravar":
        print(gravar(json.load(open(sys.argv[2], encoding="utf-8"))), "traduções no arquivo")
