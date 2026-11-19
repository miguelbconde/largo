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
    # Estudo E: meio-termo. Cabeçalho em faixa azul com marca em areia e ponto laranja; página em areia como no C.
    "e": {
        "nome": "Estudo E",
        "tema": ("#17437d", "#123a6e"),
        "css": """
:root{ --sol:#d96c14; --faixa:#17437d; --faixa-texto:#fbf7ee; --faixa-texto2:#cbd8ec; --faixa-linha:#3d68a6; --faixa-sol:#ffb469; }
@media (prefers-color-scheme: dark){ :root{ --sol:#f29a45; --faixa:#123a6e; } }
header.topo{background:var(--faixa);color:var(--faixa-texto);border-bottom:none;padding:28px 0 16px;margin-bottom:16px;
  box-shadow:0 0 0 100vmax var(--faixa);clip-path:inset(-100vmax -100vmax 0 -100vmax)}
.marca h1 span{color:var(--faixa-sol)}
header.topo .sub,header.topo .edicao{color:var(--faixa-texto2)}
header.topo .edicao{margin-bottom:0}
.idiomas button{border-color:var(--faixa-linha);color:var(--faixa-texto2)}
.idiomas button[aria-pressed=true]{background:var(--faixa-texto);border-color:var(--faixa-texto);color:#0f2a50}
#destaques .ev{border-left:4px solid var(--sol)}
.qb::before{content:"";display:inline-block;width:.42em;height:.42em;border-radius:50%;background:var(--sol);margin-right:.32em;vertical-align:.12em}
""",
    },
    # Estudo F: dois modos com botão. Claro = areia + sol, com azul no que está selecionado. Escuro = mar no fundo.
    "f": {
        "nome": "Estudo F",
        "tema": ("#f8f4ec", "#143b70"),
        "botao": True,
        "css": """
:root,:root[data-tema=claro]{ %(claro)s }
@media (prefers-color-scheme: dark){ :root{ %(escuro)s } }
:root[data-tema=claro]{ %(claro)s }
:root[data-tema=escuro]{ %(escuro)s }
.dia[aria-pressed=true],.idiomas button[aria-pressed=true],.btn.cheio{background:var(--sel);border-color:var(--sel);color:var(--sel-texto)}
.dia[aria-pressed=true] small{color:var(--sel-texto)}
.dia.passado[aria-pressed=true]{opacity:1}
.tag.popular{border:1px solid var(--pop-borda)}
.aviso{border:1px solid var(--pop-borda)}
#destaques .ev{border-left:4px solid var(--sol)}
.qb::before{content:"";display:inline-block;width:.42em;height:.42em;border-radius:50%%;background:var(--sol);margin-right:.32em;vertical-align:.12em}
.controles{display:flex;gap:8px;align-items:center;flex-wrap:wrap;justify-content:flex-end}
#tema{font:600 12px var(--sans);border:1px solid var(--tinta2);background:transparent;color:var(--tinta);padding:4px 10px;border-radius:999px;cursor:pointer;min-height:26px}
""" % {
            "claro": "--papel:#f8f4ec; --papel2:#eee7d9; --tinta:#2a2623; --tinta2:#5f574e; --linha:#dbd2c1;"
                     " --acento:#1b4e8f; --acento-suave:#dfe7f2; --gratis:#1d5a3c; --gratis-suave:#1d5a3c;"
                     " --popular:#75461f; --popular-suave:#eddcc0; --alerta:#8a4b12; --sobre-cor:#f8f4ec;"
                     " --sol:#d96c14; --sel:#1b4e8f; --sel-texto:#f8f4ec; --pop-borda:transparent;",
            "escuro": "--papel:#143b70; --papel2:#0f2e59; --tinta:#fbf7ee; --tinta2:#c9d6ea; --linha:#3a629e;"
                      " --acento:#ffb469; --acento-suave:#0f2e59; --gratis:#86cfa3; --gratis-suave:#86cfa3;"
                      " --popular:#fbf7ee; --popular-suave:transparent; --alerta:#ffcf9e; --sobre-cor:#0d2748;"
                      " --sol:#ffb469; --sel:#ffb469; --sel-texto:#0d2748; --pop-borda:#fbf7ee;",
        },
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

# A escolha de modo fica guardada só no aparelho da pessoa. Sem escolha, vale a configuração do aparelho.
TEMA_CEDO = """(function(){try{var m=localStorage.getItem('largo:tema');if(m==='claro'||m==='escuro')document.documentElement.dataset.tema=m}catch(e){}})();"""
TEMA_BOTAO = """(function(){
var R=document.documentElement, COR={claro:'%s',escuro:'%s'};
var N={pt:{claro:'Claro',escuro:'Escuro',r:'Mudar para modo '},en:{claro:'Light',escuro:'Dark',r:'Switch to mode: '},es:{claro:'Claro',escuro:'Oscuro',r:'Cambiar a modo '}};
function atual(){return R.dataset.tema||(matchMedia('(prefers-color-scheme: dark)').matches?'escuro':'claro')}
var id=document.querySelector('.idiomas'), c=document.createElement('div'), b=document.createElement('button');
c.className='controles'; b.id='tema'; b.type='button'; id.replaceWith(c); c.append(b,id);
function pinta(){var a=atual(), o=a==='claro'?'escuro':'claro', l=(R.lang||'pt').slice(0,2), n=N[l]||N.pt;
  b.textContent=n[o]; b.setAttribute('aria-label',n.r+n[o].toLowerCase());
  document.querySelectorAll('meta[name=theme-color]').forEach(function(m){m.content=COR[a]})}
b.onclick=function(){var o=atual()==='claro'?'escuro':'claro'; R.dataset.tema=o; try{localStorage.setItem('largo:tema',o)}catch(e){} pinta()};
new MutationObserver(pinta).observe(R,{attributes:true,attributeFilter:['lang']});
matchMedia('(prefers-color-scheme: dark)').addEventListener('change',pinta); pinta();
})();"""

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
        if e.get("botao"):
            html = html.replace("<head>", "<head>\n<script>" + TEMA_CEDO + "</script>", 1)
            html = html.replace("</body>", "<script>" + (TEMA_BOTAO % (claro, escuro)) + "</script>\n</body>", 1)
        pasta = os.path.join(RAIZ, "docs", "estudo-" + letra)
        os.makedirs(pasta, exist_ok=True)
        open(os.path.join(pasta, "index.html"), "w", encoding="utf-8").write(html)
        print("ok", pasta)

if __name__ == "__main__":
    main()
