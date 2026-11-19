# Peneira da ronda: separa, do texto bruto de cada fonte, só os trechos que falam de datas
# da semana da edição (com algumas linhas de contexto), para a redação das fichas.
# Uso: python3 peneirar.py <pasta com os F*.txt> <início AAAA-MM-DD> <fim AAAA-MM-DD> <arquivo de saída> [vistos.json]
# Com o quinto argumento, a peneira vira "só o que mudou": mostra apenas os trechos com alguma linha que
# não estava nas rondas anteriores (a linha nova vem marcada com ★) e grava, ao lado da saída, um arquivo
# <saída>.vistos com a lista atualizada. Esse arquivo guarda só códigos das linhas (não o texto dos sites);
# depois de redigir as fichas, copie-o por cima de dados/coleta/vistos.json.
import re, sys, os, glob, datetime, json, hashlib

MESES = "janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro".split()
ABR = [m[:3] for m in MESES]

def padroes(inicio, fim):
    dias = []
    d = inicio
    while d <= fim:
        dias.append(d); d += datetime.timedelta(days=1)
    ps = []
    for d in dias:
        dd, m = d.day, d.month
        ps += [r"\b0?%d\s*[/.]\s*0?%d\b" % (dd, m),
               r"\b0?%d(º)?\s*(de\s+)?(%s|%s)\b" % (dd, MESES[m-1], ABR[m-1]),
               r"\b(%s|%s)[a-z]*\.?\s+0?%d\b" % (ABR[m-1], ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"][m-1], dd),
               r"%04d-%02d-%02d" % (d.year, m, dd)]
        # faixas do tipo "20, 21 e 22 de novembro" ou "20 a 22/11"
        ps.append(r"\b0?%d\s*(,|e|a|–|-|até)\s*\d{1,2}(\s*(,|e|a|–|-)\s*\d{1,2})*\s*(/\s*0?%d\b|de\s+%s)" % (dd, m, MESES[m-1]))
    return re.compile("|".join("(?:%s)" % p for p in ps), re.I)

def cod(fonte, linha):
    return hashlib.sha1((fonte + "|" + re.sub(r"\s+", " ", linha.strip())).encode("utf-8")).hexdigest()[:12]

def peneirar(pasta, inicio, fim, saida, contexto=4, vistos=None):
    pad = padroes(inicio, fim)
    antigos = set(json.load(open(vistos, encoding="utf-8")).get("linhas", [])) if vistos and os.path.exists(vistos) else set()
    agora = set(); fontes_novas = 0
    with open(saida, "w", encoding="utf-8") as out:
        for caminho in sorted(glob.glob(os.path.join(pasta, "F*.txt"))):
            linhas = open(caminho, encoding="utf-8", errors="replace").read().split("\n")
            cab = linhas[0] if linhas else ""
            fonte = os.path.basename(caminho)
            marcar = set(); pagina = {}; novas = set()
            atual = ""
            for i, l in enumerate(linhas):
                if l.startswith("## "): atual = l
                pagina[i] = atual
                if pad.search(l):
                    c = cod(fonte, l); agora.add(c)
                    if vistos and c in antigos: continue
                    novas.add(i)
                    for j in range(max(0, i-contexto), min(len(linhas), i+contexto+1)): marcar.add(j)
            if not marcar: continue
            fontes_novas += 1
            out.write("\n\n=================== %s\n" % cab)
            vistos = set(); ult = -9; pag_ult = None
            for i in sorted(marcar):
                l = linhas[i].strip()
                if not l or l in vistos: continue
                vistos.add(l)
                if pagina[i] != pag_ult:
                    out.write("\n%s\n" % pagina[i]); pag_ult = pagina[i]
                elif i - ult > 1: out.write("  ...\n")
                out.write(("★ " if vistos and i in novas else "") + l[:1200] + "\n"); ult = i
    if vistos:
        json.dump({"edicao": [str(inicio), str(fim)], "linhas": sorted(antigos | agora)},
                  open(saida + ".vistos", "w", encoding="utf-8"))
    print(f"{fontes_novas} fonte(s) com trechos" + (" novos" if vistos else ""), "->", saida)

if __name__ == "__main__":
    pasta, ini, fim, saida = sys.argv[1:5]
    vistos = sys.argv[5] if len(sys.argv) > 5 else None
    f = lambda s: datetime.date(*map(int, s.split("-")))
    peneirar(pasta, f(ini), f(fim), saida, vistos=vistos)
