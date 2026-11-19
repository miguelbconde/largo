# Repórter A — fichas da edição de 19 a 25/11/2026
# Cada evento guarda o trecho exato da fonte usado para preencher datas, horários e preços.
# Fontes desta edição: PDF semanal da SMC (19 a 25/11) e PDF "Programação Unificada – Novembro Negro 2026",
# os dois enviados pela coordenação editorial em 19/11. CCBB, Sesc e Circo Voador vêm da coleta de 15–17/11.
import json, os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EDICAO = {"id": "2026-11-19", "inicio": "2026-11-19", "fim": "2026-11-25",
          "titulo": "Edição de 19 a 25 de novembro de 2026"}

SMC = ("Programação Semanal da Cultura Rio 19–25/11 (PDF SMC)",
       "https://cultura.prefeitura.rio/agendacultural/")
NN = ("Programação Unificada – Novembro Negro 2026 (PDF SMC)",
      "https://cultura.prefeitura.rio/agendacultural/")

L = {  # local: (nome, endereço, bairro, região)
 "sergioporto": ("Espaço Cultural Sérgio Porto", "Rua Visconde de Silva, ao lado do nº 292", "Humaitá", "Zona Sul"),
 "cafepequeno": ("Teatro Municipal Café Pequeno", "Av. Ataulfo de Paiva, 269", "Leblon", "Zona Sul"),
 "domingos": ("Teatro Municipal Domingos Oliveira (Planetário)", "Rua Padre Leonel Franca, 240", "Gávea", "Zona Sul"),
 "werneck": ("Teatro de Fantoches e Marionetes Carlos Werneck de Carvalho", "Aterro do Flamengo, altura do Posto 3", "Flamengo", "Zona Sul"),
 "mhc": ("Museu Histórico da Cidade", "Estrada Santa Marinha, s/nº", "Gávea", "Zona Sul"),
 "memorial": ("Memorial Getúlio Vargas", "Praça Luís de Camões, s/nº", "Glória", "Zona Sul"),
 "carlosgomes": ("Teatro Municipal Carlos Gomes", "Praça Tiradentes, s/nº", "Centro", "Centro"),
 "ruth": ("Teatro Municipal Ruth de Souza", "Rua Murtinho Nobre, 169", "Santa Teresa", "Centro"),
 "amanha": ("Museu do Amanhã", "Praça Mauá, 1", "Centro", "Centro"),
 "muhcab": ("Muhcab – Museu da História e da Cultura Afro-Brasileira", "Rua Pedro Ernesto, 80", "Gamboa", "Centro"),
 "mar": ("Museu de Arte do Rio (MAR)", "Praça Mauá, 5", "Centro", "Centro"),
 "helio": ("Centro Municipal de Arte Hélio Oiticica", "Rua Luís de Camões, 68", "Centro", "Centro"),
 "calouste": ("Centro Municipal de Artes Calouste Gulbenkian", "Rua Benedito Hipólito, 125", "Praça XI", "Centro"),
 "annita": ("Biblioteca Municipal Annita Porto Martins", "Rua Sampaio Viana, 357", "Rio Comprido", "Centro"),
 "ccbb": ("Centro Cultural Banco do Brasil (CCBB)", "Rua Primeiro de Março, 66", "Centro", "Centro"),
 "circo": ("Circo Voador", "Rua dos Arcos, s/nº", "Lapa", "Centro"),
 "cidadeartes": ("Cidade das Artes", "Av. das Américas, 5.300", "Barra da Tijuca", "Zona Sudoeste"),
 "milton": ("Biblioteca Municipal Milton Santos (Areninha Jacob do Bandolim)", "Praça do Barro Vermelho (Praça Geraldo Simonard), s/nº", "Pechincha", "Zona Sudoeste"),
 "moacyr": ("Biblioteca Municipal Moacyr Teixeira", "", "", ""),
 "jacob": ("Areninha Cultural Jacob do Bandolim", "Praça do Barro Vermelho (Praça Geraldo Simonard), s/nº", "Pechincha", "Zona Sudoeste"),
 "dyla": ("Centro Cultural Professora Dyla Sylvia de Sá", "Rua Barão, 1.180", "Praça Seca", "Zona Sudoeste"),
 "ziembinski": ("Teatro Municipal Ziembinski", "Rua Heitor Beltrão, s/nº", "Tijuca", "Zona Norte"),
 "guignoltijuca": ("Teatro Municipal de Guignol da Tijuca", "Praça Comandante Xavier de Brito, s/nº", "Tijuca", "Zona Norte"),
 "musicacarioca": ("Centro da Música Carioca Artur da Távola", "Rua Conde de Bonfim, 824", "Tijuca", "Zona Norte"),
 "coreografico": ("Centro Coreográfico da Cidade do Rio de Janeiro", "Rua José Higino, 115", "Tijuca", "Zona Norte"),
 "dicro": ("Arena Cultural Dicró", "Rua Flora Lobo, Parque Ary Barroso, s/nº", "Penha Circular", "Zona Norte"),
 "fernandotorres": ("Arena Cultural Fernando Torres", "Rua Bernardino de Andrade, 200 (Parque de Madureira)", "Madureira", "Zona Norte"),
 "terra": ("Areninha Cultural Terra", "Rua Marcos de Macedo, s/nº", "Guadalupe", "Zona Norte"),
 "zefiro": ("Areninha Cultural Carlos Zéfiro", "Estrada Marechal Alencastro, s/nº", "Anchieta", "Zona Norte"),
 "jorgeamado": ("Biblioteca Municipal Jorge Amado (Areninha Herbert Vianna)", "Rua Ivanildo Alves, s/nº", "Maré", "Zona Norte"),
 "marques": ("Biblioteca Municipal Marques Rebelo", "Rua Guapeni, 61", "Tijuca", "Zona Norte"),
 "sesctijuca": ("Sesc Tijuca", "Rua Barão de Mesquita, 539", "Tijuca", "Zona Norte"),
 "hermeto": ("Areninha Cultural Hermeto Pascoal", "Praça Primeiro de Maio, s/nº", "Bangu", "Zona Oeste"),
 "sandra": ("Areninha Cultural Sandra de Sá", "Rua Doze, 1", "Santa Cruz", "Zona Oeste"),
 # ---- locais novos na edição de 19/11 ----
 "gonzaguinha": ("Teatro Municipal Gonzaguinha", "Rua Benedito Hipólito, 125", "Praça XI", "Centro"),
 "leagarcia": ("Teatro Correios Léa Garcia", "Rua Visconde de Itaboraí, 20", "Centro", "Centro"),
 "terreirocontemp": ("Terreiro Contemporâneo (Teatro Chica Xavier, Galeria Quilombo e Sala Rubens Barbot)", "Rua Carlos de Carvalho, 53", "Centro", "Centro"),
 "gloriamaria": ("Parque Glória Maria", "Rua Murtinho Nobre, 169", "Santa Teresa", "Centro"),
 "bonifacio": ("Biblioteca José Bonifácio (Muhcab)", "Rua Pedro Ernesto, 80", "Gamboa", "Centro"),
 "alencar": ("Biblioteca Municipal José de Alencar", "Rua Monte Alegre, 306 (anexo ao Centro Cultural Laurinda Santos Lobo)", "Santa Teresa", "Centro"),
 "firmina": ("Biblioteca Municipal Maria Firmina dos Reis", "Rua Afonso Cavalcanti, 455", "Cidade Nova", "Centro"),
 "passeio": ("Passeio Público", "Passeio Público", "Centro", "Centro"),
 "estacio": ("Praça do Estácio (saída B do metrô)", "Praça do Estácio", "Estácio", "Centro"),
 "zumbi": ("Monumento a Zumbi dos Palmares", "Praça XI, em frente ao Terreirão do Samba", "Praça XI", "Centro"),
 "crescer": ("Circo Crescer e Viver", "Rua Carmo Neto, 143", "Cidade Nova", "Centro"),
 "ziraldo": ("Biblioteca Municipal Ziraldo (Cidade das Artes)", "Av. das Américas, 5.300", "Barra da Tijuca", "Zona Sudoeste"),
 "renato": ("Areninha Cultural Renato Russo", "Parque Poeta Manuel Bandeira, s/nº", "Cocotá (Ilha do Governador)", "Zona Norte"),
 "joaobosco": ("Areninha Cultural João Bosco", "", "Vista Alegre", "Zona Norte"),
 "jovelina": ("Arena Cultural Jovelina Pérola Negra", "Praça Ênio, s/nº", "Pavuna", "Zona Norte"),
 "chacrinha": ("Arena Cultural Abelardo Barbosa – Chacrinha", "Rua Soldado Eliseu Hipólito, s/nº", "Pedra de Guaratiba", "Zona Oeste"),
 "gil": ("Areninha Cultural Gilberto Gil", "Av. Marechal Fontenelle, 5.000", "Realengo", "Zona Oeste"),
 "juras": ("Praça das Juras", "Praça das Juras (referência: Nave do Conhecimento de Padre Miguel)", "Padre Miguel", "Zona Oeste"),
 "moacyr": ("Espaço de Leitura Moacyr Teixeira", "Rua Doze, s/nº", "Santa Cruz", "Zona Oeste"),
 "casabonifacio": ("Casa Bonifácio (Ateliê Bonifácio – Espaço Afro-Carioca)", "Rua do Senado, 47", "Centro", "Centro"),
 "bpmanguinhos": ("Biblioteca Parque de Manguinhos", "", "Manguinhos", "Zona Norte"),
}

EV = []
def ev(titulo, area, local, sinopse, trecho, fonte, sessoes=None, cartaz=None,
       preco="", pmin=None, pmax=None, gratis=False, classif="", acess="", link=None, nota="", rua=False):
    nome, end, bairro, reg = L[local]
    EV.append(dict(titulo=titulo, areas=area.split("|"), tipo="cartaz" if cartaz else "evento",
        local=nome, endereco=end, bairro=bairro, regiao=reg,
        sessoes=[{"data": s[:10], "hora": s[11:16]} for s in (sessoes or [])],
        cartaz=cartaz, preco_texto=preco, preco_min=pmin, preco_max=pmax, gratis=gratis,
        classificacao=classif, acessibilidade=acess, na_rua=rua, sinopse=sinopse,
        fonte=fonte[0], link=link or fonte[1], trecho_fonte=trecho, nota_redacao=nota))
def C(inicio, fim, horario): return {"inicio": inicio, "fim": fim, "horario": horario}
def D(*xs): return ["2026-11-%s %s" % (x[:2], x[3:]) for x in xs]   # D("20 19:00") -> "2026-11-20 19:00"
G = dict(preco="Grátis", gratis=True)

# =========== PDF SEMANAL DA SMC (19 a 25/11). Dias da semana viram datas dentro da semana: ===========
# qui 19 · sex 20 · sáb 21 · dom 22 · seg 23 · ter 24 · qua 25

# ---------------- ZONA SUL ----------------
ev("Minha Vó Ri", "Teatro", "sergioporto",
   "Primeiro solo de Júlia Bernat, dirigido por Débora Lamm. Mistura autoficção e pesquisa sobre a história do ativismo lésbico, com trilha de Ângela Ro Ro e Cássia Eller.",
   'Espetáculo “Minha Vó Ri” Sextas e Sábados às 20h, Domingos às 19h. Classificação 14 anos R$ 30 a R$ 60.', SMC,
   sessoes=D("20 20:00", "21 20:00", "22 19:00"), preco="R$ 30 a R$ 60", pmin=30, pmax=60, classif="14 anos")
ev("Equina", "Teatro", "sergioporto",
   "Espetáculo de dança de Aline Bernardi e Dani Lima sobre os laços de cuidado entre humanos e cavalos, a partir da pesquisa de doutorado de Aline.",
   'Espetáculo “Equina” sábados 19h e domingos 18h. Até 29/11. R$ 30 a R$ 60. 18 anos.', SMC,
   sessoes=D("21 19:00", "22 18:00"), preco="R$ 30 a R$ 60", pmin=30, pmax=60, classif="18 anos")
ev("O Último Dia da Minha Vida", "Teatro", "cafepequeno",
   "Numa noite decisiva, Ângelo abre o baú onde guarda o que o tempo tentou apagar. Drama com humor ácido, em última semana.",
   'Espetáculo “O Último Dia da Minha Vida” Terças e quartas-feiras, às 20h. Até 25/11, R$ 10 a R$20. 14 anos.', SMC,
   sessoes=D("24 20:00", "25 20:00"), preco="R$ 10 a R$ 20", pmin=10, pmax=20, classif="14 anos")
ev("Nada sob Controle", "Teatro", "cafepequeno",
   "Comédia circense do Circo Teatro Saltimbanco, feita de situações cômicas, desencontros e improviso, na tradição do palhaço de circo. Última semana.",
   '“Nada sob Controle” 13 a 22 de novembro Sextas e Sábados às 20h e Domingos às 19h R$ 15 | R$ 30. 14 anos. Nada Sob Controle é um espetáculo de comédia circense do Circo Teatro Saltimbanco', SMC,
   sessoes=D("20 20:00", "21 20:00", "22 19:00"), preco="R$ 15 a R$ 30", pmin=15, pmax=30, classif="14 anos",
   nota="O PDF traz o espetáculo dentro do bloco do Teatro Café Pequeno, logo depois de “O Último Dia da Minha Vida”, sem repetir o nome do teatro.")
ev("A Cura da Terra – Pequenas Revoluções", "Teatro|Música", "domingos",
   "Uma banda se prepara para o show e conta, em vozes e histórias, algumas das principais revoluções indígenas da América Latina. Dialoga com o livro “A Cura da Terra”, de Eliane Potiguara. Estreia.",
   'Espetáculo “A Cura da Terra – Pequenas Revoluções” Sábados e domingos, às 11h. De 21 a 29/11. Grátis. Livre.', SMC,
   sessoes=D("21 11:00", "22 11:00"), classif="Livre", **G)
ev("Superiores", "Teatro", "domingos",
   "Nove atores criam com o corpo e a voz todos os sons e ambientes de uma fábula sobre poder, falada numa língua inventada que o público entende pelo som.",
   'Espetáculo “Superiores” Sextas e sábados, 20h, domingos, 19h. Até 29/11. R$ 30 a R$ 60. Livre.', SMC,
   sessoes=D("20 20:00", "21 20:00", "22 19:00"), preco="R$ 30 a R$ 60", pmin=30, pmax=60, classif="Livre")
ev("A Menina Dança", "Infantil|Teatro", "werneck",
   "Dança-teatro para crianças sobre Maria Felipa de Oliveira, marisqueira negra e heroína da Independência da Bahia, com maracatu, jongo, maculelê e samba de roda.",
   'Teatro de Fantoches e Marionetes Carlos Werneck de Carvalho [...] Espetáculo “A Menina Dança” Sexta-feira (20/11), às 11h. Grátis. Livre.', SMC,
   sessoes=D("20 11:00"), classif="Livre", **G,
   nota="Horário diverge entre as duas fontes: o PDF semanal diz 11h; o PDF do Novembro Negro diz “20/11 (sexta, feriado), às 10h, no Teatro Carlos Werneck”. Publicado com o horário do PDF semanal.")
ev("Exposição principal do Museu Histórico da Cidade", "Artes Visuais", "mhc",
   "Exposição principal do museu, na Gávea.",
   'Exposição Principal do Museu Histórico da Cidade Terça-feira a domingo, das 9h às 16h. Grátis. Livre.', SMC,
   cartaz=C(None, None, "Terça a domingo, 9h–16h"), classif="Livre", **G)
ev("Pai – Pretos no Branco, de Diogo Brozoski", "Artes Visuais", "memorial",
   "Ilustrações e pinturas inéditas em que o artista, homem branco e pai de duas crianças negras, trata da paternidade e das questões afrodiaspóricas da sua família.",
   '"Pai – Pretos no Branco", de Diogo Brozoski Quarta-feira a domingo, das 10h às 17h. Até 06/12 . Grátis. Livre', SMC,
   cartaz=C(None, "2026-12-06", "Quarta a domingo, 10h–17h"), classif="Livre", **G)
ev("CORPO: onde a memória e os processos se inscrevem", "Artes Visuais", "memorial",
   "Coletiva com 67 artistas de várias regiões do país em torno do corpo como arquivo vivo, em múltiplas linguagens.",
   'Exposição "CORPO: onde a memória e os processos se inscrevem" Quarta-feira a domingo, das 10h às 17h. Até 06/12 . Grátis. Livre', SMC,
   cartaz=C(None, "2026-12-06", "Quarta a domingo, 10h–17h"), classif="Livre", **G)
ev("Uma vida à beira-mar sob o olhar do arquiteto, de Gisele Nossar", "Artes Visuais", "memorial",
   "A artista leva para o bordado os traços e as curvas do imaginário do Rio, em diálogo com croquis de Niemeyer e Le Corbusier.",
   'Exposição "Uma vida à beira-mar sob o olhar do arquiteto", de Gisele Nossar Quarta-feira a domingo, das 10h às 17h. Até 06/12 . Grátis. Livre', SMC,
   cartaz=C(None, "2026-12-06", "Quarta a domingo, 10h–17h"), classif="Livre", **G)
ev("Exposição permanente Getúlio Vargas", "Artes Visuais", "memorial",
   "Exposição permanente do memorial, na Glória.",
   'Exposição permanente Getulio Vargas Quarta-feira a domingo, das 10h às 17h. Grátis. Livre.', SMC,
   cartaz=C(None, None, "Quarta a domingo, 10h–17h"), classif="Livre", **G)

# ---------------- CENTRO ----------------
ev("Moraes Musical Moreira", "Teatro|Música", "carlosgomes",
   "Musical sobre a vida e a obra de Moraes Moreira, em linguagem de cordel: o Poeta Cantador revisita a jornada do jovem Vaqueiro do Som pelo país.",
   'Espetáculo “Moraes Musical Moreira” Quintas e sextas-feiras, às 19h, sábados, às 17h e às 20h, e domingos, às 17h. R$ 40 a R$ 80. 12 anos.', SMC,
   sessoes=D("19 19:00", "20 19:00", "21 17:00", "21 20:00", "22 17:00"), preco="R$ 40 a R$ 80", pmin=40, pmax=80, classif="12 anos")
ev("Superfície: O Encontro das Marés", "Teatro", "gonzaguinha",
   "Uma jornalista presa a uma relação de controle e violência reconhece a própria história na de outra mulher. Peça sobre romper o silêncio e recomeçar.",
   'Espetáculo “Superfície: O Encontro das Marés” Sexta-feira (20/11), às 19h. R$ 5 a R$ 10. 12 anos.', SMC,
   sessoes=D("20 19:00"), preco="R$ 5 a R$ 10", pmin=5, pmax=10, classif="12 anos")
MOSTRA_PRECO = dict(preco="Grátis ou até R$ 10 (ver programação)", pmin=5, pmax=10)
MOSTRA_NOTA = ("Preço: o PDF semanal dá “R$ 5 a R$ 10” para a Mostra; o PDF do Novembro Negro diz “Majoritariamente gratuito; apenas uma sessão "
               "com ingressos a preços populares (R$ 10 a inteira e R$ 5 a meia)”, sem dizer qual sessão. Classificação: 10 anos no PDF semanal, Livre no outro.")
ev("Festa, Fé e Luta (Mostra do Impossível)", "Teatro", "leagarcia",
   "Um jovem professor resgata a memória de grandes referências negras brasileiras e os ensinamentos da mãe. Peça de João Pessanha na 8ª Mostra do Impossível, festival de arte negra da Confraria do Impossível.",
   'Mostra do Impossível Quinta e sexta-feira (19 e 20/11). R$ 5 a R$ 10. 10 anos. [...] Espetáculo “Festa, Fé e Luta” Quinta-feira (19/11), às 19h. || Novembro Negro: 19h – Espetáculo Festa, Fé e Luta, de João Pessanha (Teatro Correios Léa Garcia)', SMC,
   sessoes=D("19 19:00"), classif="10 anos", nota=MOSTRA_NOTA, link="https://confrariadoimpossivel.com/2026-mostra-do-impossivel/", **MOSTRA_PRECO)
ev("Sortilégios – leitura dramatizada (Mostra do Impossível)", "Teatro", "leagarcia",
   "O Coletivo Nyogolon lê em cena o texto “Sortilégios”, dentro da 8ª Mostra do Impossível.",
   'Leitura “Sortilégios” Sexta-feira (19/11), às 18h. Grátis A leitura dramatizada do texto Sortilégios com o grupo Nyogolon || Novembro Negro: 20/11 (sexta-feira) [...] 18h – Leitura Dramatizada Sortilégios, com Coletivo Nyogolon (Teatro Correios Léa Garcia)', SMC,
   sessoes=D("20 18:00"), classif="10 anos", link="https://confrariadoimpossivel.com/2026-mostra-do-impossivel/", **G,
   nota="O PDF semanal escreve “Sexta-feira (19/11)”, mas 19/11 é quinta. O PDF do Novembro Negro confirma sexta, 20/11.")
ev("Cabeça de Porco – Retratos de um Território (Mostra do Impossível)", "Teatro", "leagarcia",
   "A partir da crença de que uma cabeça de porco enterrada impede um lugar de prosperar, a peça do Grupo Código fala de luta por moradia e sonhos da periferia, entre o forró e o funk. Direção de Juliana França, indicada ao Prêmio Shell.",
   'Espetáculo “Cabeça de porco” Sexta-feira (19/11), às 19h. Indicado ao 36º Prêmio Shell de Teatro (2025) na categoria "Direção" para Juliana França || Novembro Negro: 20/11 (sexta-feira) [...] 19h – Espetáculo Cabeça de Porco, do Grupo Código (Teatro Correios Léa Garcia)', SMC,
   sessoes=D("20 19:00"), classif="10 anos", link="https://confrariadoimpossivel.com/2026-mostra-do-impossivel/", **MOSTRA_PRECO,
   nota="O PDF semanal escreve “Sexta-feira (19/11)”, mas 19/11 é quinta. O PDF do Novembro Negro confirma sexta, 20/11. " + MOSTRA_NOTA)
ev("Tudo Entre Nós – leitura dramatizada e roda de conversa", "Teatro", "leagarcia",
   "Dezesseis anos depois da separação, um ex-casal negro e maduro se reencontra para vender o apartamento. Comédia romântica de Davi Martins, com Lica Oliveira e Valdo Boaventura, seguida do “Papo entre Nós”.",
   'Tudo Entre Nós – Leitura Dramatizada, seguida de roda de conversa “Papo entre Nós” Serviço: Sábado, 21 de novembro, às 18h. Grátis. 16 anos.', SMC,
   sessoes=D("21 18:00"), classif="16 anos", **G)
ev("Zuzuê Contos Africanos", "Infantil|Teatro", "ruth",
   "Paulinha Cavalcanti, Anderson Barreto e Árvore Vicente narram histórias afro-diaspóricas, com Libras integrada à cena. Cerca de 50 minutos.",
   'Espetáculo “Zuzuê Contos Africanos” Sábado e domingo, às 11h. Até 29/11. R$ 20 a R$ 40. Livre. [...] com libras como parte integrante da cena', SMC,
   sessoes=D("21 11:00", "22 11:00"), preco="R$ 20 a R$ 40", pmin=20, pmax=40, classif="Livre", acess="Libras integrada à cena")
ev("Providência 130: Histórias que Fazem Território", "Artes Visuais", "amanha",
   "Às vésperas dos 130 anos do Morro da Providência, a mostra reúne cerca de 300 fotografias de moradores e dez histórias, em curadoria feita pelo museu com o território. Abre nesta quinta.",
   'Exposição “Providência 130: Histórias que Fazem Território” Quinta a terça-feira, das 10h às 18h (última entrada às 17h). De 19/11 a 17/11/2027. R$ 20 a R$ 40. Livre.', SMC,
   cartaz=C("2026-11-19", "2027-11-17", "Quinta a terça, 10h–18h (última entrada 17h)"), preco="R$ 20 a R$ 40", pmin=20, pmax=40, classif="Livre")
ev("Visita mediada: Imersão", "Artes Visuais", "amanha",
   "Visita conduzida pelos educadores do museu, que convida a mergulhar nas narrativas das exposições.",
   'Visitas Mediadas: Imersão Sexta-feira (20/11), às 11h. Grátis. Livre.', SMC,
   sessoes=D("20 11:00"), classif="Livre", **G)
ev("Inside Out – 15 anos", "Artes Visuais", "amanha",
   "Edição especial do projeto do artista francês JR: retratos em preto e branco, em grande escala, de gente da vizinhança. O público pode tirar sua foto e entrar na intervenção.",
   '“Inside Out – 15 anos’ Sábado e domingo (21 e 22/11), às 10h. Grátis. Livre.', SMC,
   sessoes=D("21 10:00", "22 10:00"), classif="Livre", **G)
ev("Do Cosmos a Nós", "Artes Visuais", "amanha",
   "Exposição principal do museu: uma narrativa multimídia em cinco momentos (Cosmos, Terra, Antropoceno, Amanhãs e Nós).",
   'Exposição principal do Museu do Amanhã “Do Cosmos a Nós” Quinta a terça-feira, das 10h às 18h (última entrada às 17h). R$ 20 a R$ 40. Livre.', SMC,
   cartaz=C(None, None, "Quinta a terça, 10h–18h (última entrada 17h)"), preco="R$ 20 a R$ 40", pmin=20, pmax=40, classif="Livre")
ev("Abertura da exposição “7 Ervas”", "Artes Visuais", "muhcab",
   "Noite de abertura da coletiva de sete artistas mulheres, com curadoria de Marcelo Campos, que marca o primeiro aniversário da Galeria Berê.",
   'Novembro Negro: 2. Abertura da exposição “7 Ervas” Data e horário: 19/11/2026, das 18h às 21h | Local: Galeria Berê | Valor: Gratuita', NN,
   sessoes=D("19 18:00"), **G)
ev("7 Ervas", "Artes Visuais", "muhcab",
   "Sete artistas mulheres partem dos usos e sentidos das ervas nos saberes afro-brasileiros para falar de proteção, memória, cuidado e renovação. Curadoria de Marcelo Campos, na Galeria Berê.",
   'ABERTURA - Exposição “7 Ervas’ Terça-feira a domingo, das 10h às 17h, na Galeria Berê. De 20/11 a 10/01/2027. Grátis. Livre.', SMC,
   cartaz=C("2026-11-20", "2027-01-10", "Terça a domingo, 10h–17h (Galeria Berê)"), classif="Livre", **G)
ev("Samba da Dida Bar", "Música", "muhcab",
   "Samba no feriado da Consciência Negra, do meio-dia à noite, no Muhcab.",
   'Samba da Dida Bar Sexta-feira, 20 de novembro, das 12h às 21h. Entrada colaborativa. Livre.', SMC,
   sessoes=D("20 12:00"), preco="Entrada colaborativa", gratis=True, classif="Livre")
ev("Festival Trançando Cultura do Ayó", "Festas & Feiras", "muhcab",
   "Um dia dedicado às tranças, à arte e aos saberes tradicionais afro-brasileiros.",
   'Festival Trançando Cultura do Ayó Domingo, 22 de novembro, das 10h às 17h45. Grátis. Livre.', SMC,
   sessoes=D("22 10:00"), classif="Livre", **G)
ev("Protagonismos: Memória, Orgulho e Identidade", "Artes Visuais", "muhcab",
   "Exposição em cartaz no Muhcab, na Gamboa.",
   'Exposição “Protagonismos: Memória, Orgulho e Identidade” Terça-feira a domingo, das 10h às 17h. Grátis. Livre.', SMC,
   cartaz=C(None, None, "Terça a domingo, 10h–17h"), classif="Livre", **G)
ev("Bebês no MAR – exposição Guilherme Kid", "Infantil|Artes Visuais", "mar",
   "Visita educativa para bebês de 0 a 2 anos e suas famílias. É preciso se inscrever pelo link nas redes do museu.",
   'Bebês no MAR – exposição Guilherme Kid Sábado(21/11), às 10h e 11h. Grátis, com inscrição (link nas redes do MAR). Livre. Visita educativa para familiares e seus bebês de 0 a 2 anos.', SMC,
   sessoes=D("21 10:00", "21 11:00"), preco="Grátis (com inscrição)", gratis=True, classif="Livre")
ev("Zanele Muholi", "Artes Visuais", "mar",
   "Fotografias de Zanele Muholi, ativista visual da África do Sul que há mais de uma década documenta a vida de pessoas negras LGBTI no país. Últimas semanas.",
   'Exposição “Zanele Muholi” Quinta a terça-feira, das 11h às 18h (última entrada às 17h). Até 29/11. R$ 10 a R$ 20 (terças-feiras são gratuitas). Livre.', SMC,
   cartaz=C(None, "2026-11-29", "Quinta a terça, 11h–18h · grátis às terças"), preco="R$ 10 a R$ 20 (grátis às terças)", pmin=10, pmax=20, classif="Livre")
ev("Tião – Um fotógrafo da Providência", "Artes Visuais", "mar",
   "O acervo de Sebastião Pires, o Tião, fotógrafo e vizinho do museu. Últimas semanas.",
   'Exposição “Tião-Um fotógrafo da Providência” Quinta a terça-feira, das 11h às 18h (última entrada às 17h). Até 29/11 R$ 10 a R$ 20 (terças-feiras são gratuitas). Livre.', SMC,
   cartaz=C(None, "2026-11-29", "Quinta a terça, 11h–18h · grátis às terças"), preco="R$ 10 a R$ 20 (grátis às terças)", pmin=10, pmax=20, classif="Livre")
ev("Ponto de Leitura: Brasilidades que vêm de Áfricas", "Livros & Debates", "mar",
   "Livros, imagens e sons sobre as contribuições africanas ao Brasil, do “pretuguês” de Lélia Gonzalez às cozinhas da diáspora.",
   'Ponto de Leitura - Brasilidades que vêm de Áfricas Quinta a terça-feira, das 11h às 17h. Até 30/11. R$ 10 a R$ 20 (terças-feiras são gratuitas). Livre. || Novembro Negro: das 11h às 17h | Local: Biblioteca do MAR | Valor: Gratuita', SMC,
   cartaz=C(None, "2026-11-30", "Quinta a terça, 11h–17h"), preco="R$ 10 a R$ 20 (grátis às terças)", pmin=10, pmax=20, classif="Livre",
   nota="Preço diverge entre as fontes: o PDF semanal dá R$ 10 a R$ 20 (grátis às terças); o do Novembro Negro diz “Valor: Gratuita”.")
ev("Festival Rio Santa – Edição Especial Zumbi dos Palmares", "Festas & Feiras", "gloriamaria",
   "Festival que celebra a cultura negra e a figura de Zumbi dos Palmares no parque de Santa Teresa.",
   'Novembro Negro: Parque Glória Maria 1. Festival Rio Santa – Edição Especial Zumbi dos Palmares Data e horário: 21/11, às 10h | Classificação: Livre | Valor: Gratuito | Linguagem: Festival', NN,
   sessoes=D("21 10:00"), classif="Livre", rua=True, **G)
ev("Na capoeira de Carybé", "Livros & Debates", "helio",
   "Conversa sobre a história da capoeira, criada por pessoas escravizadas no Brasil colonial como forma de resistência. Atividade da programação de férias.",
   'Novembro Negro: Centro Municipal de Artes Hélio Oiticica 1. Programação de Férias: Na capoeira de Carybé (Consciência Negra) Data e horário: 21/11, às 14h | Classificação: Livre | Valor: Gratuito | Linguagem: Cultura Popular', NN,
   sessoes=D("21 14:00"), classif="Livre", **G)
ev("Programa Hélio Oiticica", "Artes Visuais", "helio",
   "Exposição em cartaz no centro de arte.",
   'Exposição “Programa Hélio Oiticica” Segunda-feira a sábado, das 10h às 18h. Grátis. Livre.', SMC,
   cartaz=C(None, None, "Segunda a sábado, 10h–18h"), classif="Livre", **G)
ev("12º Cortejo da Tia Ciata", "Festas & Feiras|Música", "calouste",
   "Uma escultura de Tia Ciata com mais de cinco metros abre o cortejo pelas ruas da Pequena África, com afoxé, maracatu e samba, em memória da matriarca do samba e de Zumbi. Depois, roda de samba e feira.",
   '12º Cortejo da Tia Ciata Sexta-feira (20/11), com concentração às 10h no Calouste. Grátis. Livre. O cortejo percorre ruas e avenidas do entorno do Calouste', SMC,
   sessoes=D("20 10:00"), classif="Livre", rua=True, **G)
ev("MULTIARTE 2026", "Artes Visuais", "calouste",
   "Exposição anual das oficinas do Calouste: pintura, gravura, cerâmica, mosaico, estamparia e outras técnicas.",
   'MULTIARTE 2026 – Exposição Anual das Oficinas do Coletivo Calouste Segunda à sábado, das 09h às 20h45. Até 19/12. Grátis. Livre.', SMC,
   cartaz=C(None, "2026-12-19", "Segunda a sábado, 9h–20h45"), classif="Livre", **G)
ev("Encontro com Vanessa Gomes, autora de “Fora do Lugar”", "Livros & Debates", "bonifacio",
   "A escritora conversa sobre literatura, racismo, identidade e violência contra a mulher a partir do seu romance.",
   'Biblioteca José Bonifácio Rua Pedro Ernesto, 80 — Gamboa, Rio de Janeiro 21/11/26 - 14:00 Encontro com Vanessa Gomes, a autora de “Fora do Lugar” || Novembro Negro: Data e horário: 21/11, às 14h | Valor: Gratuito | Linguagem: Literatura', SMC,
   sessoes=D("21 14:00"), **G)
ev("Clube literário infantil", "Infantil|Livros & Debates", "alencar",
   "Encontro semanal de leitura de livros infantis sobre inclusão e diversidade.",
   'Clube literário infantil Quintas-feiras, às 15h. Grátis. Livre.', SMC,
   sessoes=D("19 15:00"), classif="Livre", **G)
ev("Mesa-redonda: O Mundo que se Quer Esconder das Crianças", "Livros & Debates", "annita",
   "As autoras Nilma Lacerda e Fabíola Farias discutem o incômodo na literatura infantil, tema do livro que escreveram juntas.",
   'Mesa Redonda: O Mundo que se Quer Esconder das Crianças – O Incômodo na Literatura Infantil Quarta-feira (25/11), às 10h. Grátis. 18 anos.', SMC,
   sessoes=D("25 10:00"), classif="18 anos", **G)
ev("Maquete da Biblioteca dos Saberes", "Artes Visuais", "annita",
   "Modelo da futura biblioteca projetada por Francis Kéré para a Praça Onze, legado do Rio Capital Mundial do Livro.",
   'Exposição da Maquete da Biblioteca dos Saberes Segunda a sexta-feira, das 9h às 17h. Grátis. Livre.', SMC,
   cartaz=C(None, None, "Segunda a sexta, 9h–17h"), classif="Livre", **G)
ev("Roda de conversa com Vanessa Gomes sobre “Fora do Lugar”", "Livros & Debates", "firmina",
   "A professora e escritora fala do seu romance, que acompanha a trajetória de Júlia, mulher negra, e trata de racismo, violência contra a mulher e identidade.",
   'Roda de conversa com Vanessa Gomes sobre o livro “Fora do Lugar” Quinta-feira (19/11), às 13h. Grátis. Livre.', SMC,
   sessoes=D("19 13:00"), classif="Livre", **G)

# ---------------- ZONA SUDOESTE ----------------
ev("Maquete de Lego do Rio de Janeiro", "Artes Visuais", "cidadeartes",
   "A cidade em miniatura, montada com peças de Lego.",
   'Exposição permanente “Maquete de Lego do Rio de Janeiro” Domingo a sábado, das 10h às 18h. Grátis. Livre.', SMC,
   cartaz=C(None, None, "Todos os dias, 10h–18h"), classif="Livre", **G)
ev("Banda Sinfônica Nacional apresenta Clássicos", "Música", "cidadeartes",
   "Concerto da Banda Sinfônica Nacional.",
   'Banda Sinfônica Nacional apresenta Clássicos 19/11/2026, às 19:00', SMC,
   sessoes=D("19 19:00"), nota="A fonte não informa preço nem classificação.")
ev("Encontro literário: Maria e o Segredo da Poupança", "Livros & Debates|Infantil", "ziraldo",
   "Encontro em torno do livro “Maria e o Segredo da Poupança”.",
   'Biblioteca Ziraldo Encontro Literário: Maria e o Segredo da Poupança 21/11 às 16h Gratuito', SMC,
   sessoes=D("21 16:00"), **G,
   nota="O PDF não dá o endereço da Biblioteca Ziraldo; usei o da Cidade das Artes, onde ela funciona (regulamento das bibliotecas da SMC: “Biblioteca Municipal Ziraldo, Av. das Américas, Barra da Tijuca”). A área Infantil é dedução pelo título.")
ev("Exposição Literária – Mês da Consciência Negra", "Livros & Debates", "milton",
   "Mostra de livros de autoras e autores negros na biblioteca da Areninha Jacob do Bandolim.",
   'Novembro Negro: Biblioteca Municipal Milton Santos 1. Exposição Literária (Mês da Consciência Negra) Data e horário: em cartaz até 30/11 (de 01/11 a 30/11), a partir das 10h | Classificação indicativa: Livre | Linguagem: Exposição [...] promove uma exposição de livros de autoria negra.', NN,
   cartaz=C("2026-11-01", "2026-11-30", "A partir das 10h"), classif="Livre", nota="Preço não informado na fonte.")
ev("Festival Quem Dança é Mais Feliz", "Teatro", "jacob",
   "Festival de dança que reúne diferentes estilos numa manhã de domingo na areninha do Pechincha.",
   'Festival “Quem Dança é Mais Feliz” Domingo (22/11), às 11h. Grátis. Livre.', SMC,
   sessoes=D("22 11:00"), classif="Livre", **G)
ev("Orquestra Agogô Carioca", "Música", "dyla",
   "A orquestra de agogôs se apresenta sob a regência de Sidcley Fernandes, mestre de agogô do carnaval carioca.",
   'Show da Orquestra Agogô Carioca Sexta-feira (20/11), às 15h. Grátis. Livre.', SMC,
   sessoes=D("20 15:00"), classif="Livre", **G)
ev("Baile Charme do Projeto Black Music Soul", "Festas & Feiras|Música", "dyla",
   "Baile de charme, tradição da cultura negra e urbana do Rio, em plena manhã de sábado na Praça Seca.",
   'Baile Charme do Projeto Black Music Soul Sábado (21/11), às 11h. Grátis. Livre.', SMC,
   sessoes=D("21 11:00"), classif="Livre", **G)
ev("Rap & Repente – Artes do Improviso", "Música", "dyla",
   "Encontro entre duas tradições de rima e improviso, com conversa sobre origens e processos de criação, pensado para o público jovem.",
   'Show “Rap & Repente – Artes do Improviso” Quarta-feira (25/11), às 14h. Grátis. 12 anos.', SMC,
   sessoes=D("25 14:00"), classif="12 anos", **G)

# ---------------- ZONA NORTE ----------------
ev("Priscilla em 2L em A Cara da Mãe e o P@u do Pai", "Teatro", "ziembinski",
   "Stand-up, improviso e palhaçaria: Priscilla conta sua transição de gênero depois dos 30. Na Semana da Comédia, do Festival Queer Comedy.",
   'Semana da Comédia: Festival Queer Comedy apresenta “Priscilla em 2L em A Cara da Mãe e o P@u do Pai” Terça-feira (24/11), , às 20h. R$ 30 a R$ 60. 18 anos.', SMC,
   sessoes=D("24 20:00"), preco="R$ 30 a R$ 60", pmin=30, pmax=60, classif="18 anos")
ev("Régis Araújo em Tá Bixada", "Teatro", "ziembinski",
   "Solo de stand-up sobre amor, família e envelhecimento, do ponto de vista de um homem gay na maturidade. Na Semana da Comédia, do Festival Queer Comedy.",
   'Semana da Comédia: Festival Queer Comedy apresenta “Régis Araújo em Tá Bixada” Quarta-feira (25/11), às 20h. R$ 30 a R$ 60. 16 anos.', SMC,
   sessoes=D("25 20:00"), preco="R$ 30 a R$ 60", pmin=30, pmax=60, classif="16 anos")
ev("As Irmãs Pereira", "Teatro", "ziembinski",
   "Três irmãs entre os 60 e os 70 anos se reúnem numa casa do Largo do Boticário para decidir onde jogar as cinzas da mãe, e acabam revirando o passado e os desejos do presente.",
   'Espetáculo “As Irmãs Pereira” Sextas-feiras e sábados às 20h, e domingo às 19h. R$ 35 a R$ 70. 12 anos.', SMC,
   sessoes=D("20 20:00", "21 20:00", "22 19:00"), preco="R$ 35 a R$ 70", pmin=35, pmax=70, classif="12 anos")
ev("Quintal", "Infantil|Teatro", "ziembinski",
   "Cinco crianças do subúrbio estão prestes a perder o quintal onde brincam para um condomínio de luxo. Infantojuvenil sobre a memória dos bairros e o direito de brincar. Último fim de semana.",
   'Espetáculo “Quintal” Sábados e domingos às 16h. Até 22/11. R$ 20 a R$40. Livre.', SMC,
   sessoes=D("21 16:00", "22 16:00"), preco="R$ 20 a R$ 40", pmin=20, pmax=40, classif="Livre")
ev("A Menina Dança", "Infantil|Teatro", "guignoltijuca",
   "Dança-teatro para crianças sobre Maria Felipa de Oliveira, marisqueira negra e heroína da Independência da Bahia, com maracatu, jongo, maculelê e samba de roda.",
   'Teatro Municipal de Guignol da Tijuca [...] Espetáculo “A Menina Dança” Sexta-feira, (20/11) às 16h. Grátis. Livre. || Novembro Negro: às 16h, no Teatro de Guignol da Tijuca', SMC,
   sessoes=D("20 16:00"), classif="Livre", **G)
ev("Sétima Era apresenta Essa É a Pista", "Música", "musicacarioca",
   "Banda autoral com pé nos anos 90, que cruza rock, hip hop e funk rock em letras de crítica social. No projeto Quintas Autorais.",
   'Quintas Autorais: Sétima Era apresenta Essa É a Pista Quinta-feira (19/11), às 19h. R$ 15 a R$ 30. Livre.', SMC,
   sessoes=D("19 19:00"), preco="R$ 15 a R$ 30", pmin=15, pmax=30, classif="Livre")
ev("OMNISOUL – Música, Ancestralidade e Conexão", "Música", "musicacarioca",
   "Show autoral de Allex Guedes, com banda, entre a soul music, a MPB e as matrizes da música brasileira. Cerca de 90 minutos.",
   'Sextas Lançamentos: OMNISOUL – Música, Ancestralidade e Conexão Sexta-feira (20/11), às 19h. R$ 30 a R$ 60. Livre.', SMC,
   sessoes=D("20 19:00"), preco="R$ 30 a R$ 60", pmin=30, pmax=60, classif="Livre")
ev("Baú da Dona Ivone Lara, com Bruno Castro e Áurea Martins", "Música", "musicacarioca",
   "Parceiro de Dona Ivone Lara por mais de vinte anos, Bruno Castro canta clássicos e sambas pouco conhecidos da Primeira-Dama do Samba, com participação de Áurea Martins.",
   'Evento/Show: Sábado Homenagem – Bruno Castro apresenta Baú da Dona Ivone Lara: Tributo à Primeira-Dama do Samba com participação especial de Áurea Martins Data: 21/11/2026 – Sábado Horário: 17h Espaço: Sala Paulo Moura Ingresso: R$ 60,00 (inteira) / R$ 30,00 (meia-entrada) MORADORES DA CIDADE DO RIO DE JANEIRO PAGAM MEIA ENTRADA. Classificação: Livre', SMC,
   sessoes=D("21 17:00"), preco="R$ 30 a R$ 60 (moradores do Rio pagam meia)", pmin=30, pmax=60, classif="Livre")
ev("Ramon Araújo", "Música", "musicacarioca",
   "Voz e violão em repertório de Pixinguinha, Jobim, Caymmi, Baden Powell e Gilberto Gil, além de composições próprias. No projeto Clássicos Domingos.",
   'Clássicos Domingos apresenta Ramon Araújo Domingo (22/11), às 11h. R$ 20 a R$ 40. Livre.', SMC,
   sessoes=D("22 11:00"), preco="R$ 20 a R$ 40", pmin=20, pmax=40, classif="Livre")
ev("Meu Amigo Tempo – O Tempo Também Brinca", "Infantil", "musicacarioca",
   "A escritora Luana Rodrigues conduz brincadeiras e uma Caixa das Memórias antes de contar as histórias do seu livro “Meu Amigo Tempo”. No Domingo das Crianças.",
   'Domingo das Crianças: Luana Rodrigues apresenta Meu Amigo Tempo – O Tempo Também Brinca Domingo (22/11), às 16h. R$ 10 a R$ 20. Livre.', SMC,
   sessoes=D("22 16:00"), preco="R$ 10 a R$ 20", pmin=10, pmax=20, classif="Livre")
ev("Amanda Mendonça canta Djavan", "Música", "musicacarioca",
   "A cantora alagoana celebra os 50 anos de carreira do conterrâneo com “Oceano”, “Flor de Lis”, “Sina” e outros clássicos. No projeto Quartas Acústicas.",
   'Quartas Acústicas apresenta Amanda Mendonça Canta Djavan Quarta-feira (25/11), às 19h. R$ 25. a R$ 50 Livre.', SMC,
   sessoes=D("25 19:00"), preco="R$ 25 a R$ 50", pmin=25, pmax=50, classif="Livre")
ev("Música Brasilis", "Artes Visuais|Música", "musicacarioca",
   "Exposição em cartaz no Centro da Música Carioca.",
   'Exposição “Música Brasilis” Terça-feira a domingo, das 10h às 17h. Grátis. Livre.', SMC,
   cartaz=C(None, None, "Terça a domingo, 10h–17h"), classif="Livre", **G)
ev("Renaissance Cyclique – Premye Etensèl", "Teatro", "coreografico",
   "Solo de dança sobre heranças afro-diaspóricas, deslocamento e reinvenção, com o corpo como território de memória.",
   'Espetáculo “Renaissance Cyclique – Premye Etensèl” Sexta-feira (20/11), às 19h. R$ 20 a R$ 40. 16 anos.', SMC,
   sessoes=D("20 19:00"), preco="R$ 20 a R$ 40", pmin=20, pmax=40, classif="16 anos")
ev("Corpo-Encruzilhada", "Teatro", "coreografico",
   "Dança-teatro com percussão ao vivo, inspirada nos itans de Exu, orixá dos caminhos. Aproxima saberes afro-brasileiros das vivências da juventude periférica.",
   'Espetáculo “Corpo-Encruzilhada” Sábado (21/11), às 19h. Grátis. 12 anos.', SMC,
   sessoes=D("21 19:00"), classif="12 anos", **G)
ev("Contação de histórias: Mapa do Tesouro", "Infantil", "dicro",
   "Um pirata sai atrás de ouro e, no caminho, encontra o menino Dayo e sua avó, que vive perto do rio. Com Juliana Dandarilê, na Agroflorestinha da arena.",
   'Agroflorestinha da Arena Dicró apresenta Contação de Histórias: Mapa do Tesouro Sábado (21/11), às 10h. Grátis. Livre. [...] Tradução em Libras por estudantes da UFRJ (TradInter Lab).', SMC,
   sessoes=D("21 10:00"), classif="Livre", acess="Libras", **G)
ev("Fora do Quadro", "Teatro", "dicro",
   "Espetáculo de dança em que o muro de um quartel símbolo da ditadura vira passarela para ballroom, voguing, waacking, hip hop, jazz e sapateado.",
   'Espetáculo “Fora do Quadro” Sábado (21/11),às 19h. Grátis. 18 anos.', SMC,
   sessoes=D("21 19:00"), classif="18 anos", **G)
ev("Cravejar o Corpo, Inventar o Mundo – Madah Sodré", "Artes Visuais", "dicro",
   "Pinturas que partem do corpo travesti e trans como lugar de memória, desejo e invenção. Ocupação da Galeria L.",
   'Ocupação Galeria L: “Cravejar o Corpo, Inventar o Mundo com: Madah Sodré” Visitação de terça a domingo, das 10h. Até 12/01/2027. Grátis. Livre.', SMC,
   cartaz=C(None, "2027-01-12", "Terça a domingo, a partir das 10h"), classif="Livre", **G)
ev("Música Terapia – Banda Filarmônica Maestro Nunes", "Música", "fernandotorres",
   "Concerto da banda filarmônica, pensado como uma viagem pelo tempo e pelas emoções.",
   'MÚSICA TERAPIA, UMA VIAGEM PELO TEMPO E PELAS EMOÇÕES Dia 20 (sexta-feira), ás 19h - LIVRE - INGRESSO: R$ 30,00 (meia). || Novembro Negro: 1. Música Terapia – Banda Filarmônica Maestro Nunes Data e horário: 20/11, às 19h | Valor: R$ 40,00 (inteira) / R$ 20,00 (meia)', SMC,
   sessoes=D("20 19:00"), preco="R$ 20 a R$ 40", pmin=20, pmax=40, classif="Livre",
   nota="Preço diverge entre as fontes: o PDF semanal diz “R$ 30,00 (meia)”; o do Novembro Negro, “R$ 40,00 (inteira) / R$ 20,00 (meia)”. Publicado com o do Novembro Negro, que traz inteira e meia.")
ev("Urban Charme – Mostra de Charme (10 anos)", "Teatro", "fernandotorres",
   "Na edição de dez anos, trinta grupos de dança charme e hip hop se dividem em duas noites em Madureira.",
   'Urban Charme – Mostra de Charme (10 anos) Sábado e domingo (21 e 22/11), às 18h. R$ 20 a R$ 40. Livre.', SMC,
   sessoes=D("21 18:00", "22 18:00"), preco="R$ 20 a R$ 40", pmin=20, pmax=40, classif="Livre")
ev("Feira Negrah Cor", "Festas & Feiras", "terra",
   "Feira de afroempreendedoras com roda de conversa, sarau, dança, oficina de charme, curta-metragem e tarde de autógrafos.",
   'Feira Negrah Cor Sexta-feira (20/11), às 10h. Grátis. Livre.', SMC,
   sessoes=D("20 10:00"), classif="Livre", **G)
ev("Roda de samba Feijão do Peró-Cão", "Música", "terra",
   "Tarde de samba em Guadalupe, com a tradicional feijoada vendida a preço popular.",
   'Roda de Samba “Feijão do Peró-Cão” Sexta-feira (20/11), às 13h. Grátis. Livre.', SMC,
   sessoes=D("20 13:00"), classif="Livre", **G)
ev("Tudo por um Pop Star", "Teatro", "terra",
   "Três amigas fãs do maior astro do momento descobrem um concurso que dá a chance de conhecê-lo. Até onde vão para ficar frente a frente com o ídolo?",
   'Espetáculo “Tudo por um Pop Star” Domingo (22/11), às 10h. R$ 25 a R$ 50 Livre.', SMC,
   sessoes=D("22 10:00"), preco="R$ 25 a R$ 50", pmin=25, pmax=50, classif="Livre")
ev("Quintal do Primo", "Música", "zefiro",
   "Tarde de samba e cultura popular em Anchieta, no Dia da Consciência Negra.",
   'Quintal do Primo Dia 20/11 - 15h - Gratuito', SMC,
   sessoes=D("20 15:00"), **G)
ev("Batalha na Areninha", "Música", "zefiro",
   "Encontro de MCs em Anchieta: rimas, improviso e prêmio em dinheiro para quem vencer a noite.",
   'Batalha na Areninha Dia 21/11 - 19h - Gratuito', SMC,
   sessoes=D("21 19:00"), **G)
ev("Mensageiras da Cultura – 50 anos da Kotekitai", "Música", "zefiro",
   "A Banda Asas da Paz Kotekitai do Brasil, formada só por mulheres, celebra 50 anos de atuação no Rio em duas sessões.",
   'Mensageiras da Cultura - 50 anos da Kotekitai construindo um futuro de esperança Domingo (22/11), às 10h e 11:30h. Grátis. Livre.', SMC,
   sessoes=D("22 10:00", "22 11:30"), classif="Livre", **G,
   nota="O PDF traz o mesmo evento duas vezes, com títulos diferentes (“Asas de Kotekitai” e “Mensageiras da Cultura”). Ficou um só registro.")
ev("Quintal do Renatin", "Música|Festas & Feiras", "renato",
   "Ocupação cultural do feriado na Ilha do Governador: samba, capoeira, rap, poesia e danças urbanas em roda, com banda residente e o público dentro da cena.",
   'Quintal do Renatin Sexta-feira (20/11), às 18h. Grátis. Livre.', SMC,
   sessoes=D("20 18:00"), classif="Livre", **G)
ev("Poexistência: Consciência Negra", "Livros & Debates", "marques",
   "Sarau aberto em que cada pessoa pode ler textos seus ou de outros autores, com um poeta convidado. O tema de novembro é a Consciência Negra.",
   'Poexistência Quinta-feira (19/11), das 14h30 às 16h30. Grátis. 16 anos.', SMC,
   sessoes=D("19 14:30"), classif="16 anos", **G)
ev("Estante temática: cultura afro-brasileira", "Livros & Debates|Infantil", "marques",
   "Mostra de livros infantis e juvenis sobre cultura afro-brasileira.",
   'Estante Temática de Livros Segunda a sexta-feira, das 9h às 17h. Até 30/11. Grátis. Livre. Sábados das 9 às 13 horas. Grátis. Livre. Exposição de livros infantis e juvenis sobre cultura afro-brasileira.', SMC,
   cartaz=C(None, "2026-11-30", "Segunda a sexta, 9h–17h; sábados, 9h–13h"), classif="Livre", **G)
ev("Tem Jongo no Beco Novais", "Música|Cinema", "joaobosco",
   "O griot Celso Marinho e músicos da Serrinha fazem roda de jongo, com exibição do filme independente “Herdeiros”.",
   'Novembro Negro: Tem Jongo no Beco Novais Data e horário: 20/11, às 18h | Local: Areninha Cultural João Bosco | Classificação indicativa: Livre | Valor: Gratuito | Linguagem: Cinema e música | Acessibilidade: não haverá recurso de acessibilidade em 20/11', NN,
   sessoes=D("20 18:00"), classif="Livre", **G,
   nota="A fonte não dá o endereço da Areninha João Bosco. O bairro (Vista Alegre) vem do cadastro de fontes do projeto.")
ev("Encontro de Baluartes e Futuros Bambas", "Música|Festas & Feiras", "jovelina",
   "Capoeira, maculelê, música, curtas-metragens e homenagens a personalidades da cultura afro-brasileira, na Pavuna.",
   'Novembro Negro: Arena Cultural Jovelina Pérola Negra 1. Encontro de Baluartes e Futuros Bambas Data e horário: 20/11, a partir das 14h | Valor: Gratuita', NN,
   sessoes=D("20 14:00"), **G,
   nota="A fonte não dá o endereço da arena. Usei “Praça Ênio, s/nº, Pavuna”, encontrado numa página de terceiros (Buser), não em fonte oficial.")

# ---------------- ZONA OESTE ----------------
ev("Felipe Ferreira – Novo", "Teatro", "hermeto",
   "Stand-up do humorista da Pavuna, conhecido pelos vídeos nas redes.",
   'Show de Comédia Stand Up “Novo – Felipe Ferreira” Sábado (21/11), às 19h. R$ 35 a R$ 60. 16 anos.', SMC,
   sessoes=D("21 19:00"), preco="R$ 35 a R$ 60", pmin=35, pmax=60, classif="16 anos")
ev("Ônibus Biblioteca – Livros nas Praças", "Livros & Debates|Infantil", "hermeto",
   "Biblioteca sobre rodas com empréstimo gratuito de livros (com cadastro), leitura dramatizada, teatro literário e contação de histórias.",
   'Ônibus Biblioteca – Livros nas Praças Até 27 de novembro, às 11h. Grátis. Livre.', SMC,
   cartaz=C(None, "2026-11-27", "Às 11h (a fonte não informa os dias)"), classif="Livre", **G)
ev("KD O Show", "Teatro", "chacrinha",
   "Kwesny e Daniel Lopes fazem um show de humor que muda a cada noite, com a plateia ditando o rumo.",
   'Show de Comédia “KD O Show” Quinta-feira (19/11), às 20h. R$ 35. 14 anos.', SMC,
   sessoes=D("19 20:00"), preco="R$ 35", pmin=35, pmax=35, classif="14 anos")
ev("FIPAZO – Festival de Pole Dance, Aéreos e Danças da Zona Oeste", "Teatro", "chacrinha",
   "Terceira edição do festival não competitivo que reúne artistas de Pedra de Guaratiba e de outras regiões em números de pole dance, circo e dança.",
   'FIPAZO – Festival Internacional de Pole Dance, Aéreos e Danças da Zona Oeste Sábado e domingo (21 e 22/11), às 14h. R$ 30. 16 anos.', SMC,
   sessoes=D("21 14:00", "22 14:00"), preco="R$ 30", pmin=30, pmax=30, classif="16 anos")
ev("Alice no País das Maravilhas: O Despertar da União – O Musical", "Teatro", "chacrinha",
   "Entre o reino da Rainha Vermelha e o da Rainha Branca, Alice descobre que a maior batalha é saber quem ela é.",
   'Alice no País das Maravilhas: O Despertar da União – O Musical Terça-feira (24/11), às 18h. R$ 50. Livre.', SMC,
   sessoes=D("24 18:00"), preco="R$ 50", pmin=50, pmax=50, classif="Livre")
ev("Domingo recreativo para crianças", "Infantil", "sandra",
   "Jogos, brincadeiras e pintura conduzidos pela equipe da areninha, todo domingo.",
   'Domingo recreativo para crianças Domingos, às 10h. Grátis. Livre.', SMC,
   sessoes=D("22 10:00"), classif="Livre", **G)
ev("Celebração da Diversidade – Dia da Consciência Negra", "Festas & Feiras", "gil",
   "Evento da programação do Dia da Consciência Negra na areninha de Realengo. A fonte não detalha as atrações.",
   'Celebração da Diversidade em Homenagem ao Dia da Consciência Negra Sexta-feira (20/11) às 15h. R$ 20 ou 1 lata de leite em pó. Livre. || Novembro Negro: 1. Uma Celebração à Diversidade Data e horário: 20/11, às 15h | Valor: R$ 40,00 (inteira) / R$ 20,00 (meia), com alternativa de ingresso mediante doação de uma lata de leite em pó', SMC,
   sessoes=D("20 15:00"), preco="R$ 20 a R$ 40, ou 1 lata de leite em pó", pmin=20, pmax=40, classif="Livre",
   nota="As fontes não dizem o que acontece no evento. Preço: o PDF semanal diz “R$ 20 ou 1 lata de leite em pó”; o do Novembro Negro, “R$ 40 (inteira) / R$ 20 (meia)”.")
ev("No Ritmo do Circo", "Teatro", "gil",
   "Espetáculo de circo na areninha de Realengo. A fonte não traz mais detalhes.",
   'Espetáculo no Ritmo do Circo 21/11 - 19 horas - R$ 40,00 - Livre', SMC,
   sessoes=D("21 19:00"), preco="R$ 40", pmin=40, pmax=40, classif="Livre")
ev("Clube de Leitura Infantil – mês da Consciência Negra", "Infantil|Livros & Debates", "moacyr",
   "Leitura de livros infantis sobre a temática negra.",
   'Novembro Negro: Espaço de Leitura Moacyr Teixeira 1. Clube de Leitura Infantil – mês da Consciência Negra Data e horário: 13/11 e 17/11 a 19/11, às 15h | Classificação indicativa: Livre | Valor: Gratuito | Linguagem: Literatura', NN,
   sessoes=D("19 15:00"), classif="Livre", **G,
   nota="A fonte não dá o endereço. Usei o do regulamento das bibliotecas da SMC (“Espaço de Leitura Moacyr Teixeira, Rua 12, s/n, Santa Cruz”).")

# =========== PDF DO NOVEMBRO NEGRO: eventos de rua e de parceiros que não estão no PDF semanal ===========
ev("Amanhecer Rio – Festival Cultura e Cuidado", "Festas & Feiras|Música", "passeio",
   "Três manhãs no Passeio Público com shows, conversas, ioga e feira. Sexta tem Jonathan Ferr; sábado, Michael Sullivan; domingo, a Bateria da Portela e a roda Quintal da Magia. Idealizado por Marcus Faustini.",
   'Amanhecer Rio – Festival Cultura e Cuidado Data e horário: 20, 21 e 22/11, das 8h às 13h (portões abertos a partir das 7h) | Local: Passeio Público, Centro [...] | Classificação indicativa: Livre | Valor: Gratuito | [...] Acessibilidade: Libras em todas as palestras, oficinas e shows', NN,
   sessoes=D("20 08:00", "21 08:00", "22 08:00"), classif="Livre", acess="Libras em palestras, oficinas e shows", rua=True, **G)
ev("Rolé Estácio – Berço do Samba", "Festas & Feiras|Música", "estacio",
   "Caminhada guiada pelas ruas do Estácio, por lugares e memórias de Ismael Silva, Bide e da Deixa Falar. Termina na quadra da Estácio de Sá, com feijoada e música a partir das 13h (consumo à parte).",
   'Rolé Estácio – Berço do Samba Data e horário: 21/11, às 10h (roteiro guiado); feijoada e atrações musicais na quadra, a partir das 13h | Local: ponto de encontro na Praça do Estácio (saída B do metrô), com encerramento na quadra da G.R.E.S. Estácio de Sá | Classificação indicativa: Livre | Valor: Gratuito, sem necessidade de inscrição (feijoada e consumação à parte) | [...] Acessibilidade: intérpretes de Libras no roteiro guiado', NN,
   sessoes=D("21 10:00"), classif="Livre", acess="Intérpretes de Libras no roteiro guiado", rua=True, **G)
ev("40 Anos do Monumento a Zumbi", "Festas & Feiras", "zumbi",
   "Três dias de festa na Praça XI pelos 40 anos do monumento: shows, blocos afro, afoxés, escolas de samba, feira de negócios e gastronomia.",
   '40 Anos do Monumento à Zumbi – Elevando a Autoestima do Povo Afro Carioca Data e horário: 19, 20 e 21/11, das 6h às 23h | Local: Monumento à Zumbi, Praça XI, em frente ao Terreirão do Samba | Classificação indicativa: Livre | Valor: Gratuito', NN,
   sessoes=D("19 06:00", "20 06:00", "21 06:00"), classif="Livre", rua=True, **G)
ev("Mostra de Cenas e Performances (Mostra do Impossível)", "Teatro", "terreirocontemp",
   "Noite de cenas curtas e performances de artistas negros, em sequência, nos três espaços do Terreiro Contemporâneo. Encerra a 8ª Mostra do Impossível.",
   'Novembro Negro: 21/11 (sábado) [...] 19h – Mostra de Cenas e Performances – Movimento Aquecimento, com Nyl MC (Galeria Quilombo) [...] 21h – Mostra de Cenas e Performances – Casa de Laffond: A Experiência, com Casa de Laffond (Sala Rubens Barbot) [...] Local: Terreiro Contemporâneo – Teatro Chica Xavier, Galeria Quilombo e Sala Rubens Barbot (R. Carlos de Carvalho, 53, Centro)', NN,
   sessoes=D("21 19:00"), classif="Livre", link="https://confrariadoimpossivel.com/2026-mostra-do-impossivel/", **MOSTRA_PRECO,
   nota="Preço: a fonte diz “Majoritariamente gratuito; apenas uma sessão com ingressos a preços populares (R$ 10 a inteira e R$ 5 a meia)”, sem dizer qual.")
ev("OFÁ / Um Corpo Flecha, de Rona Neves (Mostra do Impossível)", "Artes Visuais", "terreirocontemp",
   "Exposição de Rona Neves na Galeria Quilombo, aberta durante os dias da Mostra do Impossível.",
   'Novembro Negro: 19/11 (quinta-feira) • Horário contínuo – Exposição OFÁ/Um Corpo Flecha, de Rona Neves (Galeria Quilombo)', NN,
   cartaz=C("2026-11-18", "2026-11-21", "Horário contínuo, nos dias da mostra"), link="https://confrariadoimpossivel.com/2026-mostra-do-impossivel/",
   nota="A exposição aparece na programação de 19, 20 e 21/11. Preço e horário de abertura não informados na fonte.")
ev("Cabaret – Edição Especial Consciência Negra", "Teatro", "crescer",
   "A 39ª edição do Cabaret – Absurdos & Variedades tem elenco inteiramente negro, com circo, dança, música e humor. Depois, DJs e pista.",
   'Novembro Negro: Circo Crescer e Viver 1. Cabaret – Edição Especial Consciência Negra Data e horário: 20/11/2026 (sexta-feira), às 20h | Local: Rua Carmo Neto, 143 | Valor: de R$ 10,00 a R$ 600,00, conforme setor e modalidade | Vendas: https://bileto.sympla.com.br/event/121801/d/390956', NN,
   sessoes=D("20 20:00"), preco="R$ 10 a R$ 600, conforme o setor", pmin=10, pmax=600,
   link="https://bileto.sympla.com.br/event/121801/d/390956",
   nota="A fonte não dá o bairro. “Cidade Nova” vem do cadastro de fontes do projeto. Classificação não informada.")
ev("Festival Terreiro 2026 – Dia da Consciência Negra", "Música|Festas & Feiras|Infantil", "juras",
   "Do começo da tarde à meia-noite na praça: samba, jongo e cultura popular, com Sombrinha, Jongo da Serrinha e o festival infantil Terreirinho. Do Terreiro de Crioulo.",
   'Novembro Negro: Terreiro de Crioulo 1. Festival Terreiro 2026 – Dia da Consciência Negra Data e horário: 20/11/2026 (sexta-feira), das 13h à 0h do dia 21/11 | Local: Praça das Juras, Padre Miguel (referência: Nave do Conhecimento de Padre Miguel) | Classificação indicativa: não informada [...] | Valor: Gratuita, com opção de ingressos colaborativos de R$ 5,00, R$ 10,00 ou R$ 20,00', NN,
   sessoes=D("20 13:00"), preco="Grátis (ingresso colaborativo opcional)", gratis=True, rua=True)


# =========== TRAZIDOS DA EDIÇÃO ANTERIOR (coleta de 15–17/11; não relidos nesta edição) ===========
ANT = {e["id"]: e for e in json.load(open(os.path.join(RAIZ, "dados", "edicoes", "2026-11-15", "eventos.json"), encoding="utf-8"))["eventos"]}
def trazer(num, nota):
    e = dict(ANT["2026-11-15-%03d" % num]); e.pop("id")
    e["sessoes"] = [s for s in e["sessoes"] if EDICAO["inicio"] <= s["data"] <= EDICAO["fim"]]
    e["nota_redacao"] = (nota + " " + (e.get("nota_redacao") or "")).strip()
    assert e["tipo"] == "cartaz" or e["sessoes"], num
    EV.append(e)
N_SITE = "Coletado no site em 15–17/11 e não relido nesta edição."
trazer(5, "Consta no PDF semanal anterior (“12 e 19/11”), mas não aparece no PDF desta semana, que lista só outros dois espetáculos no mesmo teatro. Pode ter sido cancelado ou apenas omitido.")
for n in (16, 17):
    trazer(n, "Consta no PDF semanal anterior, com data de encerramento em 2027; o PDF desta semana não repete a exposição.")
for n in (54, 55, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66):   # CCBB (56, Amazônicas, terminou em 16/11)
    trazer(n, N_SITE)
for n in (67, 68, 69):   # Circo Voador
    trazer(n, N_SITE)
for n in (70, 72, 73):   # Sesc Tijuca
    trazer(n, N_SITE)

# =========== ACRÉSCIMOS DE 19/11 (decisão editorial: atividades entre evento e oficina entram) ===========
# Ficam no fim da lista para não mudar a numeração das fichas já conferidas.
ev("Seminário Estadual: Por uma Educação Antirracista", "Livros & Debates", "muhcab",
   "Dia de debates sobre práticas de ensino comprometidas com a equidade racial e com a história e a cultura afro-brasileiras.",
   'Seminário Estadual: Por uma Educação Antirracista Terça-feira (24/11), das 10h às 15h. Grátis. Livre. || Novembro Negro: Data e horário: 24/11/2026, das 10h às 15h | Observação: evento sujeito a alterações', SMC,
   sessoes=D("24 10:00"), classif="Livre", **G,
   nota="O PDF do Novembro Negro avisa: “evento sujeito a alterações”. No PDF semanal está na seção de atividades formativas.")
ev("Aula-baile de forró e samba de gafieira – Corpos em Diálogo", "Festas & Feiras", "coreografico",
   "Baile que encerra as oficinas de forró e samba de gafieira para iniciantes, aberto a quem quiser dançar, com acompanhamento da professora Amanda Guimarães Moreira.",
   'Aula-Baile de “Forró e Samba de Gafieira – Corpos em Diálogo” Quarta-feira (25/11), das 19h às 20h. Grátis. 18 anos. [...] Aberta à comunidade', SMC,
   sessoes=D("25 19:00"), classif="18 anos", **G,
   nota="No PDF semanal está na seção de atividades formativas.")
ev("Café com Arte – Novembro Negro, com Pandro Nobã", "Artes Visuais|Livros & Debates", "casabonifacio",
   "Manhã de café, pintura e conversa com o artista urbano e arte-educador Pandro Nobã, da Penha, inspirada na ideia de casa como lugar de acolhimento, de bell hooks. É preciso se inscrever.",
   'Novembro Negro: Casa Bonifácio Rua do Senado, 47, Centro, Rio de Janeiro 1. Café com Arte – Novembro Negro, com Pandro Nobã Data e horário: 20/11, a partir das 10h | Local: Casa Bonifácio (divulgado também como Ateliê Bonifácio – Espaço Afro-Carioca) | Participação: inscrições abertas', NN,
   sessoes=D("20 10:00"), nota="A fonte não informa preço, classificação nem como se inscrever.")
ev("Dança, Identidade e Resistência – aulão do Ballet Manguinhos", "Festas & Feiras", "bpmanguinhos",
   "Aulão do Dia da Consciência Negra para conhecer e experimentar afoxé, maculelê e capoeira. As senhas são distribuídas no local meia hora antes.",
   'Novembro Negro: 2. Dança, Identidade e Resistência Data e horário: 20/11/2026 (sexta-feira), às 14h | Local: Biblioteca Parque de Manguinhos | Classificação indicativa: a partir de 16 anos | Valor: Gratuita, com retirada de senha no local 30 minutos antes da atividade', NN,
   sessoes=D("20 14:00"), preco="Grátis (senha no local, 30 min antes)", gratis=True, classif="16 anos",
   nota="A fonte não dá o endereço da Biblioteca Parque de Manguinhos.")


# =========== RONDA DAS FONTES DE 19/11 (coleta automática na nuvem + ronda no computador da coordenação) ===========
# Ficam no fim da lista para não mudar a numeração das fichas já conferidas.
# Só entra o que a fonte dá com dia, hora e lugar. O texto bruto fica no ramo coleta-bruta (nuvem) e no .zip da ronda do PC.
RONDA = "Ronda das fontes de 19/11"
def F(nome, link): return (nome + " (ronda de 19/11)", link)

# --- CCBB: relido na ronda. As datas da edição anterior conferem; Música no Museu ganhou o concerto de domingo.
for e in EV:
    if e["local"].startswith("Centro Cultural Banco do Brasil") and N_SITE in e["nota_redacao"]:
        e["nota_redacao"] = e["nota_redacao"].replace(N_SITE, "Coletado no site em 15–17/11 e relido na ronda de 19/11: datas conferem.")
        if e["titulo"] == "Música no Museu":
            e["sessoes"] = [{"data": "2026-11-22", "hora": "13:00"}, {"data": "2026-11-25", "hora": "12:30"}]
            e["trecho_fonte"] += " || Ronda de 19/11: 22/11, domingo 13h , Ernesto Leston, oboé, e Mariana Airaudo, piano (Uruguai). [...] 25/11, quarta 12h30 , William Wielgus, oboé, e Matthew Van Hoose, piano (EUA)."
            e["nota_redacao"] = "Coletado no site em 15–17/11 e relido na ronda de 19/11: o site agora dá horário (13h) para o concerto de domingo, 22/11, que entra."

L.update({
 "abl": ("Academia Brasileira de Letras (ABL)", "Av. Presidente Wilson, 203", "Centro (Castelo)", "Centro"),
 "cariocadagema": ("Carioca da Gema", "Av. Mem de Sá, 79", "Lapa", "Centro"),
 "salacecilia": ("Sala Cecília Meireles", "Largo da Lapa, 47", "Lapa", "Centro"),
 "tm": ("Theatro Municipal do Rio de Janeiro", "Praça Floriano, s/nº", "Centro (Cinelândia)", "Centro"),
 "tmassyrio": ("Theatro Municipal do Rio de Janeiro – Salão Assyrio", "Praça Floriano, s/nº", "Centro (Cinelândia)", "Centro"),
 "paco": ("Paço Imperial", "Praça XV de Novembro, 48", "Centro", "Centro"),
 "bpe": ("Biblioteca Parque Estadual", "Av. Presidente Vargas, 1.261", "Centro", "Centro"),
 "travcentro": ("Livraria da Travessa – Centro", "Rua Graça Aranha, 296", "Centro", "Centro"),
 "crm": ("Casa Roberto Marinho", "Rua Cosme Velho, 1.105", "Cosme Velho", "Zona Sul"),
 "mviegas": ("Galeria Mercedes Viegas", "Rua Abreu Fialho, 5, sobrado", "Jardim Botânico", "Zona Sul"),
 "futuros": ("Petrobras Futuros – Arte e Tecnologia", "Rua Dois de Dezembro, 63", "Flamengo", "Zona Sul"),
 "casafirjan": ("Casa Firjan", "Rua Guilhermina Guinle, 211", "Botafogo", "Zona Sul"),
 "evaklabin": ("Casa Museu Eva Klabin", "Av. Epitácio Pessoa, 2.480", "Lagoa", "Zona Sul"),
 "eav": ("EAV Parque Lage", "Rua Jardim Botânico, 414", "Jardim Botânico", "Zona Sul"),
 "ecovilla": ("EcoVilla Ri Happy", "Rua Jardim Botânico, 1.008", "Jardim Botânico", "Zona Sul"),
 "casagrande": ("Teatro Casa Grande (Teatro Axia Casa Grande)", "Av. Afrânio de Melo Franco, 290", "Leblon", "Zona Sul"),
 "poeira": ("Teatro Poeira", "Rua São João Batista, 104", "Botafogo", "Zona Sul"),
 "poeirinha": ("Teatro Poeirinha", "Rua São João Batista, 104", "Botafogo", "Zona Sul"),
 "vivorio": ("Vivo Rio", "Av. Infante Dom Henrique, 85", "Glória (Aterro do Flamengo)", "Zona Sul"),
 "travipanema": ("Livraria da Travessa – Ipanema", "Rua Visconde de Pirajá, 572", "Ipanema", "Zona Sul"),
 "travleblon": ("Livraria da Travessa – Shopping Leblon", "Av. Afrânio de Melo Franco, 290", "Leblon", "Zona Sul"),
 "travbotafogo": ("Livraria da Travessa – Botafogo", "Rua Voluntários da Pátria, 97", "Botafogo", "Zona Sul"),
 "travbarra": ("Livraria da Travessa – BarraShopping", "Av. das Américas, 4.666", "Barra da Tijuca", "Zona Sudoeste"),
 "pontal": ("Museu do Pontal", "Av. Célia Ribeiro da Silva Mendes, s/nº", "Barra da Tijuca", "Zona Sudoeste"),
 "qualistage": ("Qualistage", "Av. Ayrton Senna, 3.000 (Via Parque Shopping)", "Barra da Tijuca", "Zona Sudoeste"),
 "multiplan": ("Teatro Multiplan", "Av. das Américas, 3.900", "Barra da Tijuca", "Zona Sudoeste"),
 "eduerj": ("Livraria da EdUERJ (campus Maracanã da Uerj)", "Rua São Francisco Xavier, 524, térreo", "Maracanã", "Zona Norte"),
 "bangu": ("Teatro Bangu Shopping", "Rua da Fonseca, 240", "Bangu", "Zona Oeste"),
})
N_END = "O endereço não está no texto coletado; é o endereço público do espaço."
N_ABERT = "O horário é o que a página do bar dá para a noite; a mesma página avisa que o show principal pode começar mais tarde."

# ---------------- CENTRO ----------------
ABL = F("Site da ABL", "https://academia.org.br/eventos")
ev("A retórica de Júlia Lopes de Almeida – Quinta é Cultura", "Livros & Debates", "abl",
   "Encontro da série Quinta é Cultura dedicado à retórica de Júlia Lopes de Almeida, com coordenação do acadêmico Godofredo de Oliveira Neto. A inscrição é feita pelo site da Academia.",
   'Próximos eventos A retórica de Júlia Lopes de Almeida Quinta é Cultura Data e horário: 19 de Novembro de 2026 às 17h30 Coordenação: Acadêmico Godofredo de Oliveira Neto INSCREVA-SE CLICANDO AQUI', ABL,
   sessoes=D("19 17:30"), nota="A fonte não informa preço nem classificação.")
ev("A poesia brasileira na Coleção Ciranda da Poesia – ciclo de conferências", "Livros & Debates", "abl",
   "Conferência do ciclo sobre a poesia brasileira na Coleção Ciranda da Poesia, com coordenação do acadêmico Paulo Henriques Britto. A inscrição é feita pelo site da Academia.",
   '"A poesia brasileira na Coleção Ciranda da Poesia" ciclo de conferências Data e horário: 24 de Novembro de 2026 às 16h00 Coordenação: Acadêmico Paulo Henriques Britto INSCREVA-SE CLICANDO AQUI', ABL,
   sessoes=D("24 16:00"), nota="A fonte não informa preço nem classificação.")

CG = F("Site do Carioca da Gema", "https://www.barcariocadagema.com.br/shows")
CG_PRECO = ' || Valor entrada de terça ate quinta - R$ 30,00 sexta e sábado - R$ 35,00 véspera de feriado - R$35,00'
ev("Andrezão do Cacique", "Música", "cariocadagema",
   "Noite de samba em homenagem aos compositores que se reuniam em volta da tamarineira, como Arlindo Cruz, Sombrinha, Jorge Aragão, Zeca Pagodinho, Almir Guineto e Luiz Carlos da Vila, com sucessos do Fundo de Quintal.",
   'qui., 19 de nov. Andrezão do Cacique / 19 de nov. de 2026, 21:30 Carioca da Gema, Av. Mem de Sá, 79 - Centro, Rio de Janeiro - RJ' + CG_PRECO, CG,
   sessoes=D("19 21:30"), preco="R$ 35 (véspera de feriado)", pmin=35, pmax=35,
   nota="Quinta, 19/11, é véspera de feriado: vale o preço de véspera (R$ 35), não o de quinta (R$ 30). " + N_ABERT)
ev("Pedro Menezes", "Música", "cariocadagema",
   "Show de samba tradicional com toque contemporâneo, na Lapa.",
   'sex., 20 de nov. Pedro Menezes / 20 de nov. de 2026, 20:00 [...] Samba de verdade com raízes fortes no gênero [...] a essência do samba tradicional com toque contemporâneo' + CG_PRECO, CG,
   sessoes=D("20 20:00"), preco="R$ 35", pmin=35, pmax=35, nota=N_ABERT)
ev("Leonardo Bessa", "Música", "cariocadagema",
   "O cantor e compositor do Salgueiro passa por samba de raiz, pagode e sambas-enredo, com histórias entre as músicas.",
   'sáb., 21 de nov. Leonardo Bessa / 21 de nov. de 2026, 20:30 BRT [...] Cantor e compositor do Salgueiro, passeia pelo samba de raiz, pagode e grandes sambas-enredo, com histórias, bom humor e muita interação. || SÁBADOS-abertura 20:30/inicio show principal 22:00' + CG_PRECO, CG,
   sessoes=D("21 20:30"), preco="R$ 35", pmin=35, pmax=35,
   nota="20h30 é a abertura da casa; a página informa que, aos sábados, o show principal começa às 22h.")
ev("Três a Varejo + 1", "Música", "cariocadagema",
   "Show para dançar que vai do samba ao maxixe, ao ijexá, ao xote, ao baião e ao frevo.",
   'seg., 23 de nov. Três a Varejo / 23 de nov. de 2026, 19:30 [...] Três a Varejo + 1 celebra a brasilidade em um show que vai do samba ao maxixe, ijexá, xote, baião e frevo.', CG,
   sessoes=D("23 19:30"), nota="A página só dá o preço de terça a sábado; o de segunda-feira não é informado. " + N_ABERT)

ev("Guilherme Pozzi – Série Piano na Sala", "Música", "salacecilia",
   "Recital do pianista com obras de Schumann, Beethoven, Chopin e Prokofiev, da Arabeske à Sonata nº 7, passando pela “Appassionata” e pela Balada nº 4.",
   'Série Piano na Sala 2026-11-19 19:00:00 • qui, 19 nov • 19H00 Guilherme Pozzi Sala Cecília Meireles R$ 40 [...] recital que reúne obras de Robert Schumann, Ludwig van Beethoven, Frédéric Chopin e Sergei Prokofiev. O programa percorre [...] da Arabeske , de Schumann, à Sonata nº 7 , de Prokofiev, passando pela Sonata “Appassionata” , de Beethoven, e pela Balada nº 4 , de Chopin.',
   F("Site da Sala Cecília Meireles", "https://salaceciliameireles.rj.gov.br/programacao/guilherme-pozzi/"),
   sessoes=D("19 19:00"), preco="R$ 40", pmin=40, pmax=40, nota="A fonte não informa o valor da meia-entrada nem a classificação.")

ev("OSB Jovem – Legado em Harmonia", "Música", "tm",
   "A Orquestra Sinfônica Brasileira Jovem toca Bizet, Lebrun e Tchaikovsky, com regência de Anderson Alves e o oboísta Rodrigo Herculano como solista.",
   'OSB Jovem | Legado em Harmonia 19 de novembro (quinta-feira) – 19h Theatro Municipal do Rio de Janeiro Anderson Alves , regência Rodrigo Herculano , oboé [...] Ingressos: Plateia: R$60 (R$30 meia) | Frisa: R$50 (R$25 meia) | Camarote: R$40 (R$20 meia) | Galeria: R$30 (R$15 meia) || Site do Theatro Municipal: No dia 19 de novembro , a Orquestra Sinfônica Brasileira Jovem leva ao palco do Theatro Municipal do Rio de Janeiro o espetáculo Legado em Harmonia . [...] No repertório, obras de Georges Bizet , Ludwig August Lebrun e Piotr Ilitch Tchaikovsky .',
   F("Sites da OSB e do Theatro Municipal", "https://www.osb.com.br/osb-jovem/"),
   sessoes=D("19 19:00"), preco="R$ 30 a R$ 60 (meia de R$ 15 a R$ 30)", pmin=15, pmax=60)
ev("Coral Brasil Ensemble – UFRJ (Música no Assyrio)", "Música", "tmassyrio",
   "O coral da UFRJ, voltado à música brasileira contemporânea, canta com André Santos e Claudia Feitosa ao piano, sob regência de Maria José Chevitarese.",
   'TMRJ recebe o Coral Brasil Ensemble – UFRJ – Dia 22/11, às 11h | A série Música no Assyrio recebe, no dia 22 de novembro, às 11 horas, o Coral Brasil Ensemble – UFRJ, com André Santos e Claudia Feitosa no piano, sob regência e direção artística de Maria José Chevitarese. [...] tem como propósito principal promover a música brasileira contemporânea. [...] Os ingressos estão disponíveis através do site theatromunicipal.rj.gov.br ou na Bilheteria do Theatro.',
   F("Site do Theatro Municipal", "https://theatromunicipal.rj.gov.br/tmrj-recebe-o-coral-brasil-ensemble-ufrj-dia-22-11-as-11h/"),
   sessoes=D("22 11:00"), nota="O trecho coletado não traz o preço do ingresso.")

ev("Claudia Hersz: Mostra sua cara", "Artes Visuais", "paco",
   "Cerca de 140 obras feitas entre 2018 e 2026, entre objetos, instalações e vídeos, em que a artista rasga, cola e remonta mapas, capas de disco e outras imagens conhecidas do Brasil. Curadoria de Fernanda Lopes. Últimos dias.",
   'Mostra sua cara reúne cerca de 140 obras, a maioria inéditas, produzidas entre 2018 e 2026, incluindo objetos, instalações e vídeos. Com curadoria de Fernanda Lopes [...] Local : Paço Imperial — Praça XV de Novembro, 48, Centro, Rio de Janeiro – RJ Visitação : 26 de setembro a 22 de novembro de 2026 Horário : Terça a domingo e feriados, das 12h às 18h Entrada gratuita',
   F("Site da galeria Portas Vilaseca", "https://portasvilaseca.com.br/pt"),
   cartaz=C("2026-09-26", "2026-11-22", "Terça a domingo e feriados, 12h–18h"), **G)
ev("O gesto do poder, o poder do gesto – um recorte da Coleção Instituto PIPA", "Artes Visuais", "paco",
   "Recorte da Coleção Instituto PIPA sobre as relações entre arte, autoridade e memória, com curadoria de Lucrécia Vinhaes. Entre as obras está a pintura “Rio Setecentista” (2013), de Arjan Martins. Últimos dias.",
   'Arjan Martins | O gesto do poder, o poder do gesto Centro Cultural do Patrimônio Paço Imperial | Rio de Janeiro, Brasil 26 Setembro - 22 Novembro 2026 Curadoria: Lucrécia Vinhaes Expografia: Carla Marins Em “O gesto do poder, o poder do gesto - um recorte da Coleção Instituto PIPA”, a relação estrutural entre arte, autoridade e memória é o eixo central. [...] Arjan Martins apresenta a pintura “Rio Setecentista” (2013).',
   F("Site da galeria A Gentil Carioca", "https://www.agentilcarioca.com.br/exhibitions/"),
   cartaz=C("2026-09-26", "2026-11-22", "Terça a domingo e feriados, 12h–18h"),
   nota="A fonte desta mostra não dá horário nem preço. O horário é o do Paço Imperial informado na ficha de “Claudia Hersz: Mostra sua cara”.")

ev("Casa da Mônica", "Infantil|Artes Visuais", "bpe",
   "Exposição interativa com cenários do Bairro do Limoeiro, como a casa da Mônica, a cozinha da Magali e o estúdio de Mauricio de Sousa. Os ingressos gratuitos são liberados toda segunda-feira, às 10h, pela internet.",
   'Serviço: Exposição Casa da Mônica Período: 28 de outubro a 22 de dezembro Dias de visitação: segunda a sexta-feira (exceto feriados), das 10h às 17h Retirada de ingressos: toda segunda-feira, às 10h, através da plataforma Sympla || Gratuita, a exposição fica disponível para visitação de segunda-feira a sexta-feira até o dia 22 de dezembro',
   F("Site da Secretaria de Estado de Cultura", "https://cultura.rj.gov.br/biblioteca-parque-estadual-inaugura-exposicao-inspirada-no-universo-da-turma-da-monica/"),
   cartaz=C("2026-10-28", "2026-12-22", "Segunda a sexta, 10h–17h (fecha nos feriados)"),
   preco="Grátis (ingresso pela internet, liberado às segundas, 10h)", gratis=True,
   nota="Fecha no feriado de 20/11. " + N_END)

TRAV = F("Site da Livraria da Travessa", "https://www.travessa.com.br/eventos")
N_TRAV = "A fonte não informa preço. " + N_END
ev("Lançamento: Migrantes da Descolonização", "Livros & Debates", "travcentro",
   "Isabel de Souza Lima Junqueira Barreto autografa o livro sobre portugueses e luso-angolanos que vieram para o Brasil entre 1974 e 1977, depois da guerra em Angola.",
   '23/11 . SEGUNDA Centro - Graça Aranha - RJ | 17:00 MIGRANTES DA DESCOLONIZAÇÃO: PORTUGUESES E LUSO-ANGOLANOS NO BRASIL (1974-1977) Autor(a): Isabel de Souza Lima Junqueira Barreto AUTÓGRAFOS Após uma longa guerra (1961-1974), Angola tornou-se independente em 11 de novembro de 1975', TRAV,
   sessoes=D("23 17:00"), nota="A fonte não informa preço.")

# ---------------- ZONA SUL ----------------
ev("Guardar – Coleção Marcia e Luiz Chrysostomo", "Artes Visuais", "crm",
   "Abre nesta quinta a mostra com cerca de 300 obras de uma coleção particular, das vanguardas do início do século XX à produção contemporânea, com curadoria de Paulo Venancio Filho.",
   'Exposição Guardar Coleção Marcia e Luiz Chrysostomo 19 Nov a 14 Mar De terça-feira a domingo das 12h às 18h *Entrada até 17h15 [...] R. Cosme Velho, 1105 || ArtRio: Com curadoria de Paulo Venancio Filho, a mostra apresenta cerca de 300 obras e percorre diferentes momentos da arte brasileira e internacional, das vanguardas do início do século XX à produção contemporânea. [...] Abertura pública: 19 de novembro de 2026, às 12h Encerramento: 14 de março de 2027 De terça a domingo, das 12h às 18h Ingressos à venda exclusivamente na bilheteria: R$ 10 (inteira) / R$ 5 (meia entrada)',
   F("Sites da Casa Roberto Marinho e da ArtRio", "https://casarobertomarinho.org.br"),
   cartaz=C("2026-11-19", "2027-03-14", "Terça a domingo, 12h–18h (entrada até 17h15)"),
   preco="R$ 10 (meia R$ 5), só na bilheteria", pmin=5, pmax=10)
ev("ECOS – coletiva", "Artes Visuais", "mviegas",
   "Coletiva com obras de Antonio Bokel, Hildebranda, Nathan Braga, Omar Salomão, Regina de Paula e Tetê Sá: 19 trabalhos, entre pinturas, esculturas e um vídeo.",
   'ECOS | antonio bokel + hildebranda + nathan braga + omar salomão + regina de paula + tetê sá | 14.11.26 > 23.01.27 abertura: 14.11.26 exposição : 17.11.26 – 23.01.27 horários: de segunda a sexta: 12h - 19h; sábados: 15h30 - 19h30 || ArtRio: Mostra reúne 19 obras, entre pinturas, esculturas e um vídeo sob curadoria de Amanda Mujica [...] Galeria Mercedes Viegas | Rua Abreu Fialho 5, sobrado – Jardim Botânico [...] Até 23 de janeiro de 2027 De terça a sexta, das 12h às 19h. Sábados, das 15h30 e 19h30. Entrada gratuita',
   F("Sites da galeria Mercedes Viegas e da ArtRio", "https://www.mercedesviegas.com.br/exposicoes/ecos"),
   cartaz=C("2026-11-17", "2027-01-23", "Segunda a sexta, 12h–19h; sábado, 15h30–19h30"), **G,
   nota="As fontes divergem num ponto: o site da galeria diz “segunda a sexta”; a ArtRio diz “terça a sexta”. Vale o site da galeria.")
ev("Escrevendo com a Luz – Zumví Arquivo Afro Fotográfico", "Artes Visuais", "futuros",
   "Fotografias do arquivo baiano Zumví que registram corpos, territórios e manifestações culturais da população negra, numa ponte entre Salvador e o Rio. Curadoria de Lázaro Roberto e Luedji Luna.",
   'SERVIÇO Exposição “Escrevendo com a Luz” | Zumví Arquivo Afro Fotográfico Data: 29 de outubro a 20 de dezembro de 2026 Horário: quarta a domingo, das 11h às 20h Local: Petrobras Futuros - Arte e Tecnologia - Galeria 2 Endereço: Rua Dois de Dezembro, 63, Flamengo, Rio de Janeiro - RJ Entrada franca || Com curadoria de Lázaro Roberto e Luedji Luna, mostra fotográfica estabelece uma ponte entre Salvador e Rio de Janeiro [...] Fotografias que registram corpos, territórios, manifestações culturais e diferentes experiências da população negra',
   F("Site do Petrobras Futuros", "https://petrobrasfuturos.com.br/programacao/exposicao-escrevendo-com-a-luz-zumvi/"),
   cartaz=C("2026-10-29", "2026-12-20", "Quarta a domingo, 11h–20h"), **G)

CF = F("Site da Casa Firjan", "https://casafirjan.com.br/")
ev("Cartografia de Futuros Imaginários – Casa Aberta", "Artes Visuais|Infantil", "casafirjan",
   "Atividade de uma hora para criar zines com palavras, imagens e recortes.",
   '21 de novembro de 2026 Sábado Horário: 16h00 | Duração: 1h Cartografia de Futuros Imaginários | Atividade Casa Aberta Crie zines com palavras, imagens e recortes, transforme ideias em narrativas e explore diferentes caminhos para o amanhã.', CF,
   sessoes=D("21 16:00"), nota="A fonte não informa preço, classificação nem se é preciso se inscrever.")
ev("Meninas e Mulheres na Ciência e Tecnologia: redes que abrem caminhos", "Livros & Debates", "casafirjan",
   "Encontro de quatro horas para aproximar iniciativas que fortalecem a participação feminina na ciência e na tecnologia.",
   '24 de novembro de 2026 Terça Horário: 14h00 | Duração: 4h Meninas e Mulheres na Ciência e Tecnologia: redes que abrem caminhos | Aquário Edu Casa Firjan Conecte iniciativas e fortaleça a participação feminina na ciência e na tecnologia', CF,
   sessoes=D("24 14:00"), nota="A fonte não informa preço nem se é preciso se inscrever.")

ev("Oficina Cliques e Movimento", "Infantil", "evaklabin",
   "Crianças a partir de 3 anos criam cenas e histórias em stop motion, com celular, corpo e tecidos. As senhas são distribuídas dez minutos antes.",
   'A oficina de práticas artísticas [...] Chamada de "Cliques e Movimentos", se baseia no uso do "Stop Motion Studio", corpos e tecidos [...] voltada para crianças a partir de 3 anos de idade. [...] As oficinas são gratuitas e a participação ocorre mediante a retirada de senhas, dez minutos antes da atividade. Essa atividade estará aberta ao público nos dias 15, 21, 22 e 29 de novembro, sempre às 15h.',
   F("Site da Casa Museu Eva Klabin", "https://www.evaklabin.org.br/pt"),
   sessoes=D("21 15:00", "22 15:00"), preco="Grátis (senha 10 minutos antes)", gratis=True)

ev("Encontro dos Povos Originários", "Artes Visuais|Festas & Feiras", "eav",
   "Três dias de programação reunida por artistas indígenas na Escola de Artes Visuais. A grade de atividades está no site da escola.",
   'ENCONTRO DOS POVOS ORIGINÁRIOS Artistas indígenas reúnem mais uma grande programação na EAV Parque Lage. 20 NOV 2026 SEX - 10h 22 NOV 2026 DOM - 17h',
   F("Site da EAV Parque Lage", "https://eavparquelage.rj.gov.br/acontece"),
   cartaz=C("2026-11-20", "2026-11-22", "De sexta, 10h, a domingo, 17h (ver a grade no site)"),
   nota="A coleta só trouxe o período e a chamada do evento, sem a grade de atividades nem o preço.")

ECO = F("Site da EcoVilla Ri Happy", "https://ecovillarihappy.com.br/programacao/")
N_ECO = "A fonte não informa o preço."
ev("Confissões de Adolescente – o musical", "Teatro", "ecovilla",
   "Versão musical inédita da história sobre as dores e as descobertas de crescer.",
   'Confissões de Adolescente 23 de outubro a 29 de novembro | Sextas às 20h, Sábados e Domingos às 19h Classificação: 16 anos FENÔMENO QUE MARCOU GERAÇÕES, ‘CONFISSÕES DE ADOLESOCENTE’ RETORNA AOS PALCOS EM VERSÃO MUSICAL INÉDITA.', ECO,
   sessoes=D("20 20:00", "21 19:00", "22 19:00"), classif="16 anos", nota=N_ECO)
ev("Escola do Rock", "Teatro|Infantil", "ecovilla",
   "Musical baseado no filme de 2003: um guitarrista se passa por professor substituto e monta uma banda com alunos do quinto ano para disputar a Batalha das Bandas.",
   'Escola do Rock - CEFTEM 14 de novembro a 13 de dezembro | Sábados e Domingos, às 15h e dia 04 e 11 de dezembro | Sexta-feiras às 19h30 Classificação: Livre Baseado no filme School of Rock, de 2003 [...] ao fingir ser um professor substituto em uma prestigiosa e conservadora escola, Dewey forma um grupo do quinto ano, na tentativa de ganhar o próximo concurso: a Batalha das Bandas.', ECO,
   sessoes=D("21 15:00", "22 15:00"), classif="Livre", nota=N_ECO)
ev("Sábado Musical com Batuca Jardim – Ritmos da Ancestralidade", "Infantil|Música", "ecovilla",
   "Manhã de percussão, canto e brincadeiras em família sobre ritmos e tradições afro-brasileiras, em homenagem ao Dia da Consciência Negra.",
   'Sábado Musical, com Batuca Jardim - Ritmos da Ancestralidade” 21 de novembro | Sábado às 09h30 [...] Em homenagem ao Dia da Consciência Negra, o Batuca Jardim convida crianças e famílias para uma experiência musical [...] Por meio da percussão, do canto e de atividades lúdicas e coletivas', ECO,
   sessoes=D("21 09:30"), nota=N_ECO)
ev("Oficina Da Imaginação à Selva: uma aventura pela floresta de Mogli", "Infantil", "ecovilla",
   "Duas horas de atividades para crianças em torno da mata, dos bichos e das histórias da floresta de Mogli, dentro da Temporada da Consciência Negra.",
   'Oficina Da Imaginação à Selva: Uma Aventura pela Floresta de Mogli (Gratuito) 21 de novembro | Sábado, das 10h30 às 12h30 [...] Como parte da Temporada da Consciência Negra, a EcoVilla Ri Happy convidará as crianças a embarcar na oficina gratuita Da Imaginação à Selva, uma aventura inspirada na floresta de Mogli. Em duas horas de atividades lúdicas e criativas', ECO,
   sessoes=D("21 10:30"), **G)
ev("Clube Akorin: Musicalizar Brincando", "Infantil|Música", "ecovilla",
   "O músico e ator Alan Rocha encerra a turnê do projeto com canções autorais, cultura popular e brincadeiras com a plateia, em torno das matrizes da cultura afro-brasileira.",
   'Clube Akorin 22 de novembro | Domingo, às 11h [...] O músico e ator Alan Rocha subirá ao palco do Teatro EcoVilla Ri Happy com Clube Akorin: Musicalizar Brincando, show que encerrará a turnê oficial do projeto e unirá música autoral e cultura popular [...] canções e histórias que celebrarão as matrizes da cultura afro-brasileira.', ECO,
   sessoes=D("22 11:00"), nota=N_ECO)

TCG = "https://www.teatroaxiacasagrande.com.br/programacao/"
N_TCG = "A coleta trouxe datas e horários, mas não a sinopse nem o preço."
ev("O Nome do Bebê", "Teatro", "casagrande",
   "Peça em curtíssima temporada no Leblon, às quintas e sextas, até 27 de novembro.",
   'CURTÍSSIMA TEMPORADA O Nome do Bebê 05 de Novembro a 27 de Novembro [...] Data: De 5 a 27 de novembro de 2026 Horário: Quintas e sextas às 20h00 Abertura da casa: 1h antes', F("Site do Teatro Casa Grande", TCG + "detalhes/o-nome-do-bebe/"),
   sessoes=D("19 20:00", "20 20:00"), nota=N_TCG)
ev("O Mercador de Veneza", "Teatro", "casagrande",
   "Peça em curta temporada no Leblon, aos sábados e domingos, até 29 de novembro.",
   'CURTA TEMPORADA O Mercador de Veneza 07 de Novembro a 29 de Novembro [...] Data: 7 a 29 de novembro de 2026 Horário: Sábado às 21h00 e Domingo às 19h00 Abertura da casa: 1 hora antes do evento', F("Site do Teatro Casa Grande", TCG),
   sessoes=D("21 21:00", "22 19:00"), nota=N_TCG)
ev("Atom Pink Floyd – Pink Floyd Symphonic", "Música", "casagrande",
   "A banda de tributo ao Pink Floyd festeja dez anos tocando o repertório com uma orquestra de câmara ao vivo. Apresentação única.",
   'ÚNICA APRESENTAÇÃO ATOM PINK FLOYD SYMPHONIC [...] um espetáculo que marca uma década de trajetória [...] Uma orquestra em formação camerística dialoga com os músicos em tempo real [...] SERVIÇO Data: 25/11/2026 Horário: 20h00 Local: Teatro Axia Casa Grande Endereço: Avenida Afrânio de Melo Franco, 290 – Loja A- Leblon – Rio de Janeiro/RJ Abertura da casa: 01h00 antes',
   F("Site do Teatro Casa Grande", TCG + "detalhes/2895/"),
   sessoes=D("25 20:00"), nota="A coleta não trouxe o preço.")

POE = F("Site do Teatro Poeira", "https://www.teatropoeira.com.br/")
ev("Margaridas", "Teatro", "poeira",
   "Com texto de Cecília Ripoll e direção de Natasha Corbelino, a peça percorre 200 anos de educação, de 1916 a um futuro imaginado em 2116.",
   'Margaridas — Teatro Poeira TEATRO POEIRA 03 NOV a 16 DEZ TER e QUA 20h ingressos Com texto de Cecília Ripoll e direção de Natasha Corbelino, a montagem faz um passeio por temas presentes em 200 anos de educação, de 1916 a um futuro imaginado em 2116', POE,
   sessoes=D("24 20:00", "25 20:00"), nota="A coleta não trouxe o preço.")
ev("Adorável Face de Andronieva Petrosa", "Teatro", "poeirinha",
   "Primeiro solo de Fabianna de Mello e Souza, em 40 anos de carreira: uma atriz recebe uma carta anônima que a acusa de plágio e passa a se perguntar o que é original. Dramaturgia de Cecilia Ripoll e direção de Denise Stutz.",
   'Adoravel Face TEATRO POEIRINHA 29 OUT a 20 DEZ QUI a SAB 20h e DOM 19h [...] Após 40 anos de carreira, Fabianna de Mello e Souza atua em seu primeiro solo, que transforma uma acusação de plágio em reflexão [...] ‘Adorável Face de Andronieva Petrosa’, solo de Fabianna de Mello e Souza, com dramaturgia de Cecilia Ripoll e direção de Denise Stutz, fará uma temporada no Teatro Poeirinha, de 29 de outubro a 20 de dezembro, com sessões de quinta à sábado, às 20h e domingos [...] Em cena, uma atriz recebe uma carta anônima acusando-a de plágio. [...] o que é original?', POE,
   sessoes=D("19 20:00", "20 20:00", "21 20:00", "22 19:00"), nota="A coleta não trouxe o preço.")

ev("CA7RIEL & Paco Amoroso – Free Spirits World Tour", "Música", "vivorio",
   "A dupla argentina, que mistura trap, rock e pop, traz ao Rio a turnê do álbum “Free Spirits”. O show foi remarcado para esta data.",
   'Gênero Internacional Data e Horário do Evento Nova Data Quinta, 19 de Novembro às 21h Ingressos CA7RIEL & Paco Amoroso Após o lançamento do novo álbum FREE SPIRITS, CA7RIEL & Paco Amoroso anunciam a FREE SPIRITS World Tour [...] mistura de trap, rock, pop [...] artistas mais magnéticos surgidos na Argentina neste século. [...] Av. Infante Dom Henrique, 85',
   F("Site do Vivo Rio", "https://vivorio.com.br/eventos/ca7riel-paco-amoroso/"),
   sessoes=D("19 21:00"), nota="A coleta não trouxe o preço nem a classificação.")

ev("Lançamento infantil: João Rapidão e Maria Devagarinha", "Infantil|Livros & Debates", "travipanema",
   "Wania Pinto autografa o livro sobre duas crianças de ritmos completamente diferentes.",
   '22/11 . DOMINGO Ipanema | 16:00 JOÃO RAPIDÃO E MARIA DEVAGARINHA Autor(a): Wania Pinto AUTÓGRAFOS João e Maria têm ritmos completamente diferentes. Ele é tão rápido que não quer parar nem ...', TRAV,
   sessoes=D("22 16:00"), nota=N_TRAV)
ev("Lançamento: Ministério do Tempo Livre – um manifesto", "Livros & Debates", "travleblon",
   "Miguel Lago autografa o livro e conversa com Laura Carvalho.",
   '23/11 . SEGUNDA Shopping Leblon | 19:00 MINISTÉRIO DO TEMPO LIVRE: UM MANIFESTO Autor(a): Miguel Lago AUTÓGRAFOS + BATE-PAPO COM AUTOR E LAURA CARVALHO', TRAV,
   sessoes=D("23 19:00"), nota=N_TRAV)
ev("Lançamento: Música em Pauta", "Livros & Debates|Música", "travipanema",
   "Mariana Camargo lança o livro que reúne textos inéditos e textos saídos na coluna de mesmo nome.",
   '23/11 . SEGUNDA Ipanema | 19:00 MUSICA EM PAUTA Autor(a): Mariana Camargo LANÇAMENTO “Música em Pauta” reúne textos inéditos e textos publicados originalmente na coluna homônima, escrita por Mariana ...', TRAV,
   sessoes=D("23 19:00"), nota=N_TRAV)
ev("Lançamento duplo: A Vida Imprópria e O Arquivo como Gesto", "Livros & Debates", "travbotafogo",
   "Noite de lançamento dos livros de Florencia Garramuño e de Mario Cámara.",
   '24/11 . TERÇA Botafogo | 19:00 A VIDA IMPRÓPRIA Autor(a): Florencia Garramuno O ARQUIVO COMO GESTO Autor(a): , Mario Camara', TRAV,
   sessoes=D("24 19:00"), nota=N_TRAV)
ev("Encontro literário Lia Benchimol: Wabi Sabi", "Livros & Debates", "travleblon",
   "Encontro de leitura mediado por Lia Benchimol sobre “Wabi Sabi: a sabedoria japonesa de apreciar o imperfeito”, de Nobuo Suzuki.",
   '25/11 . QUARTA Shopping Leblon | 16:00 WABI SABI: A SABEDORIA JAPONESA DE APRECIAR O IMPERFEITO Autor(a): Nobuo Suzuki ENCONTRO LITERÁRIO LIA BENCHIMOL MEDIAÇÃO: LIA BENCHIMOL', TRAV,
   sessoes=D("25 16:00"), nota=N_TRAV)
ev("Lançamento: Mistérios sob o Céu de Alcântara", "Livros & Debates", "travbotafogo",
   "Alexandre Maia Lago autografa o livro.",
   '25/11 . QUARTA Botafogo | 19:00 MISTÉRIOS SOB O CÉU DE ALCÂNTARA Autor(a): Alexandre Maia Lago AUTÓGRAFOS', TRAV,
   sessoes=D("25 19:00"), nota=N_TRAV)

# ---------------- ZONA SUDOESTE ----------------
PONTAL_G = dict(preco="Grátis (contribuição sugerida de R$ 20)", gratis=True)
PONTAL_T = ' || A entrada no Museu do Pontal é gratuita para todos . Entretanto, sugerimos uma contribuição mínima de R$ 20 àqueles que puderem apoiar as atividades do Museu.'
ev("Danças populares de Moçambique, com Bela Zango", "Festas & Feiras|Música", "pontal",
   "A cantora e bailarina moçambicana apresenta a música e as danças tradicionais do seu país. Ela é uma das poucas mulheres a dominar a timbila, xilofone do povo Chopi.",
   'Danças populares de Moçambique – 21 de novembro, 16h | Neste sábado, 21 de novembro, a cantora e bailarina moçambicana Bela Zango conduz uma atividade que apresenta ao público elementos da música e da dança tradicional de Moçambique. A atividade acontece às 16h. [...] É também uma das poucas mulheres a dominar a Timbila, xilofone tradicional do povo Chopi' + PONTAL_T,
   F("Site do Museu do Pontal", "https://museudopontal.org.br/programacao/dancas-populares-mocambique-21nov/"),
   sessoes=D("21 16:00"), **PONTAL_G)
ev("Oficina de Batik Experimental, com Val Pires", "Artes Visuais|Infantil", "pontal",
   "A artista e arte-educadora ensina a estampar tecido com carimbos de espuma, numa introdução ao batik africano.",
   'Oficina de Batik Experimental – 22 de novembro, 16h | Neste domingo, 22 de novembro , a artista visual, arte-educadora e xilógrafa Val Pires comanda a oficina de Batik Experimental, que apresenta uma técnica artesanal de tingimento e criação de estampas manuais. A atividade tem classificação livre e começa às 16h. A oficina propõe uma introdução ao Batik Africano, técnica de estamparia que utiliza carimbos de espuma.' + PONTAL_T,
   F("Site do Museu do Pontal", "https://museudopontal.org.br/programacao/oficina-batik-experimental-22-nov/"),
   sessoes=D("22 16:00"), classif="Livre", **PONTAL_G)

N_QS = "O site só dá o preço inicial. " + N_END
ev("Marcelo Falcão – turnê O Legado", "Música", "qualistage",
   "Cerca de três horas de show e mais de 40 músicas, num passeio por 30 anos de carreira entre rap, reggae e rock.",
   'Marcelo Falcão anuncia nova data da turnê “O Legado” no Rio de Janeiro [...] retorna à capital fluminense no dia 20 de novembro, no Qualistage. [...] São cerca de três horas de espetáculo com um setlist que ultrapassa mais de 40 faixas. [...] mais de 30 anos de carreira [...] rap, reggae, rock || A partir de R$ 87,50 Sexta - 20 | NOVEMBRO 22h30 16 anos',
   F("Site do Qualistage", "https://qualistage.com.br/evento/439/marcelo-falcao"),
   sessoes=D("20 22:30"), preco="A partir de R$ 87,50", pmin=87.5, classif="16 anos", nota=N_QS)
ev("Dino Fonseca – Barzim de Rock", "Música", "qualistage",
   "Mais de três horas de sucessos do rock nacional e internacional.",
   'O Barzim de Rock é uma turnê [...] Com mais de 3 horas de apresentação de Dino Fonseca, que conduz uma verdadeira viagem pelos maiores sucessos do rock nacional e internacional || A partir de R$ 85,00 Sábado - 21 | NOVEMBRO 21h30 18 anos',
   F("Site do Qualistage", "https://qualistage.com.br/evento/437/dino-fonseca"),
   sessoes=D("21 21:30"), preco="A partir de R$ 85", pmin=85, classif="18 anos", nota=N_QS)
ev("O Grande Encontro – Leci Brandão, Sandro Luiz, Tião Casemiro e Luan Pureza", "Música", "qualistage",
   "Tarde que junta o samba de Leci Brandão a três gerações da música de umbanda: o mestre Tião Casemiro, Sandro Luiz e Luan Pureza.",
   'No dia 22 de novembro de 2026 [...] O Qualistage [...] recebe “O Grande Encontro”, reunindo diferentes gerações e grandes referências da música ligada à cultura afrobrasileira e à Umbanda: Leci Brandão, Sandro Luiz, Tião Casemiro e Luan Pureza. || A partir de R$ 60,00 Domingo - 22 | NOVEMBRO 16h00 18 anos',
   F("Site do Qualistage", "https://qualistage.com.br/evento/436/sandro-luiz"),
   sessoes=D("22 16:00"), preco="A partir de R$ 60", pmin=60, classif="18 anos", nota=N_QS)

MULT = "https://teatromultiplan.com.br/"
ev("Bluey – Diversão em Família", "Infantil|Teatro", "multiplan",
   "Show oficial da série de animação, numa adaptação para o palco feita para a América Latina. Último fim de semana.",
   'Bluey - Diversão em Família 07 a 22 de novembro Sexta, Sábado e Domingo às 11h, Sábado e Domingo às 15h, Sábado às 18h [...] O espetáculo faz únicas apresentações de 7 a 22 de novembro, no Teatro Multiplan. [...] adaptação teatral original desenvolvida especialmente para a América Latina. [...] Duração 60 min Classificação etária Livre Ingressos a partir de a partir de R$ 25',
   F("Site do Teatro Multiplan", MULT + "eventos/bluey-2026/"),
   sessoes=D("20 11:00", "21 11:00", "21 15:00", "21 18:00", "22 11:00", "22 15:00"), preco="A partir de R$ 25", pmin=25, classif="Livre",
   nota="O site só dá o preço inicial.")
ev("Camila Cardoso – Antes e Depois do Plantão", "Teatro", "multiplan",
   "Apresentação de stand-up, com 90 minutos.",
   'Camila Cardoso com Ante e Depois do Plantão 23 de novembro Segunda às 20h30 [...] CAMILA CARDOSO – ANTES E DEPOIS DO PLANTÃO [...] Duração 90 min Classificação etária 14 Ingressos a partir de a partir de R$55',
   F("Site do Teatro Multiplan", MULT + "eventos/camila-cardoso-2026/"),
   sessoes=D("23 20:30"), preco="A partir de R$ 55", pmin=55, classif="14 anos", nota="O site só dá o preço inicial.")
ev("Maurício Meirelles – Surto Coletivo", "Teatro", "multiplan",
   "Apresentação de stand-up, com 90 minutos.",
   'Maurício Meirelles com Surto Coletivo 25 de novembro Quarta às 20h [...] SURTO COLETIVO | MAURÍCIO MEIRELLES | TEMPORADA 2026 [...] Duração 90 min Classificação etária 14 Ingressos a partir de a partir de R$ 60',
   F("Site do Teatro Multiplan", MULT + "eventos/mauricio-meirelles-2026/"),
   sessoes=D("25 20:00"), preco="A partir de R$ 60", pmin=60, classif="14 anos", nota="O site só dá o preço inicial.")

ev("O Clube Romance: Quando, de Carla Madeira", "Livros & Debates", "travbarra",
   "Encontro do clube de leitura sobre o romance de Carla Madeira, com mediação de Gabriela Campany.",
   '21/11 . SÁBADO BarraShopping | 13:30 QUANDO Autor(a): Carla Madeira O CLUBE ROMANCE MEDIAÇÃO GABRIELA CAMPANY', TRAV,
   sessoes=D("21 13:30"), nota=N_TRAV)
ev("Clube do Livro Trill: As Vacas Não Me Olham Mais na Cara, de Dora Freind", "Livros & Debates", "travbarra",
   "Encontro do clube de leitura sobre o livro de Dora Freind, com mediação de Rooh.",
   '22/11 . DOMINGO BarraShopping | 13:00 AS VACAS NÃO ME OLHAM MAIS NA CARA Autor(a): Dora Freind CLUBE DO LIVRO TRILL MEDIAÇÃO: ROOH', TRAV,
   sessoes=D("22 13:00"), nota=N_TRAV)

# ---------------- ZONA NORTE ----------------
ev("Debate de lançamento: As Três Mulheres do Alencar", "Livros & Debates", "eduerj",
   "Gustavo Bernardo debate o seu livro “As três mulheres do Alencar: sementes do fascismo na literatura brasileira”, que sai pela editora da universidade.",
   'Debate de lançamento do livro “As três mulheres do Alencar: sementes do fascismo na literatura brasileira” | A Editora da Universidade do Estado do Rio de Janeiro (EdUERJ) promove um debate com o autor Gustavo Bernardo no lançamento do seu livro “As três mulheres do Alencar: sementes do fascismo na literatura brasileira” no dia 19 de novembro, às 17h, na livraria da EdUERJ, localizada no térreo do campus Maracanã. || R. São Francisco Xavier, 524, Térreo, Bloco F – Sala T031',
   F("Agenda do site da Uerj", "https://www.uerj.br/agenda/debate-de-lancamento-do-livro-as-tres-mulheres-do-alencar-sementes-do-fascismo-na-literatura-brasileira/"),
   sessoes=D("19 17:00"), nota="Lido na ronda feita no computador da coordenação editorial (a nuvem não conseguiu abrir o site). A fonte não informa preço.")

# ---------------- ZONA OESTE ----------------
ev("Muato – DERÊ: Concerto sobre o Pagode", "Música", "bangu",
   "Sozinho no palco, com voz, violão de oito cordas, guitarra, pedais de loop e samples, o artista revisita o pagode nascido no subúrbio carioca nos anos 90, entre música, manifesto e poesia.",
   'Muato - Concerto Sobre o Pagode [...] sáb, 21 de novembro de 2026 20h00 Em “DERÊ - CONCERTO SOBRE O PAGODE”, o premiado artista Muato, apresenta um show que flutua entre a música, o manifesto e a poesia. O artista se expressa através de sua voz, violão de 8 cordas, guitarra, pedais de loop, samples [...] repertório baseado no Pagode, gênero que nasceu no subúrbio carioca nos anos 90. [...] 21/11/2026 Livre || Rua da Fonseca, 240 – Espaço 174 – Bangu – Rio de Janeiro – RJ',
   F("Site do Teatro Bangu Shopping", "https://teatrobangushopping.com.br/evento/muato-concerto-sobre-o-pagode"),
   sessoes=D("21 20:00"), classif="Livre", nota="A coleta não trouxe o preço.")


# =========== CORREÇÕES DEPOIS DO CONFERENTE (ronda de 19/11) ===========
def achar(t):
    c = [e for e in EV if e["titulo"].startswith(t)]; assert len(c) == 1, t; return c[0]
e = achar("OSB Jovem")
e.update(preco_texto="", preco_min=None, preco_max=None, nota_redacao="As fontes não trazem o preço deste concerto.")
e["trecho_fonte"] = 'OSB Jovem | Legado em Harmonia 19 de novembro (quinta-feira) – 19h Theatro Municipal do Rio de Janeiro Anderson Alves , regência Rodrigo Herculano , oboé || Site do Theatro Municipal: No dia 19 de novembro , a Orquestra Sinfônica Brasileira Jovem leva ao palco do Theatro Municipal do Rio de Janeiro o espetáculo Legado em Harmonia . [...] No repertório, obras de Georges Bizet , Ludwig August Lebrun e Piotr Ilitch Tchaikovsky .'
e = achar("CA7RIEL")
e.update(preco_texto="R$ 490 (meia R$ 245)", preco_min=245, preco_max=490, classificacao="18 anos", nota_redacao="")
e["trecho_fonte"] += " || INGRESSOS A PARTIR DE: R$ 245 (meia) R$ 490 (inteira) [...] Classificação Etária 18"
e = achar("Cartografia de Futuros")
e.update(areas=["Artes Visuais"], sessoes=[{"data": "2026-11-21", "hora": "16:00"}, {"data": "2026-11-22", "hora": "16:00"}],
         preco_texto="Grátis (sujeito a lotação)", gratis=True, classificacao="12 anos", nota_redacao="")
e["trecho_fonte"] += " || 22 de novembro de 2026 Domingo Horário: 16h00 | Duração: 1h Cartografia de Futuros Imaginários | Atividade Casa Aberta || Sábados e domingos Horário: 16h [...] Atividade gratuita, sujeito a lotação [...] Classificação: 12 anos"
e = achar("Meninas e Mulheres")
e["nota_redacao"] = "A fonte não informa preço. A página de atividades da casa tem um botão de inscrição que parece ser deste encontro, mas não repete o título nem a data."
e = achar("Guardar")
e.update(preco_texto="R$ 10 (meia R$ 5), só na bilheteria; grátis às quartas")
e["trecho_fonte"] += " || Às quartas-feiras, a entrada é franca para todos os públicos."
e = achar("O Nome do Bebê")
e.update(classificacao="12 anos", nota_redacao="A coleta não trouxe o preço.",
         sinopse="Comédia da dupla francesa Matthieu Delaporte e Alexandre de la Patellière, com Bianca Bin no elenco e direção de Elias Andreato. Curtíssima temporada, até 27 de novembro.")
e["trecho_fonte"] += " || a comédia O Nome do Bebê, com Bianca Bin e grande elenco [...] da dupla francesa Matthieu Delaporte e Alexandre de la Patellière [...] A direção é de Elias Andreato [...] Classificação etária: 12 anos."
e = achar("O Mercador de Veneza")
e.update(classificacao="14 anos", nota_redacao="A coleta não trouxe o preço.",
         sinopse="A peça de William Shakespeare, com direção de Daniela Stirbulov e Dan Stulbach no papel do agiota Shylock. Dura duas horas. Curta temporada, até 29 de novembro.")
e["trecho_fonte"] += " || O Mercador de Veneza, do dramaturgo inglês William Shakespeare [...] A peça tem direção de Daniela Stirbulov e é protagonizada por Dan Stulbach que dá vida ao marcante agiota Shylock [...] Duração: 120 minutos [...] Classificação etária: 14 anos."
e = achar("Atom Pink Floyd"); e["classificacao"] = "16 anos"; e["trecho_fonte"] += " || Classificação etária: 16 anos."
e = achar("Margaridas"); e["classificacao"] = "10 anos"; e["trecho_fonte"] += " || CLASSIFICAÇÃO ETÁRIA: 10 anos"
e = achar("Adorável Face"); e["classificacao"] = "Livre"; e["trecho_fonte"] += " || CLASSIFICAÇÃO: Livre"
for t in ("Sábado Musical com Batuca", "Oficina Da Imaginação", "Clube Akorin"):
    e = achar(t); e["classificacao"] = "Livre"; e["trecho_fonte"] += " || Classificação: Livre"
e = achar("Oficina Cliques e Movimento")
e.update(classificacao="Livre", nota_redacao="A fonte dá dois endereços para a casa: “Avenida Epitácio Pessoa, 2480”, no rodapé do site, e “Praça Benedito Cerqueira, 0 | Lagoa”, no serviço da oficina. Fica o do rodapé, que é o endereço fixo da instituição.")
e["trecho_fonte"] += " || Entrada gratuita Classificação livre"
e = achar("ECOS")
e["sinopse"] = "Coletiva com obras de Antonio Bokel, Hildebranda, Nathan Braga, Omar Salomão, Regina de Paula e Tetê Sá: cerca de vinte trabalhos, entre pinturas, esculturas, serigrafias e vídeos."
e["trecho_fonte"] += " || Site da galeria: Reunindo vinte trabalhos, entre pinturas, esculturas, serigrafias e vídeos"
e["nota_redacao"] += " Também divergem no número de obras (vinte no site da galeria, dezenove na ArtRio); vale o site da galeria."
e = achar("Debate de lançamento: As Três Mulheres")
e["endereco"] = "Rua São Francisco Xavier, 524 (campus Maracanã), térreo"
e["trecho_fonte"] = e["trecho_fonte"].split(" || R. São Francisco")[0]
e["nota_redacao"] += " Sobre o lugar, a fonte só diz “na livraria da EdUERJ, localizada no térreo do campus Maracanã”; o número 524 é o endereço do campus, que aparece em outras páginas do mesmo site."
e = achar("O Grande Encontro")
e["sinopse"] = "Tarde que junta o samba de Leci Brandão a diferentes gerações da música de umbanda: o mestre Tião Casemiro, Sandro Luiz e Luan Pureza."
e = achar("Casa da Mônica"); e["nota_redacao"] = "Fecha no feriado de 20/11."
e["trecho_fonte"] += " || Biblioteca Parque Estadual Av. Pres. Vargas, 1261 – Centro, Rio de Janeiro – RJ"

# =========== PROGRAMAÇÃO RECEBIDA DIRETAMENTE (19/11): ensaios de rua das escolas de samba ===========
# Post enviado pela coordenação editorial, sem data de publicação, com a agenda semanal dos ensaios das
# escolas do Grupo Especial. Dias da semana viram datas da edição. Ficam de fora, por estarem fora do
# município: União de Maricá (Maricá), Beija-Flor (Nilópolis), Viradouro (Niterói) e Grande Rio (Duque de Caxias).
L.update({
 "tuiuti": ("Campo de São Cristóvão (em frente ao Colégio Pedro II)", "Campo de São Cristóvão", "São Cristóvão", "Centro"),
 "boulevard28": ("Boulevard 28 de Setembro", "Boulevard 28 de Setembro", "Vila Isabel", "Zona Norte"),
 "viad1": ("Via D1 (Rua Geógrafo Milton Santos)", "Rua Geógrafo Milton Santos", "Santo Cristo", "Centro"),
 "maxwell": ("Rua Maxwell", "Rua Maxwell, 581", "Andaraí", "Zona Norte"),
 "aryfranco": ("Avenida Ministro Ary Franco", "Avenida Ministro Ary Franco", "Padre Miguel", "Zona Oeste"),
 "euclidesfaria": ("Rua Euclides Faria", "Rua Euclides Faria", "Ramos", "Zona Norte"),
 "viscniteroi": ("Rua Visconde de Niterói", "Rua Visconde de Niterói", "Mangueira", "Centro"),
 "claranunes": ("Rua Clara Nunes, esquina com Estrada do Portela", "Rua Clara Nunes, esquina com Estrada do Portela", "Madureira", "Zona Norte"),
})
POST = ("Agenda dos ensaios de rua do Grupo Especial (programação recebida pela coordenação editorial)", "")
NOTA_ENSAIO = ("Fonte: agenda semanal dos ensaios divulgada em post e enviada à coordenação editorial em 19/11, sem data de publicação; "
               "o horário é o de início ou de concentração. Sexta, 20/11, é feriado.")
for titulo, local, dia_hora, trecho, sinopse in [
    ("Ensaio de rua do Paraíso do Tuiuti", "tuiuti", "23 19:00",
     "SEGUNDA-FEIRA: • Paraíso do Tuiuti • São Cristóvão (Campo de São Cristóvão, em frente ao Pedro II), a partir das 19h.",
     "O Paraíso do Tuiuti ensaia no Campo de São Cristóvão, preparando o Carnaval 2027. Entrada gratuita."),
    ("Ensaio de rua da Unidos de Vila Isabel", "boulevard28", "25 20:00",
     "QUARTA-FEIRA: • Unidos de Vila Isabel • Vila Isabel (Boulevard 28 de Setembro), a partir das 20h.",
     "A Vila Isabel leva o ensaio para o Boulevard 28 de Setembro, preparando o Carnaval 2027."),
    ("Ensaio de rua da Unidos da Tijuca", "viad1", "19 19:00",
     "QUINTA-FEIRA: • Unidos da Tijuca • Santo Cristo (Via D1 / Rua Geógrafo Milton Santos), a partir das 19h.",
     "A Unidos da Tijuca ensaia na Via D1, em Santo Cristo, preparando o Carnaval 2027."),
    ("Ensaio de rua do Acadêmicos do Salgueiro", "maxwell", "19 20:00",
     "QUINTA-FEIRA: • Acadêmicos do Salgueiro • Andaraí (Rua Maxwell, 581), a partir das 20h.",
     "O Salgueiro ensaia na Rua Maxwell, no Andaraí, preparando o Carnaval 2027."),
    ("Ensaio de rua da Mocidade Independente", "aryfranco", "21 18:00",
     "SÁBADO: • Mocidade Independente • Padre Miguel / Bangu (Av. Ministro Ary Franco), concentração às 18h.",
     "A Mocidade de Padre Miguel ensaia na Avenida Ministro Ary Franco, preparando o Carnaval 2027."),
    ("Ensaio de rua da Imperatriz Leopoldinense", "euclidesfaria", "22 16:00",
     "DOMINGO: • Imperatriz Leopoldinense • Ramos (Rua Euclides Faria), a partir das 16h.",
     "A Imperatriz ensaia na Rua Euclides Faria, em Ramos, preparando o Carnaval 2027."),
    ("Ensaio de rua da Estação Primeira de Mangueira", "viscniteroi", "22 17:00",
     "DOMINGO: • Estação Primeira de Mangueira • Mangueira (Rua Visconde de Niterói), a partir das 17h.",
     "A Mangueira ensaia na Rua Visconde de Niterói, preparando o Carnaval 2027."),
    ("Ensaio de rua da Portela", "claranunes", "22 18:00",
     "DOMINGO: • Portela • Madureira (Esquina da Rua Clara Nunes com Estrada do Portela), a partir das 18h.",
     "A Portela ensaia em Madureira, na esquina da Rua Clara Nunes com a Estrada do Portela, preparando o Carnaval 2027."),
]:
    ev(titulo, "Festas & Feiras|Música", local, sinopse,
       "A temporada de preparação para o Carnaval 2027 já começou e as escolas do Grupo Especial do Rio estão tomando as ruas com entrada gratuita [...] " + trecho,
       POST, sessoes=D(dia_hora), rua=True, nota=NOTA_ENSAIO, **G)


for i, e in enumerate(EV, 1):
    e["id"] = f"2026-11-19-{i:03d}"
pasta = os.path.join(RAIZ, "dados", "edicoes", EDICAO["id"])
os.makedirs(pasta, exist_ok=True)
json.dump({"edicao": EDICAO, "eventos": EV}, open(os.path.join(pasta, "eventos.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print(len(EV), "eventos")
