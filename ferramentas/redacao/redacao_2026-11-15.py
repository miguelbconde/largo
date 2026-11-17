# Repórter A — fichas da edição de teste (15 a 25/11/2026)
# Cada evento guarda o trecho exato da fonte usado para preencher datas, horários e preços.
import json, os

EDICAO = {"id": "2026-11-15", "inicio": "2026-11-15", "fim": "2026-11-25",
          "titulo": "Edição de teste · 15 a 25 de novembro de 2026"}

SMC = ("Programação Semanal da Cultura Rio 12–18/11 (PDF SMC)",
       "https://cultura.prefeitura.rio/agendacultural/")
CCBB = ("Site CCBB Rio", "https://ccbb.com.br/rio-de-janeiro/programacao/")
CIRCO = ("API pública do Circo Voador", "https://www.circovoador.com.br/")
SESC = ("Site Sesc RJ +cultura", "https://cultura.sescrio.org.br/")

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
 "dicro": ("Arena Carioca Dicró", "Rua Flora Lobo, Parque Ary Barroso, s/nº", "Penha Circular", "Zona Norte"),
 "fernandotorres": ("Arena Cultural Fernando Torres", "Rua Bernardino de Andrade, 200 (Parque de Madureira)", "Madureira", "Zona Norte"),
 "terra": ("Areninha Cultural Terra", "Rua Marcos de Macedo, s/nº", "Guadalupe", "Zona Norte"),
 "zefiro": ("Areninha Cultural Carlos Zéfiro", "Estrada Marechal Alencastro, s/nº", "Anchieta", "Zona Norte"),
 "jorgeamado": ("Biblioteca Municipal Jorge Amado (Areninha Herbert Vianna)", "Rua Ivanildo Alves, s/nº", "Maré", "Zona Norte"),
 "marques": ("Biblioteca Municipal Marques Rebelo", "Rua Guapeni, 61", "Tijuca", "Zona Norte"),
 "sesctijuca": ("Sesc Tijuca", "Rua Barão de Mesquita, 539", "Tijuca", "Zona Norte"),
 "hermeto": ("Areninha Cultural Hermeto Pascoal", "Praça Primeiro de Maio, s/nº", "Bangu", "Zona Oeste"),
 "sandra": ("Areninha Cultural Sandra de Sá", "Rua Doze, 1", "Santa Cruz", "Zona Oeste"),
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

# ---------------- PDF SMC (válido para 12–18/11; datas além de 18/11 só quando a fonte diz "até") ----------------
ev("Equina", "Teatro", "sergioporto",
   "Espetáculo de dança de Aline Bernardi e Dani Lima sobre os laços de cuidado entre humanos e cavalos, a partir da pesquisa de doutorado de Aline.",
   'Espetáculo "Equina" sábados 19h e domingos 18h. Até 29/11. R$ 30 a R$ 60. 18 anos.', SMC,
   sessoes=["2026-11-15 18:00", "2026-11-21 19:00", "2026-11-22 18:00"], preco="R$ 30 a R$ 60", pmin=30, pmax=60,
   classif="18 anos", acess="Sala Preta, 2º andar, acesso apenas por escadas")
ev("O Extermínio da Cegonha", "Teatro", "sergioporto",
   "Um feriado de Finados em família vira acerto de contas quando um amigo de infância reaparece; a tecnologia funciona como gatilho trágico.",
   'Sexta-feiras e sábados, às 20h, e domingo, às 19h. Até 15/11. R$ 30 a R$ 60. 14 anos.', SMC,
   sessoes=["2026-11-15 19:00"], preco="R$ 30 a R$ 60", pmin=30, pmax=60, classif="14 anos")
ev("O Último Dia da Minha Vida", "Teatro", "cafepequeno",
   "Numa noite decisiva, um homem abre o baú de memórias que tentou esquecer. Drama com humor ácido.",
   'Terças e quartas-feiras, às 20h. De 17 a 25/11, R$ 10 a R$20. 14 anos.', SMC,
   sessoes=["2026-11-17 20:00", "2026-11-18 20:00", "2026-11-24 20:00", "2026-11-25 20:00"],
   preco="R$ 10 a R$ 20", pmin=10, pmax=20, classif="14 anos")
ev("Nada sob Controle", "Teatro|Infantil", "cafepequeno",
   "Comédia circense do Circo Teatro Saltimbanco, com palhaços, desencontros e improviso na tradição do circo brasileiro.",
   '"Nada sob Controle" 13 a 22 de novembro Sextas e Sábados às 20h e Domingos às 19h R$ 15 | R$ 30. 14 anos. Nada Sob Controle é um espetáculo de comédia circense do Circo Teatro Saltimbanco', SMC,
   sessoes=["2026-11-15 19:00", "2026-11-20 20:00", "2026-11-21 20:00", "2026-11-22 19:00"],
   preco="R$ 15 a R$ 30", pmin=15, pmax=30, classif="14 anos",
   nota="Local inferido pela posição no PDF (bloco do Teatro Café Pequeno).")
ev("WD – Eclipse Tour", "Música", "domingos",
   "Show que mistura canto, dança e imagens inspiradas no sol, na lua e no eclipse.",
   'Show"WD - Eclipse Tour" Quintas-feiras, (12 e 19/11), às 20h. R$ 60 a R$ 30. Livre', SMC,
   sessoes=["2026-11-19 20:00"], preco="R$ 30 a R$ 60", pmin=30, pmax=60, classif="Livre")
ev("Superiores", "Teatro", "domingos",
   "Nove atores criam toda a sonoplastia com o corpo e a voz, numa língua inventada, numa fábula sobre poder e opressão.",
   'Espetáculo "Superiores" Sextas e sábados, 20h, domingos, 19h. Até 29/11. R$ 30 a R$ 60. Livre.', SMC,
   sessoes=["2026-11-15 19:00", "2026-11-20 20:00", "2026-11-21 20:00", "2026-11-22 19:00"],
   preco="R$ 30 a R$ 60", pmin=30, pmax=60, classif="Livre")
ev("O Salto – 20 Anos", "Infantil|Teatro", "werneck",
   "O palhaço Migué Bruguelo promete três saltos de olhos vendados — e até lá tudo pode acontecer.",
   'Espetáculo "O Salto – 20 Anos" Domingo (15/11), às 15h. Grátis. Livre.', SMC,
   sessoes=["2026-11-15 15:00"], preco="Grátis", gratis=True, classif="Livre", rua=True)
ev("Exposição principal do Museu Histórico da Cidade", "Artes Visuais", "mhc",
   "Acervo permanente sobre a história do Rio, na antiga chácara da Gávea.",
   'Exposição Principal do Museu Histórico da Cidade Terça-feira a domingo, das 9h às 16h. Grátis. Livre.', SMC,
   cartaz=C(None, None, "Terça a domingo, 9h–16h"), preco="Grátis", gratis=True, classif="Livre")
ev("Pai – Pretos no Branco, de Diogo Brozoski", "Artes Visuais", "memorial",
   "Ilustrações e pinturas em que o artista, pai branco de duas crianças negras, reflete sobre paternidade e questões afrodiaspóricas.",
   '"Pai – Pretos no Branco", de Diogo Brozoski Quarta-feira a domingo, das 10h às 17h. Até 06/12 . Grátis. Livre', SMC,
   cartaz=C(None, "2026-12-06", "Quarta a domingo, 10h–17h"), preco="Grátis", gratis=True, classif="Livre")
ev("CORPO: onde a memória e os processos se inscrevem", "Artes Visuais", "memorial",
   "Coletiva com 67 artistas de várias regiões do país sobre o corpo como arquivo vivo.",
   'Exposição "CORPO: onde a memória e os processos se inscrevem" Quarta-feira a domingo, das 10h às 17h. Até 06/12 . Grátis. Livre', SMC,
   cartaz=C(None, "2026-12-06", "Quarta a domingo, 10h–17h"), preco="Grátis", gratis=True, classif="Livre")
ev("Uma vida à beira-mar sob o olhar do arquiteto, de Gisele Nossar", "Artes Visuais", "memorial",
   "Bordados que traduzem em linha as curvas da arquitetura carioca e os croquis de Niemeyer e Le Corbusier.",
   'Exposição "Uma vida à beira-mar sob o olhar do arquiteto", de Gisele Nossar Quarta-feira a domingo, das 10h às 17h. Até 06/12 . Grátis. Livre', SMC,
   cartaz=C(None, "2026-12-06", "Quarta a domingo, 10h–17h"), preco="Grátis", gratis=True, classif="Livre")
ev("Moraes Musical Moreira", "Música|Teatro", "carlosgomes",
   "Musical inspirado no cordel que percorre a vida e a obra de Moraes Moreira.",
   'Espetáculo "Moraes Musical Moreira" Quintas e sextas-feiras, às 19h, sábados, às 17h e às 20h, e domingos, às 17h. R$ 40 a R$ 80. 12 anos.', SMC,
   sessoes=["2026-11-15 17:00"], preco="R$ 40 a R$ 80", pmin=40, pmax=80, classif="12 anos",
   nota="Fonte sem data final; incluídas só as sessões até 18/11 (validade do PDF).")
ev("Zuzuê Contos Africanos", "Infantil|Teatro", "ruth",
   "Narração de histórias afro-diaspóricas, com Libras integrada à cena. Cerca de 50 minutos.",
   'Espetáculo "Zuzuê Contos Africanos" Sábado e domingo, às 11h. Até 29/11. R$ 20 a R$ 40. Livre.', SMC,
   sessoes=["2026-11-15 11:00", "2026-11-21 11:00", "2026-11-22 11:00"], preco="R$ 20 a R$ 40", pmin=20, pmax=40,
   classif="Livre", acess="Libras integrada à cena")
ev("Cia Banto – 20 Anos em Movimento", "Música|Teatro", "ruth",
   "Primeiro grupo de jongo da Zona Oeste celebra 20 anos com jongo, samba de roda e ijexá.",
   'Cia Banto - 20 Anos em Movimento Domingo 15 de novembro às 17h classificação Livre - Acessibilidade - Intérprete de Libras ... Ingressos Gratuitos com retirada no dia na bilheteria do teatro.', SMC,
   sessoes=["2026-11-15 17:00"], preco="Grátis (retirada no dia, na bilheteria)", gratis=True, classif="Livre",
   acess="Intérprete de Libras")
ev("Carnaval: Memória para o Amanhã", "Livros & Debates", "amanha",
   "Roda de conversa sobre o carnaval como guardião da memória de povos e territórios pouco representados.",
   'Carnaval: Memória para o Amanhã Segunda-feira (16/11), , às 14h30. Grátis. Livre.', SMC,
   sessoes=["2026-11-16 14:30"], preco="Grátis", gratis=True, classif="Livre")
ev("País Brasa, Planeta Fogo", "Artes Visuais", "amanha",
   "Exposição imersiva que trata o fogo como tecnologia, linguagem e força política.",
   'Exposição "País Brasa, Planeta Fogo" Quinta a terça-feira, das 10h às 18h (última entrada às 17h). Até 03/08/2027. R$ 20 a R$ 40. Livre.', SMC,
   cartaz=C(None, "2027-08-03", "Quinta a terça, 10h–18h (última entrada 17h)"), preco="R$ 20 a R$ 40", pmin=20, pmax=40, classif="Livre")
ev("A Cidade entre o Jardim e a Baía", "Artes Visuais", "amanha",
   "Instalação ao ar livre sobre a relação do Rio com a natureza, o espaço público e a Baía de Guanabara.",
   'Exposição "A Cidade entre o Jardim e a Baía" Quinta a terça-feira, das 10h às 18h (última entrada às 17h). Até 21/09/27. R$ 20 a R$ 40. Livre.', SMC,
   cartaz=C(None, "2027-09-21", "Quinta a terça, 10h–18h"), preco="R$ 20 a R$ 40", pmin=20, pmax=40, classif="Livre")
ev("Lançamento: Vivências Pedagógicas – Terreiros e Escolas na Luta Antirracista", "Livros & Debates", "muhcab",
   "Livro organizado por Gisele Rose sobre o encontro entre escola e saberes de terreiro no combate ao racismo.",
   'Lançamento do livro Vivências Pedagógicas: Terreiros e Escolas na Luta Antirracista Domingo (15/11), das 9h às 12h. Grátis. Livre.', SMC,
   sessoes=["2026-11-15 09:00"], preco="Grátis", gratis=True, classif="Livre")
ev("Pagode da Gigi", "Música", "muhcab",
   "Tradicional roda de samba que celebra a cultura negra e os laços comunitários.",
   'Pagode da Gigi Domingo (15/11), das 12h às 22h. R$ 15 a R$ 25. Livre.', SMC,
   sessoes=["2026-11-15 12:00"], preco="R$ 15 a R$ 25", pmin=15, pmax=25, classif="Livre")
ev("Protagonismos: Memória, Orgulho e Identidade", "Artes Visuais", "muhcab",
   "Exposição do Muhcab sobre memória e identidade.",
   'Exposição "Protagonismos: Memória, Orgulho e Identidade" Terça-feira a domingo, das 10h às 17h. Grátis. Livre.', SMC,
   cartaz=C(None, None, "Terça a domingo, 10h–17h"), preco="Grátis", gratis=True, classif="Livre")
ev("Zanele Muholi", "Artes Visuais", "mar",
   "Fotografias do(a) ativista visual sul-africano(a) que documenta a vida de pessoas negras LGBTI na África do Sul.",
   'Exposição "Zanele Muholi" Quinta a terça-feira, das 11h às 18h (última entrada às 17h). Até 29/11. R$ 10 a R$ 20 (terças-feiras são gratuitas). Livre.', SMC,
   cartaz=C(None, "2026-11-29", "Quinta a terça, 11h–18h · grátis às terças"), preco="R$ 10 a R$ 20 (grátis às terças)", pmin=10, pmax=20, classif="Livre")
ev("Tião – Um fotógrafo da Providência", "Artes Visuais", "mar",
   "O acervo de Sebastião Pires, o Tião, fotógrafo vizinho do museu, morador do Morro da Providência.",
   'Exposição "Tião-Um fotógrafo da Providência" Quinta a terça-feira, das 11h às 18h (última entrada às 17h). Até 29/11 R$ 10 a R$ 20 (terças-feiras são gratuitas). Livre.', SMC,
   cartaz=C(None, "2026-11-29", "Quinta a terça, 11h–18h · grátis às terças"), preco="R$ 10 a R$ 20 (grátis às terças)", pmin=10, pmax=20, classif="Livre")
ev("Ponto de Leitura: Brasilidades que vêm de Áfricas", "Livros & Debates", "mar",
   "Livros, imagens e sons sobre contribuições africanas à cultura brasileira, do pretuguês de Lélia Gonzalez às cozinhas diaspóricas.",
   'Ponto de Leitura - Brasilidades que vêm de Áfricas Quinta a terça-feira, das 11h às 17h. Até 30/11. R$ 10 a R$ 20 (terças-feiras são gratuitas). Livre.', SMC,
   cartaz=C(None, "2026-11-30", "Quinta a terça, 11h–17h"), preco="R$ 10 a R$ 20 (grátis às terças)", pmin=10, pmax=20, classif="Livre")
ev("Programa Hélio Oiticica", "Artes Visuais", "helio",
   "Exposição dedicada à obra de Hélio Oiticica no centro que leva seu nome.",
   'Exposição "Programa Hélio Oiticica" Segunda-feira a sábado, das 10h às 18h. Grátis. Livre.', SMC,
   cartaz=C(None, None, "Segunda a sábado, 10h–18h"), preco="Grátis", gratis=True, classif="Livre")
ev("MULTIARTE 2026", "Artes Visuais", "calouste",
   "Mostra anual das oficinas do Coletivo Calouste: pintura, gravura, cerâmica, mosaico, estamparia e mais.",
   'MULTIARTE 2026 – Exposição Anual das Oficinas do Coletivo Calouste Segunda à sábado, das 09h às 20h45. Até 19/12. Grátis. Livre.', SMC,
   cartaz=C(None, "2026-12-19", "Segunda a sábado, 9h–20h45"), preco="Grátis", gratis=True, classif="Livre")
ev("Maquete da Biblioteca dos Saberes", "Artes Visuais", "annita",
   "Modelo da futura biblioteca projetada por Francis Kéré para a Praça Onze, legado do Rio Capital Mundial do Livro.",
   'Exposição da Maquete da Biblioteca dos Saberes Segunda a sexta-feira, das 9h às 17h. Grátis. Livre.', SMC,
   cartaz=C(None, None, "Segunda a sexta, 9h–17h"), preco="Grátis", gratis=True, classif="Livre")
ev("Dominguinho – João Gomes, Jota.pê e Mestrinho", "Música", "cidadeartes",
   "Segunda etapa da turnê que reúne os três artistas numa grande roda de forró.",
   'Show "Turnê Dominguinho com João Gomes, Jota.pê e Mestrinho" Sábado e domingo, (14 e 15/11), às 15h. R$ 180 a R$ 360. 18 anos.', SMC,
   sessoes=["2026-11-15 15:00"], preco="R$ 180 a R$ 360", pmin=180, pmax=360, classif="18 anos")
ev("Canta o Brasil | Corais", "Música", "cidadeartes",
   "Todos os corais do projeto do maestro Luiz Lima reunidos numa só apresentação.",
   'Concerto "Canta o Brasil | Corais" Domingo, (15/11) às 16h. R$ 40 a R$ 80. Livre.', SMC,
   sessoes=["2026-11-15 16:00"], preco="R$ 40 a R$ 80", pmin=40, pmax=80, classif="Livre")
ev("Maquete de Lego do Rio de Janeiro", "Infantil|Artes Visuais", "cidadeartes",
   "A cidade inteira montada em peças de Lego, em exposição permanente.",
   'Exposição permanente "Maquete de Lego do Rio de Janeiro" Domingo a sábado, das 10h às 18h. Grátis. Livre.', SMC,
   cartaz=C(None, None, "Todos os dias, 10h–18h"), preco="Grátis", gratis=True, classif="Livre")
ev("Exposição Literária – Mês da Consciência Negra", "Livros & Debates", "milton",
   "No mês da Consciência Negra, a biblioteca expõe livros de autoras e autores negros.",
   'Exposição Literária (Mês da Consciência Negra) 01/11 a 30/11, à partir das 10:00 Classificação livre ... a Biblioteca aproveita o tema e promove uma exposição de livros de autoria negra.', SMC,
   cartaz=C("2026-11-01", "2026-11-30", "A partir das 10h"), preco="", classif="Livre",
   nota="Preço não informado na fonte.")
ev("Clube de Leitura Infantil – Consciência Negra", "Infantil|Livros & Debates", "moacyr",
   "Leituras de livros infantis sobre a temática negra.",
   'Clube de Leitura Infantil - mês da Consciência Negra 17/11 a 19/11 - 15:00 Classificação livre', SMC,
   sessoes=["2026-11-17 15:00", "2026-11-18 15:00", "2026-11-19 15:00"], preco="", classif="Livre",
   nota="Endereço da biblioteca não consta no PDF; preço não informado.")
ev("Consciência – Baile o Charme", "Música", "jacob",
   "Baile charme em celebração à cultura negra, com música, dança e elegância.",
   'Consciência – Baile o Charme Domingo (15/11), às 14h. R$ 10. Livre.', SMC,
   sessoes=["2026-11-15 14:00"], preco="R$ 10", pmin=10, pmax=10, classif="Livre")
ev("Ecos da Diáspora: Medida Provisória", "Cinema", "dyla",
   "Exibição do filme de Lázaro Ramos no projeto Ecos da Diáspora, com o Cine Praça Seca.",
   'Projeto Ecos da Diáspora, em parceria com o Cine Praça Seca, exibe "Medida Provisória" Quarta-feira(18/11), às 14h. Grátis. 14 anos.', SMC,
   sessoes=["2026-11-18 14:00"], preco="Grátis", gratis=True, classif="14 anos")
ev("As Irmãs Pereira", "Teatro", "ziembinski",
   "Três irmãs na casa da família, no Largo do Boticário, decidem onde jogar as cinzas da mãe e revisitam desejos e memórias.",
   'Espetáculo "As Irmãs Pereira" Sextas-feiras e sábados às 20h, e domingo às 19h. R$ 35 a R$ 70. 12 anos.', SMC,
   sessoes=["2026-11-15 19:00"], preco="R$ 35 a R$ 70", pmin=35, pmax=70, classif="12 anos",
   nota="Fonte sem data final; incluída só a sessão até 18/11.")
ev("Quintal", "Infantil|Teatro", "ziembinski",
   "Cinco crianças do subúrbio lutam para salvar o quintal onde brincam da especulação imobiliária.",
   'Espetáculo "Quintal" Sábados e domingos às 16h. Até 22/11. R$ 20 a R$40. Livre.', SMC,
   sessoes=["2026-11-15 16:00", "2026-11-21 16:00", "2026-11-22 16:00"], preco="R$ 20 a R$ 40", pmin=20, pmax=40, classif="Livre")
ev("Rei de Copas", "Teatro", "ziembinski",
   "Após a morte do pai, irmãos e o viúvo precisam decidir o destino de um bar de jogos de tabuleiro que só dá prejuízo.",
   'Espetáculo "Rei De Copas" Terças e quartas-feiras, às 20h. Até 18/11. R$ 30 a R$ 60. 12 anos.', SMC,
   sessoes=["2026-11-17 20:00", "2026-11-18 20:00"], preco="R$ 30 a R$ 60", pmin=30, pmax=60, classif="12 anos")
ev("SuperAções", "Infantil|Música", "guignoltijuca",
   "Monólogo circense-musical: um homem-banda toca até 11 instrumentos ao mesmo tempo e se equilibra em pernas de pau.",
   'Peça "SuperAções" Domingo (15/11), às 16h. Grátis. Livre.', SMC,
   sessoes=["2026-11-15 16:00"], preco="Grátis", gratis=True, classif="Livre", rua=True)
ev("Grupo Lekê: Música, Arte e Ancestralidade", "Música", "musicacarioca",
   "Músicos negros aproximam a música de concerto da música afro-brasileira, de pontos de terreiro a arranjos orquestrais.",
   'Clássicos Domingos apresenta Grupo Lekê: Música, Arte e Ancestralidade Domingo (15/11), às 11h. Ingressos: R$ 15 a R$ 30. Livre.', SMC,
   sessoes=["2026-11-15 11:00"], preco="R$ 15 a R$ 30", pmin=15, pmax=30, classif="Livre")
ev("Pérolas Negras – Histórias da Mãe África", "Infantil|Teatro", "musicacarioca",
   "A Cia. Mimos conta três histórias da tradição oral africana com mímica, objetos e música ao vivo.",
   'Domingo das Crianças: Cia Mimos apresenta Pérolas Negras – Histórias da Mãe África Domingo (15/11), às 16h. R$ 20 a R$ 40. Livre.', SMC,
   sessoes=["2026-11-15 16:00"], preco="R$ 20 a R$ 40", pmin=20, pmax=40, classif="Livre")
ev("Julio! em O Canto que a História Não Conta", "Música", "musicacarioca",
   "Show acústico do cantor e professor de História sobre os grandes intérpretes e compositores negros do samba.",
   'Quartas Acústicas: Julio! em "O Canto que a História Não Conta" Quarta-feira (18/11), às 19h. R$ 30 a R$ 60. Livre.', SMC,
   sessoes=["2026-11-18 19:00"], preco="R$ 30 a R$ 60", pmin=30, pmax=60, classif="Livre")
ev("Música Brasilis", "Artes Visuais|Música", "musicacarioca",
   "Exposição sobre a música brasileira no Centro da Música Carioca.",
   'Exposição "Música Brasilis" Terça-feira a domingo, das 10h às 17h. Grátis. Livre.', SMC,
   cartaz=C(None, None, "Terça a domingo, 10h–17h"), preco="Grátis", gratis=True, classif="Livre")
ev("Festival MonStra – Tripas, Coração (último dia)", "Teatro", "coreografico",
   "Encerramento da mostra de dança e performance com três trabalhos: Uma Coisa de Cada Vez, Manual de Feitiço e Nuca.",
   'Festival MonStra – 7ª edição: Tripas, Coração Sexta-feira e sábado (13 e 14/11) às 19h, e domingo (15/11), às 18h. R$ 20 a R$ 40. 14 anos.', SMC,
   sessoes=["2026-11-15 18:00"], preco="R$ 20 a R$ 40", pmin=20, pmax=40, classif="14 anos")
ev("Aladdin – Um Novo Mundo", "Infantil|Teatro", "dicro",
   "Montagem infantil da história do jovem que encontra uma lâmpada mágica.",
   'Espetáculo "Aladdin - Um Novo Mundo" Domingo (15/11),às 15h. R$ 20 a R$ 40. Livre.', SMC,
   sessoes=["2026-11-15 15:00"], preco="R$ 20 a R$ 40", pmin=20, pmax=40, classif="Livre")
ev("Cravejar o Corpo, Inventar o Mundo – Madah Sodré", "Artes Visuais", "dicro",
   "Pinturas que partem do corpo trans e travesti como lugar de memória, desejo e invenção.",
   'Ocupação Galeria L: "Cravejar o Corpo, Inventar o Mundo com: Madah Sodré" Visitação de terça a domingo, das 10h. Até 12/01/2027. Grátis. Livre.', SMC,
   cartaz=C(None, "2027-01-12", "Terça a domingo, a partir das 10h"), preco="Grátis", gratis=True, classif="Livre")
ev("Bora Lá – Comédia de Improviso", "Teatro", "fernandotorres",
   "Quatro artistas e um convidado criam cenas na hora a partir de sugestões da plateia.",
   'Espetáculo "Bora Lá – Comédia de Improviso\' Domingo (15/11), às 18h. R$ 30 a R$ 60. 16 anos.', SMC,
   sessoes=["2026-11-15 18:00"], preco="R$ 30 a R$ 60", pmin=30, pmax=60, classif="16 anos")
ev("Em Gira: Ela Encruzilhada", "Teatro|Música", "terra",
   "A passista Iara Cassano percorre as encruzilhadas do samba, do quintal da avó à avenida.",
   'Espetáculo "Em Gira: Ela Encruzilhada" Domingo (15/11), às 17h. Grátis. Livre.', SMC,
   sessoes=["2026-11-15 17:00"], preco="Grátis", gratis=True, classif="Livre")
ev("Roda de Samba Democráticos de Guadalupe", "Música", "terra",
   "Grupo tradicional do bairro, ligado ao Trem do Samba, com a raiz do samba de quintal suburbano.",
   'Roda de Samba Democráticos de Guadalupe Domingo (15/11), às 18h. Grátis. Livre.', SMC,
   sessoes=["2026-11-15 18:00"], preco="Grátis", gratis=True, classif="Livre")
ev("Encontro Anual de Mulheres Tèmiloju Brasil", "Livros & Debates", "zefiro",
   "Roda de conversa com mulheres e lideranças comunitárias sobre trajetórias femininas.",
   'Roda de conversa "Encontro Anual de Mulheres Tèmiloju Brasil - Minha Vida é mais importante" Domingo (15/11), às 09h. Grátis. Livre.', SMC,
   sessoes=["2026-11-15 09:00"], preco="Grátis", gratis=True, classif="Livre")
ev("Cine Jorge Amado: Autoestima de Crianças Negras", "Cinema|Infantil", "jorgeamado",
   "Exibição sobre a formação da identidade étnica e o empoderamento de crianças negras.",
   'Exibição de filme "Cine Jorge Amado – Programa Nação: Autoestima de Crianças Negras\' Segunda-feira(16/11), às 17h. Grátis. Livre.', SMC,
   sessoes=["2026-11-16 17:00"], preco="Grátis", gratis=True, classif="Livre")
ev("Júlia Lopes de Almeida: Um Fenômeno Literário na Cena Carioca", "Livros & Debates|Artes Visuais", "marques",
   "Fotos, publicações e objetos da escritora, do acervo mantido por seus netos.",
   'Exposição Júlia Lopes de Almeida: Um Fenômeno Literário na Cena Carioca Sábados das 9 às 13 h. Grátis. Livre.', SMC,
   cartaz=C(None, None, "Sábados, 9h–13h"), preco="Grátis", gratis=True, classif="Livre")
ev("Acorda & Samba convida João Martins", "Música", "hermeto",
   "Roda de samba com convidado, feira de artesãos locais e rock no encerramento.",
   'Festival Acorda & Samba convida João Martins Domingo (15/11), às 12h. Grátis. 14 anos.', SMC,
   sessoes=["2026-11-15 12:00"], preco="Grátis", gratis=True, classif="14 anos")
ev("Ônibus Biblioteca – Livros nas Praças", "Livros & Debates|Infantil", "hermeto",
   "Biblioteca itinerante com empréstimo gratuito, leitura dramatizada e contação de histórias.",
   'Ônibus Biblioteca – Livros nas Praças De 13 a 27 de novembro, às 11h. Grátis. Livre.', SMC,
   cartaz=C("2026-11-13", "2026-11-27", "A partir das 11h"), preco="Grátis", gratis=True, classif="Livre", rua=True)
ev("Domingo recreativo para crianças", "Infantil", "sandra",
   "Jogos, brincadeiras e pintura para a criançada, todo domingo.",
   'Domingo recreativo para crianças Domingos, às 10h. Grátis. Livre.', SMC,
   sessoes=["2026-11-15 10:00"], preco="Grátis", gratis=True, classif="Livre",
   nota="Fonte diz 'todos os domingos do mês', mas o PDF só vale até 18/11; 22/11 removido após conferência.")

# ---------------- CCBB ----------------
CCBB_LINK = "https://ccbb.com.br/rio-de-janeiro/programacao/"
ev("MEME: no Br@sil da memeficação", "Artes Visuais", "ccbb",
   "Primeira grande exposição brasileira sobre memes: cerca de 800 obras e conteúdos de 200 artistas e criadores.",
   'MEME: no Br@sil da memeficação 07/11/26 a 01/02/27 Ingressos L Classificação Livre Quarta a segunda, 9h às 20h. Fecha terça. 1º andar Entrada gratuita. Retirada de ingressos na bilheteria ou no site.', CCBB,
   cartaz=C("2026-11-07", "2027-02-01", "Quarta a segunda, 9h–20h"), preco="Grátis (retirada de ingresso)", gratis=True, classif="Livre",
   link=CCBB_LINK + "meme-no-brsil-da-memeficacao/")
ev("YOKAI PARADE – Seres sobrenaturais do Japão", "Artes Visuais", "ccbb",
   "Seres do folclore japonês em gravuras, pergaminhos e animação, pela primeira vez no Brasil.",
   'YOKAI PARADE – Seres sobrenaturais do Japão 13/11/26 a 03/01/27 Ingressos L Classificação Livre Quarta a segunda, das 9h às 20h 4º andar Entrada gratuita. Retirada de ingressos na bilheteria ou no site.', CCBB,
   cartaz=C("2026-11-13", "2027-01-03", "Quarta a segunda, 9h–20h"), preco="Grátis (retirada de ingresso)", gratis=True, classif="Livre",
   link=CCBB_LINK + "yokai-parade-seres-sobrenaturais-do-japao/")
ev("Amazônicas – Poéticas Femininas (últimos dias)", "Artes Visuais", "ccbb",
   "Arte contemporânea de mulheres do Pará, Acre e Amazonas, dos anos 1970 a hoje.",
   'Amazônicas – Poéticas Femininas 02/09/26 a 16/11/26 Ingressos L Classificação Livre Quarta a segunda, 9h às 20h. Fecha terça. 2º andar Entrada gratuita.', CCBB,
   cartaz=C("2026-09-02", "2026-11-16", "Quarta a segunda, 9h–20h"), preco="Grátis", gratis=True, classif="Livre",
   link=CCBB_LINK + "amazonicas-poeticas-femininas/")
ev("Um Atlas de Lembranças", "Artes Visuais", "ccbb",
   "Documentos, fotos e objetos sobre os 120 anos do prédio do CCBB.",
   'Um Atlas de Lembranças Ingressos L Classificação Livre Qua a seg, 9h às 20h 4º andar - Museu BB Entrada gratuita.', CCBB,
   cartaz=C(None, None, "Quarta a segunda, 9h–20h"), preco="Grátis", gratis=True, classif="Livre",
   link=CCBB_LINK + "um-atlas-de-lembrancas/")
ev("Palavras em Cena: O Cinema que Veio dos Livros", "Livros & Debates|Cinema", "ccbb",
   "Na biblioteca do CCBB, livros e filmes lado a lado: dos clássicos brasileiros às grandes adaptações internacionais.",
   'Palavras em Cena: O Cinema que Veio dos Livros Até 04/01/27 L Classificação Livre Qua a seg, 9h às 20h Biblioteca, 5º andar Entrada gratuita.', CCBB,
   cartaz=C(None, "2027-01-04", "Quarta a segunda, 9h–20h"), preco="Grátis", gratis=True, classif="Livre",
   link=CCBB_LINK + "palavras-em-cena-o-cinema-que-veio-dos-livros/")
ev("Entre o Sim e o Nunca", "Teatro", "ccbb",
   "Aos 35 anos, uma mulher descobre que o pai registrado não é o biológico e sai em busca da própria origem. Drama com humor.",
   'Entre o Sim e o Nunca 04/11/26 a 29/11/26 ... 12 anos Qua a Sáb, 19h | Dom, 17h Teatro III R$ 30 (inteira) | R$ 15 (meia-entrada)', CCBB,
   sessoes=["2026-11-15 17:00", "2026-11-18 19:00", "2026-11-19 19:00", "2026-11-20 19:00", "2026-11-21 19:00",
            "2026-11-22 17:00", "2026-11-25 19:00"], preco="R$ 30 (meia R$ 15)", pmin=15, pmax=30, classif="12 anos",
   link=CCBB_LINK + "entre-sim-e-o-nunca/")
ev("Música no Museu", "Música", "ccbb",
   "Concertos gratuitos ao meio-dia; em novembro, com o RioWinds Festival e o RioHarp Festival.",
   'Música no Museu 04/11/26 a 25/11/26 Ingressos L Classificação Livre Dias 04, 07, 08, 11, 18, 22 e 25/11 4º andar - sala 26 Entrada gratuita ... os concertos acontecem sempre às quartas-feiras, às 12h30', CCBB,
   sessoes=["2026-11-18 12:30", "2026-11-25 12:30"], preco="Grátis", gratis=True, classif="Livre",
   link=CCBB_LINK + "musica-no-museu-2/",
   nota="Fonte lista também 22/11 (domingo), mas só dá horário para as quartas; 22/11 fica de fora até confirmação.")
ev("21º Festival de Cinema Italiano no Brasil", "Cinema", "ccbb",
   "Lançamentos e clássicos de Fellini, Rossellini e outros mestres do cinema italiano.",
   '21º Festival de Cinema Italiano no Brasil 05/11/26 a 30/11/26 ... Cinema I Entrada gratuita. Retirada de ingressos a partir das 9h, no dia da sessão.', CCBB,
   cartaz=C("2026-11-05", "2026-11-30", "Sessões diárias (ver grade no site)"), preco="Grátis (retirada no dia, a partir das 9h)", gratis=True,
   classif="Verificar por filme", link=CCBB_LINK + "21o-festival-de-cinema-italiano-no-brasil/")
ev("Cinemateca do MAM no CCBB", "Cinema", "ccbb",
   "Mostras da Cinemateca do MAM, entre elas o centenário de Maria Della Costa e uma trajetória do cinema feminino brasileiro.",
   'Cinemateca do MAM no CCBB 15/11/26 a 30/11/26 ... Cinema II Entrada gratuita. Retirada de ingressos a partir das 9h, no dia da sessão.', CCBB,
   cartaz=C("2026-11-15", "2026-11-30", "Sessões diárias (ver grade no site)"), preco="Grátis (retirada no dia, a partir das 9h)", gratis=True,
   classif="Verificar por filme", link=CCBB_LINK + "cinemateca-do-mam-no-ccbb/")
ev("Festival Arquivo em Cartaz – 11ª edição", "Cinema", "ccbb",
   "Seis filmes premiados do festival do Arquivo Nacional, com o tema Cinema, memória e justiça.",
   'Festival Arquivo em Cartaz – 11ª Edição 20/11/26 a 22/11/26 Ingressos 18 Classificação 18 anos ... Cinema II Entrada gratuita. Retirada de ingressos a partir das 9h, no dia da sessão.', CCBB,
   cartaz=C("2026-11-20", "2026-11-22", "Ver horários no site"), preco="Grátis (retirada no dia)", gratis=True, classif="18 anos",
   link=CCBB_LINK + "festival-arquivo-em-cartaz-11a-edicao/")
ev("Sudi – O Elogio da Surdez", "Infantil|Teatro", "ccbb",
   "Uma menina que percebe o mundo pelos olhos, pela pele e pelas mãos parte em busca da Flor de Oto, ao lado de uma amiga que fala Libras.",
   'Sudi – O Elogio da Surdez 21/11/26 a 22/11/26 ... Livre 16h Teatro I R$30 (inteira) | R$15 (meia-entrada)', CCBB,
   sessoes=["2026-11-21 16:00", "2026-11-22 16:00"], preco="R$ 30 (meia R$ 15)", pmin=15, pmax=30, classif="Livre",
   acess="Libras em cena", link=CCBB_LINK + "sudi-o-elogio-da-surdez/")
ev("Samba do Sacramento", "Música", "ccbb",
   "A roda comandada por Marcos Sacramento volta ao CCBB, com Rita Benneditto, Nilze Carvalho, Nina Rosa e DJs.",
   'Samba do Sacramento no CCBB 21/11/26 ... Livre Sábado, 17h às 3h Área Externa Entrada gratuita', CCBB,
   sessoes=["2026-11-21 17:00"], preco="Grátis", gratis=True, classif="Livre", link=CCBB_LINK + "samba-do-sacramento/", rua=True)
ev("Clube de Leitura CCBB com Raphael Montes", "Livros & Debates", "ccbb",
   "Conversa sobre suspense e crime na literatura a partir do romance Dias Perfeitos, com o autor.",
   'Clube de Leitura CCBB 25/11/26 Com Raphael Montes Ingressos 14 Classificação 14 anos Quarta, 17h30 Salão de Leitura da Biblioteca, 5º andar Evento gratuito. Ingressos às 9h, no dia do evento, na bilheteria física ou no site bb.com.br/cultura ... O livro escolhido para o encontro foi Dias Perfeitos.', CCBB,
   sessoes=["2026-11-25 17:30"], preco="Grátis (ingressos às 9h do dia)", gratis=True, classif="14 anos",
   link=CCBB_LINK + "clube-de-leitura-ccbb/")

# ---------------- Circo Voador (API) ----------------
ev("Festival Abraço Negro – Ilê Aiyê convida Surdo Um da Mangueira", "Música", "circo",
   "Na véspera do feriado da Consciência Negra, o bloco baiano Ilê Aiyê recebe o Surdo Um da Mangueira; abertura com Kazen Sorriso e convidados.",
   'slug 2026-11-19-festival-abraco-negro · data_raw 20261119 · chamada: "o Circo Voador recebe o Festival Abraço Negro" · "Kazen Sorriso e convidados / Ilê Aiyê convida Surdo Um da Mangueira – Abertura dos Portões: 20:00"', CIRCO,
   sessoes=["2026-11-19 20:00"], preco="", classif="", nota="Horário = abertura dos portões. Preço só na ticketeira (camada Apoio).")
ev("Ajulliacosta – turnê Novo Testamento", "Música", "circo",
   "A turnê do álbum Novo Testamento ganha data extra no Circo Voador.",
   'slug 2026-11-20-ajulliacosta · data_raw 20261120 · "Turnê do álbum "Novo Testamento" – Abertura dos Portões: 20:00" · chamada: "Uma noite não foi suficiente!"', CIRCO,
   sessoes=["2026-11-20 20:00"], preco="", nota="Horário = abertura dos portões. Preço só na ticketeira.")
ev("Rockeria 14 anos", "Música", "circo",
   "A festa de rock celebra 14 anos com show da Vaa Surf Band e DJs convidados.",
   'slug 2026-11-21-rockeria · data_raw 20261121 · chamada: "Uma das festas mais queridas do Rio está completando 14 anos" · "Show: Vaa Surf Band / DJs Leo Paes Leme convida DJ Saddam e DJ Felipe Guga – Abertura dos Portões: 21:00"', CIRCO,
   sessoes=["2026-11-21 21:00"], preco="", nota="Horário = abertura dos portões. Preço só na ticketeira.")

# ---------------- Sesc Tijuca ----------------
ev("La Strada – Os Que Vieram Antes de Nós", "Teatro", "sesctijuca",
   "Palhaçaria e teatro documentário sobre gerações de palhaços anônimos que fizeram a história do circo no Brasil.",
   'Sesc Tijuca domingo, 15/11/2026 18:00 R$ 30 Inteira | 15 Meia ... quinta-feira, 19/11/2026 19:00 R$ 30 Inteira | 15 Meia · APRESENTAÇÃO LIVRE · Duração: 1h10min', SESC,
   sessoes=["2026-11-15 18:00", "2026-11-19 19:00"], preco="R$ 30 (meia R$ 15)", pmin=15, pmax=30, classif="Livre",
   link="https://cultura.sescrio.org.br/programacao/la-strada-os-que-vieram-antes-de-nos",
   nota="O site oculta datas posteriores atrás de 'Ver mais'; podem existir outras sessões.")
ev("Gean Pankararu", "Música", "sesctijuca",
   "Músico do povo Pankararu (PE), indicado ao Indigenous Music Awards, une tradição indígena e música contemporânea do Nordeste.",
   'Gean Pankararu ... SHOW LIVRE ... Sesc Tijuca terça-feira, 17/11/2026 19:00 Grátis Libras', SESC,
   sessoes=["2026-11-17 19:00"], preco="Grátis", gratis=True, classif="Livre", acess="Libras",
   link="https://cultura.sescrio.org.br/programacao/gean-pankararu")
ev("Terreiro de Mangueira – Cordel Negro", "Música", "sesctijuca",
   "O grupo Cordel Negro mistura ritmos afro-indígenas com samba, choro, forró e carimbó.",
   'Terreiro de Mangueira Cordel Negro ... SHOW LIVRE ... Sesc Tijuca sexta-feira, 20/11/2026 14:00 Grátis', SESC,
   sessoes=["2026-11-20 14:00"], preco="Grátis", gratis=True, classif="Livre",
   link="https://cultura.sescrio.org.br/programacao/terreiro-de-mangueira")
ev("Rio Maracatu", "Música", "sesctijuca",
   "Há 28 anos nas ruas do Centro, o grupo apresenta toadas das nações de maracatu de baque virado, ciranda e coco.",
   'Rio Maracatu ... SHOW LIVRE ... Sesc Tijuca domingo, 22/11/2026 15:00 Grátis', SESC,
   sessoes=["2026-11-22 15:00"], preco="Grátis", gratis=True, classif="Livre",
   link="https://cultura.sescrio.org.br/programacao/rio-maracatu")

for i, e in enumerate(EV, 1):
    e["id"] = f"2026-11-15-{i:03d}"
os.makedirs("/home/claude/agenda-rio/dados/edicoes/2026-11-15", exist_ok=True)
json.dump({"edicao": EDICAO, "eventos": EV}, open("/home/claude/agenda-rio/dados/edicoes/2026-11-15/eventos.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print(len(EV), "eventos")
