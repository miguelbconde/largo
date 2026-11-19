import json
ev=json.load(open("dados/edicoes/2026-11-19/eventos.json"))["eventos"]
def i(t, local=None):
    ok=lambda e: local is None or local in e["local"]
    c=[e for e in ev if e["titulo"]==t and ok(e)] or [e for e in ev if e["titulo"].startswith(t) and ok(e)]
    assert len(c)==1, (t, len(c)); return c[0]["id"]
D={
"2026-11-19":[
 (i("Abertura da exposição"),"Sete artistas mulheres abrem a mostra que festeja um ano da Galeria Berê, de graça, na Gamboa."),
 (i("Festa, Fé e Luta"),"Arte negra carioca a no máximo R$ 10, na mostra que ocupa dois teatros do Centro até sábado."),
 (i("Poexistência"),"Sarau de microfone aberto numa biblioteca pública da Tijuca: é chegar e ler."),
 (i("KD O Show"),"Humor feito com a plateia em Pedra de Guaratiba, a preço popular."),
 (i("Festival Abraço Negro"),"O Ilê Aiyê recebe o Surdo Um da Mangueira na véspera do feriado."),
 (i("Guilherme Pozzi"),"Schumann, Beethoven, Chopin e Prokofiev ao piano, a R$ 40, numa sala pública da Lapa."),
],
"2026-11-20":[
 (i("12º Cortejo da Tia Ciata"),"Uma Tia Ciata de cinco metros puxa afoxés, maracatus e sambas pelas ruas da Pequena África. De graça e na rua."),
 (i("Festival Terreiro 2026"),"Sombrinha, Jongo da Serrinha e programação para crianças numa praça de Padre Miguel, da tarde à meia-noite."),
 (i("A Menina Dança","Guignol"),"A história de Maria Felipa contada às crianças com maracatu e samba de roda, de graça, na Tijuca."),
 (i("Cabeça de Porco"),"Direção indicada ao Prêmio Shell, numa peça sobre moradia e sonho na periferia, a no máximo R$ 10."),
 (i("Orquestra Agogô Carioca"),"Uma orquestra só de agogôs, regida por um mestre do carnaval, de graça na Praça Seca."),
 (i("Quintal do Renatin"),"Samba, capoeira, rap e poesia em roda na Ilha do Governador, com o público dentro da cena."),
],
"2026-11-21":[
 (i("Rolé Estácio"),"Caminhada guiada pelo berço do samba urbano, com Libras, terminando na quadra da Estácio de Sá."),
 (i("Baú da Dona Ivone Lara"),"O parceiro de duas décadas de Dona Ivone canta seus sambas, com Áurea Martins de convidada."),
 (i("A Cura da Terra"),"Estreia gratuita que conta as revoluções indígenas da América Latina, com banda em cena."),
 (i("Baile Charme"),"Baile de charme de manhã e de graça, na Praça Seca."),
 (i("Fora do Quadro"),"Voguing, hip hop e sapateado ocupam, na dança, o muro de um quartel da ditadura. De graça, na Penha."),
 (i("FIPAZO"),"Festival que leva pole dance, circo e dança a Pedra de Guaratiba, sem competição."),
],
"2026-11-22":[
 (i("Amanhecer Rio"),"Último dia do festival, com a Bateria da Portela ao meio-dia e roda de samba no encerramento, no Passeio Público."),
 (i("Mensageiras da Cultura"),"Uma banda só de mulheres festeja 50 anos, de graça, em Anchieta."),
 (i("Quintal"),"Último fim de semana da peça em que crianças do subúrbio defendem o lugar onde brincam."),
 (i("Festival Quem Dança"),"Manhã de dança de vários estilos, de graça, na areninha do Pechincha."),
 (i("Equina"),"Dança sobre o cuidado entre gente e cavalos, em temporada só até o dia 29."),
 (i("Domingo recreativo"),"Brincadeira de graça para as crianças de Santa Cruz, todo domingo."),
],
"2026-11-23":[
 (i("Ensaio de rua do Paraíso do Tuiuti"),"A temporada de ensaios para o Carnaval 2027 começou: o Tuiuti toma o Campo de São Cristóvão, de graça."),
 (i("Lançamento: Música em Pauta"),"Crítica de música reunida em livro, com a autora, numa segunda à noite em Ipanema."),
],
"2026-11-24":[
 (i("O Último Dia da Minha Vida"),"Penúltima sessão do drama de humor ácido, em teatro municipal a no máximo R$ 20."),
 (i("Priscilla em 2L"),"Stand-up e palhaçaria sobre uma transição de gênero depois dos 30, na Semana da Comédia."),
 (i("Alice no País das Maravilhas"),"Um musical em Pedra de Guaratiba, numa terça à noite."),
 (i("A poesia brasileira na Coleção Ciranda"),"Uma tarde de conferência sobre poesia brasileira na Academia, com Paulo Henriques Britto na coordenação."),
 (i("Seminário Estadual"),"Dia de debates gratuitos sobre educação antirracista no Muhcab. A prefeitura avisa que pode haver mudança: confirme antes de ir."),
],
"2026-11-25":[
 (i("Rap & Repente"),"Rimadores de duas tradições se encontram e conversam com o público jovem, de graça, na Praça Seca."),
 (i("Amanda Mendonça"),"Uma alagoana canta os 50 anos de carreira de Djavan."),
 (i("Mesa-redonda"),"Duas autoras discutem o incômodo na literatura infantil, numa biblioteca pública."),
 (i("O Último Dia da Minha Vida"),"Última sessão da temporada, a no máximo R$ 20."),
],
}
json.dump({"criterios_versao":"2026-11-15","dias":{d:[{"id":a,"porque":b} for a,b in l] for d,l in D.items()}},
          open("dados/edicoes/2026-11-19/destaques.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
p="ferramentas/modelo.html"; s=open(p,encoding="utf-8").read()
for a,b in [("Prévia de teste: poucas fontes ainda, e a programação da prefeitura vale só até 18/11.","Prévia de teste: ainda com poucas fontes."),
            ("Test preview: few sources so far; city-hall listings valid only until Nov 18. Descriptions in Portuguese.","Test preview: few sources so far. Descriptions in Portuguese."),
            ("Vista previa: pocas fuentes; la programación municipal vale solo hasta el 18/11. Descripciones en portugués.","Vista previa: aún con pocas fuentes. Descripciones en portugués.")]:
    if a in s: s=s.replace(a,b)
assert "18/11." not in s
open(p,"w",encoding="utf-8").write(s)
g="ferramentas/gerar.py"; t=open(g,encoding="utf-8").read()
t=t.replace('main(sys.argv[1] if len(sys.argv) > 1 else "2026-11-15")','main(sys.argv[1] if len(sys.argv) > 1 else "2026-11-19")')
open(g,"w",encoding="utf-8").write(t)
