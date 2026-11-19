# Uso: python3 faixas.py <início AAAA-MM-DD> <fim AAAA-MM-DD> <pasta com F*.txt> [outra pasta...]
# Acha faixas de datas ("7 Novembro 2026 - 9 Janeiro 2027", "07/11/26 a 01/02/27", "até 20/12", "08 out - 21 nov") que cobrem a semana
import re, sys, glob, os, datetime
M = {m:i+1 for i,m in enumerate("jan fev mar abr mai jun jul ago set out nov dez".split())}
ini, fim = (datetime.date(*map(int, a.split("-"))) for a in sys.argv[1:3])
mes = r"(jan|fev|mar|abr|mai|jun|jul|ago|set|out|nov|dez)[a-zç]*\.?"
dt_txt = r"(\d{1,2})º?\s*(?:de\s+)?%s(?:\s*(?:de\s+)?(20\d\d))?" % mes
dt_num = r"(\d{1,2})[/.](\d{1,2})(?:[/.](\d{2,4}))?"
sep = r"\s*(?:-|–|—|a|até|>|ao)\s*"
R1 = re.compile(dt_txt + sep + dt_txt, re.I)
R2 = re.compile(dt_num + sep + dt_num, re.I)
R3 = re.compile(r"at[ée]\s+(?:o\s+dia\s+|dia\s+)?(?:" + dt_txt + "|" + dt_num + ")", re.I)
def mk(d, m, y, ref=None):
    try:
        m = M[m[:3].lower()] if not str(m).isdigit() else int(m)
        y = int(y) if y else (ref or ini.year)
        if y < 100: y += 2000
        return datetime.date(y, m, int(d))
    except Exception: return None
def cobre(l):
    for r in R1.finditer(l):
        b = mk(r[4], r[5], r[6]); a = mk(r[1], r[2], r[3], b.year if b else None)
        if a and b and a > b and not r[3]: a = a.replace(year=b.year-1)
        if a and b and a <= fim and b >= ini and (b-a).days < 500: return True
    for r in R2.finditer(l):
        b = mk(r[4], r[5], r[6]); a = mk(r[1], r[2], r[3], b.year if b else None)
        if a and b and a > b and not r[3]: a = a.replace(year=b.year-1)
        if a and b and a <= fim and b >= ini and (b-a).days < 500: return True
    for r in R3.finditer(l):
        b = mk(r[1], r[2], r[3]) if r[1] else mk(r[4], r[5], r[6])
        if b and ini <= b <= fim + datetime.timedelta(days=220): return True
    return False
for pasta in sys.argv[3:]:
    for c in sorted(glob.glob(os.path.join(pasta, "F*.txt"))):
        L = open(c, encoding="utf-8", errors="replace").read().split("\n")
        hits = [i for i,l in enumerate(L) if len(l) < 1500 and cobre(l)]
        if not hits: continue
        print("\n=====", L[0]); vistos=set()
        for i in hits:
            bloco = [x.strip()[:260] for x in L[max(0,i-2):i+3] if x.strip()]
            k = L[i].strip()
            if k in vistos: continue
            vistos.add(k); print("  |", " ¦ ".join(bloco))
