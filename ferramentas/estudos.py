#!/usr/bin/env python3
"""Gera estudos de paleta a partir do site já publicado (docs/index.html).

Cada estudo é o mesmo site com outra paleta, publicado como prévia separada
em docs/estudo-<letra>/index.html. Não altera o site principal.

Uso: python3 ferramentas/estudos.py
"""
import os, re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ESTUDOS = {
    # Estudo C: paleta da paisagem + sol. Laranja só em "A boa", sempre como forma, nunca como letra.
    "c": {
        "nome": "Estudo C",
        "tema": ("#f8f4ec", "#1a1918"),
        "css": """
:root{ --sol:#d96c14; }
@media (prefers-color-scheme: dark){ :root{ --sol:#f29a45; } }
#destaques .ev{border-left:4px solid var(--sol)}
.qb::before{content:"";display:inline-block;width:.42em;height:.42em;border-radius:50%;background:var(--sol);margin-right:.32em;vertical-align:.12em}
""",
    },
    # Estudo D: mar como fundo, texto claro, laranja como cor que organiza.
    "d": {
        "nome": "Estudo D",
        "tema": ("#17437d", "#0f2444"),
        "css": """
:root{
  --papel:#17437d; --papel2:#113564; --tinta:#fbf7ee; --tinta2:#cbd8ec; --linha:#3d68a6;
  --acento:#ffb469; --acento-suave:#113564; --gratis:#fbf7ee; --gratis-suave:#fbf7ee;
  --popular:#fbf7ee; --popular-suave:transparent; --alerta:#ffcf9e; --sobre-cor:#0f2a50;
}
@media (prefers-color-scheme: dark){
  :root{ --papel:#0f2444; --papel2:#0a1a33; --tinta:#f3eee3; --tinta2:#b9c7de; --linha:#2c4a7a;
    --acento:#ffb469; --acento-suave:#0a1a33; --gratis:#f3eee3; --gratis-suave:#f3eee3;
    --popular:#f3eee3; --popular-suave:transparent; --alerta:#ffcf9e; --sobre-cor:#0a1a33; }
}
.tag.popular{border:1px solid var(--tinta)}
.aviso{border:1px solid var(--linha)}
.dia[aria-pressed=true]{background:var(--acento);border-color:var(--acento);color:var(--sobre-cor)}
.dia[aria-pressed=true] small{color:var(--sobre-cor)}
.idiomas button[aria-pressed=true]{background:var(--acento);border-color:var(--acento);color:var(--sobre-cor)}
#destaques .ev{border-left:4px solid var(--acento)}
""",
    },
}

def main():
    base = open(os.path.join(RAIZ, "docs", "index.html"), encoding="utf-8").read()
    for letra, e in ESTUDOS.items():
        html = base
        html = re.sub(r"<title>(Estudo \w+ · )?", "<title>%s · " % e["nome"], html, count=1)
        claro, escuro = e["tema"]
        html = re.sub(r'(<meta name="theme-color" content=")[^"]+(" media="\(prefers-color-scheme: light\)">)', r"\g<1>%s\g<2>" % claro, html)
        html = re.sub(r'(<meta name="theme-color" content=")[^"]+(" media="\(prefers-color-scheme: dark\)">)', r"\g<1>%s\g<2>" % escuro, html)
        html = html.replace("</head>", '<meta name="robots" content="noindex">\n<style>%s</style>\n</head>' % e["css"], 1)
        # os links de dados e calendários apontam para a pasta do site principal
        html = html.replace('href="dados/', 'href="../dados/').replace('calendarios/${', '../calendarios/${')
        pasta = os.path.join(RAIZ, "docs", "estudo-" + letra)
        os.makedirs(pasta, exist_ok=True)
        open(os.path.join(pasta, "index.html"), "w", encoding="utf-8").write(html)
        print("ok", pasta)

if __name__ == "__main__":
    main()
