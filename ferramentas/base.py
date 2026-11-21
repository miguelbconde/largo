"""Peças comuns ao robô (montar.py) e à entrega das fichas (entregar.py).

A programação mora numa base permanente, dados/fichas.json: uma ficha por evento ou exposição, com
todas as sessões que a fonte informou. A edição da semana (quinta a quarta) não é escrita à mão:
o robô a monta todo dia a partir da base, cortando o que já passou.
"""
import datetime as dt
import hashlib
import json
import os
import re
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS = os.path.join(RAIZ, "dados")
ARQ_FICHAS = os.path.join(DADOS, "fichas.json")
ARQ_CONF = os.path.join(DADOS, "conferencia.json")
ARQ_DEST = os.path.join(DADOS, "destaques.json")
ARQ_ENTREGAS = os.path.join(DADOS, "entregas.json")
BRT = dt.timezone(dt.timedelta(hours=-3))  # Rio, sem horário de verão
MESES = "janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro".split()


def hoje():
    """Data de hoje no Rio (AAAA-MM-DD). A variável HOJE permite simular outro dia nos testes."""
    return os.environ.get("HOJE") or dt.datetime.now(BRT).date().isoformat()


def edicao_de(dia):
    """Edição que contém o dia: de quinta a quarta. O identificador é a data da quinta."""
    d = dt.date.fromisoformat(dia)
    ini = d - dt.timedelta(days=(d.weekday() - 3) % 7)
    fim = ini + dt.timedelta(days=6)
    if ini.month == fim.month:
        titulo = f"Edição de {ini.day} a {fim.day} de {MESES[fim.month - 1]} de {fim.year}"
    else:
        titulo = f"Edição de {ini.day} de {MESES[ini.month - 1]} a {fim.day} de {MESES[fim.month - 1]} de {fim.year}"
    return {"id": ini.isoformat(), "inicio": ini.isoformat(), "fim": fim.isoformat(), "titulo": titulo}


def slug(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def novo_id(titulo, local):
    return "f-" + hashlib.sha1((slug(titulo) + "|" + slug(local)).encode()).hexdigest()[:10]


def ler(caminho, padrao):
    return json.load(open(caminho, encoding="utf-8")) if os.path.exists(caminho) else padrao


def gravar(caminho, obj):
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write("\n")


if __name__ == "__main__":  # python3 ferramentas/base.py  -> hoje e a edição de hoje
    e = edicao_de(hoje())
    print(hoje(), e["id"], e["inicio"], e["fim"])
