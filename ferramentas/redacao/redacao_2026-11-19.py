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

for i, e in enumerate(EV, 1):
    e["id"] = f"2026-11-19-{i:03d}"
pasta = os.path.join(RAIZ, "dados", "edicoes", EDICAO["id"])
os.makedirs(pasta, exist_ok=True)
json.dump({"edicao": EDICAO, "eventos": EV}, open(os.path.join(pasta, "eventos.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print(len(EV), "eventos")
