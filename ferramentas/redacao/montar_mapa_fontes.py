import csv, re, unicodedata
SRC='/mnt/user-data/uploads/7909e88b-fontes_culturais_rio_210.csv'
rows=list(csv.DictReader(open(SRC,encoding='utf-8-sig'),delimiter=';'))

def norm(s): return unicodedata.normalize('NFD',s.lower()).encode('ascii','ignore').decode()

# ---------- bairro -> região (regionalização usada pela própria SMC) ----------
REG={
 'Centro':['centro','lapa','gamboa','saude','santo cristo','cidade nova','praca xi','rio comprido','santa teresa','cinelandia','praca maua','praca tiradentes','praca xv','castelo','zona portuaria','morro do pinto','saara','ouvidor'],
 'Zona Sul':['gloria','catete','copacabana','ipanema','leblon','gavea','botafogo','humaita','flamengo','laranjeiras','cosme velho','jardim botanico','lagoa','horto','urca','leme','jockey'],
 'Zona Sudoeste':['barra da tijuca','recreio','jacarepagua','pechincha','praca seca','vila valqueire','taquara','freguesia'],
 'Zona Norte':['tijuca','meier','madureira','penha','pavuna','guadalupe','anchieta','vista alegre','ilha do governador','cocota','mare','iraja','marechal hermes','cachambi','andarai','mangueira','alemao','ramos','oswaldo cruz','turiacu','engenho de dentro','campinho','manguinhos','alto da boa vista','vila isabel','grajau','maracana','sao cristovao'],
 'Zona Oeste':['bangu','realengo','campo grande','santa cruz','guaratiba','sepetiba'],
}
def regiao(b):
    n=norm(b)
    if 'toda a cidade' in n or 'itinerante' in n: return 'Toda a cidade'
    if any(k in n for k in ['niteroi','baixada','sao joao de meriti','caxias']): return 'Fora do município'
    # Barra da Tijuca antes de Tijuca
    found=[]
    for r,ks in REG.items():
        for k in ks:
            if k in n:
                if k=='tijuca' and 'barra da tijuca' in n and n.count('tijuca')==1: continue
                found.append(r)
    found=list(dict.fromkeys(found))
    if not found:
        if 'zona norte' in n: return 'Zona Norte'
        if 'zona oeste' in n: return 'Zona Oeste'
        if 'zona sul' in n: return 'Zona Sul'
        return '?'
    return found[0] if len(found)==1 else 'Várias'

# ---------- mapeamento de áreas editoriais ----------
def areas(cat,tipo):
    c=norm(cat+' '+tipo); a=[]
    if re.search(r'music|show|samba|choro|jazz|blues|rock|rap|pagode|forro|charme|bossa|mpb|concert|orquest|recita|opera|eletron|festa|gafieira|jongo|vinil|metal|soul',c): a.append('Música')
    if re.search(r'teatr|cenic|danca|bale|circ|stand|comedia|musicais|espetac|performance|cabare',c): a.append('Teatro')
    if re.search(r'exposic|artes visuais|arte contemp|galeri|fotograf|museu|arte moderna|arte popular|arte digital|design|gravura|multipl|arte e tecnologia|artes$',c): a.append('Artes Visuais')
    if re.search(r'cinema|audiovisual|filme|document|animac|cineclube',c): a.append('Cinema')
    if re.search(r'literat|livr|debate|seminar|palestra|conferenc|sarau|leitura|lancament|encontros|ciencia',c): a.append('Livros & Debates')
    if re.search(r'infantil',c): a.append('Infantil')
    return '|'.join(dict.fromkeys(a)) or 'Multitemático'

def esfera(nome,url,tipo):
    n=norm(nome+' '+url+' '+tipo)
    if 'ticketeira' in n: return 'Plataforma comercial'
    if 'oficial' not in norm(tipo) and re.search(r'imprensa|editorial|portal|blog|agregador|revista|guia',norm(tipo)): return 'Imprensa / agregador'
    if 'mam.rio' in n: return 'Instituição privada sem fins lucrativos'
    if re.search(r'prefeitura|riotur|\.rio\b|smc|lona|arena|municipal|museu do amanha|museudeartedorio|cidadedasartes|planeta\.rio|muhcab|parque gloria|laurinda|musicacarioca|carlos gomes|cafe pequeno|gonzaguinha|ziembinski|sergio porto|teatroipanema|imperator|cinecarioca',n): return 'Pública municipal'
    if re.search(r'rj\.gov|funarj|secec|theatromunicipal|salacecilia|mis\.rj|eavparquelage|casa franca|laura alvim|glaucio gill|joao caetano',n): return 'Pública estadual'
    if re.search(r'gov\.br|museus\.gov|ccjf|trf2|bn\.gov|arquivonacional|paco imperial|caixacultural|ccbb|correios|jbrj|museu nacional|mnba|mhn',n): return 'Pública federal'
    if re.search(r'sesc|firjan|sesi',n): return 'Sistema S'
    if re.search(r'roda|samba|cineclube|cultura de rua|baile|coletiv|agenda do samba|feira das yabas|ponto cine|tia nilda|terreiro|museu do samba|capiberibe',n): return 'Comunitária / independente'
    if re.search(r'ims|instituto|fundacao|casa roberto marinho|eva klabin|museu do pontal|oi futuro|futuros|abl|academia|real gabinete|circo crescer|casa do choro|pinakotheke|light',n): return 'Instituição privada sem fins lucrativos'
    return 'Privada'

# ---------- decisões editoriais por ID ----------
CAMADA={}; NOTA={}
def setc(ids,cam,nota=''):
    for i in ids: CAMADA[i]=cam; NOTA[i]=nota if nota else NOTA.get(i,'')
setc(range(1,26),'Apoio','Só para confirmar preço/horário de eventos já captados em fontes do Núcleo; não é porta de entrada.')
setc([26,27,36],'Radar','Paywall/direitos autorais: usar só para descobrir eventos (fatos). Sinopses sempre próprias.')
setc([28,29,30,31,34,35,38,39,40,41,42,50,166,217],'Radar','Usar para descobrir eventos que escaparam ao Núcleo.')
setc([37,43,44,45,46,47,48,49],'Arquivada','Portal nacional/revista: rendimento baixo para agenda semanal do Rio.')
setc([91,92,126,136,146],'Arquivada','Fora do município do Rio (escopo atual). Reavaliar na expansão metropolitana.')
setc([95],'Arquivada','Cursos pagos; fora do critério de programação cultural aberta.')
setc([192,194,196,197],'Arquivada','Feira essencialmente de consumo; incluir só eventos culturais pontuais via Radar.')
setc([193],'Arquivada','Feira de antiguidades/artesanato; música pontual pode entrar via Radar.')
setc([124],'Arquivada','Substituída: cada Lona/Arena/Areninha agora tem linha própria.')
setc([52],'Arquivada','Substituída: desdobrada em unidades do Sesc no município.')
DUP={211:185,212:187,213:72,214:69,215:68,216:71,218:189,220:125}
setc(DUP.keys(),'Arquivada','')
for d,o in DUP.items(): NOTA[d]=f'Duplicata do ID original {o} (fundida).'
SMC_PDF={32,55,56,84,85,86,89,90,93,100,114,115,116,117,118}
URL_FIX={185:'travessa.com.br/eventos',69:'bn.gov.br/acontece/eventos',68:'gov.br/casaderuibarbosa/pt-br/assuntos/eventos',72:'academia.org.br/eventos'}
EXTRA_NOTE={182:'Separar em duas fontes (Alfarabi e Baratos da Ribeiro) na verificação.',
 191:'Agrupa várias livrarias: desdobrar na verificação.',165:'Agrupa vários galpões: desdobrar na verificação.',
 219:'Nome ambíguo (Martins Fontes x Prefácio): verificar.',102:'Conferir URL oficial.',
 32:'FONTE-MESTRA: PDF semanal com toda a rede municipal (cultura.prefeitura.rio/agendacultural).',
 183:'Sazonal (temporada de carnaval).',184:'Sazonal (temporada de carnaval).',132:'Sazonal.',133:'Sazonal.',134:'Sazonal.',210:'Sazonal.',
 122:'Programação infantil comercial; manter com sinalização de preço.'}

def metodo(r,i):
    m=r['Método Técnico Recomendado']
    if i in SMC_PDF: return 'PDF semanal SMC (+ site próprio)'
    if 'instagram' in r['URL / Perfil'] or 'Monitoramento Social' in m: return 'Leitura assistida (Instagram) + canal de envio'
    if 'RSS' in m: return 'RSS / site'
    if 'API' in m or 'JSON-LD' in m: return 'Dados estruturados (JSON-LD/API)'
    return 'Site (leitura automática)'

def freq(cam,i,nota):
    if 'Sazonal' in nota: return 'Sazonal'
    return {'Núcleo':'Semanal','Radar':'Semanal','Apoio':'Sob demanda','Arquivada':'—'}[cam]

out=[]
for r in rows:
    i=int(r['ID']); cam=CAMADA.get(i,'Núcleo')
    nota=NOTA.get(i,''); 
    if i in EXTRA_NOTE: nota=(nota+' '+EXTRA_NOTE[i]).strip()
    reg=regiao(r['Bairro / Região'])
    if reg=='Fora do município' and cam!='Arquivada':
        cam='Arquivada'; nota=(nota+' Fora do município do Rio (escopo atual).').strip()
    out.append(dict(nome=r['Nome da Fonte'].strip(),url=URL_FIX.get(i,r['URL / Perfil'].strip()),tipo=r['Tipo de Fonte'].strip(),
        areas=areas(r['Categoria Artística'],r['Tipo de Fonte']),bairro=r['Bairro / Região'].strip(),regiao=reg,
        esfera=esfera(r['Nome da Fonte'],r['URL / Perfil'],r['Tipo de Fonte']),camada=cam,metodo=metodo(r,i) if cam!='Arquivada' else '—',
        frequencia=freq(cam,i,nota),status='a verificar',origem=f'planilha inicial #{i}',observacoes=nota))

# ---------- acréscimos: rede municipal confirmada no site da SMC (15/11/2026) ----------
SMC='cultura.prefeitura.rio'
def add(nome,url,tipo,areas_,bairro,reg,esf,met,status,orig,obs=''):
    out.append(dict(nome=nome,url=url,tipo=tipo,areas=areas_,bairro=bairro,regiao=reg,esfera=esf,camada='Núcleo',metodo=met,frequencia='Semanal',status=status,origem=orig,observacoes=obs))
P='PDF semanal SMC'; OK='confirmada'; O1='acréscimo — site SMC (15/11/2026)'
arenas=[('Areninha Cultural Hermeto Pascoal','Bangu','Zona Oeste'),('Areninha Cultural Terra','Guadalupe','Zona Norte'),
 ('Areninha Cultural Renato Russo','Cocotá (Ilha do Governador)','Zona Norte'),('Arena Carioca Dicró (Carlos Roberto de Oliveira)','Penha Circular','Zona Norte'),
 ('Arena Carioca Chacrinha (Abelardo Barbosa)','Pedra de Guaratiba','Zona Oeste'),('Arena Cultural Fernando Torres','Madureira (Parque de Madureira)','Zona Norte'),
 ('Areninha Cultural Gilberto Gil','Realengo','Zona Oeste'),('Areninha Cultural Sandra de Sá','Santa Cruz','Zona Oeste'),
 ('Arena Cultural Jovelina Pérola Negra','Pavuna','Zona Norte'),('Areninha Cultural Carlos Zéfiro','Anchieta','Zona Norte'),
 ('Areninha Cultural Herbert Vianna','Maré','Zona Norte'),('Areninha Cultural Jacob do Bandolim','Pechincha (Jacarepaguá)','Zona Sudoeste'),
 ('Areninha Cultural João Bosco','Vista Alegre','Zona Norte')]
for n,b,rg in arenas: add(n,SMC,'Arena / Areninha Cultural (antigas Lonas)','Música|Teatro|Infantil|Cinema',b,rg,'Pública municipal',P,OK,O1)
cc=[('Centro Cultural Oduvaldo Vianna Filho (Castelinho do Flamengo)','Flamengo','Zona Sul','Multitemático','Semiaberto segundo o site da SMC.'),
 ('Centro Cultural Professora Dyla Sylvia de Sá','Praça Seca','Zona Sudoeste','Cinema|Livros & Debates',''),
 ('Centro Coreográfico da Cidade do Rio de Janeiro','Tijuca','Zona Norte','Teatro',''),
 ('Centro Municipal de Arte Hélio Oiticica','Centro (Praça Tiradentes)','Centro','Artes Visuais',''),
 ('Memorial Getúlio Vargas','Glória','Zona Sul','Artes Visuais',''),
 ('Centro Municipal de Artes Calouste Gulbenkian','Praça XI','Centro','Artes Visuais|Música',''),
 ('Museu Histórico da Cidade','Gávea','Zona Sul','Artes Visuais','')]
for n,b,rg,a,o in cc: add(n,SMC,'Centro Cultural / Museu municipal',a,b,rg,'Pública municipal',P,OK,O1,o)
tt=[('Teatro Municipal Ruth de Souza','Santa Teresa','Centro','Teatro|Música'),('Teatro de Fantoches e Marionetes Carlos Werneck de Carvalho','Aterro do Flamengo','Zona Sul','Infantil|Teatro'),
 ('Teatro Municipal Domingos Oliveira (Planetário)','Gávea','Zona Sul','Teatro|Música'),('Teatro de Guignol Municipal da Tijuca','Tijuca','Zona Norte','Infantil|Teatro'),
 ('Teatro de Guignol Municipal do Méier','Méier','Zona Norte','Infantil|Teatro'),('Teatro Correios Léa Garcia','Centro','Centro','Teatro|Livros & Debates')]
for n,b,rg,a in tt: add(n,SMC,'Teatro municipal',a,b,rg,'Pública municipal',P,OK,O1)
O2='acréscimo — PDF semanal SMC 12–18/11/2026'
bib=[('Biblioteca Municipal José de Alencar','Santa Teresa','Centro'),('Biblioteca Municipal Annita Porto Martins','Rio Comprido','Centro'),
 ('Biblioteca Municipal Maria Firmina dos Reis','Cidade Nova','Centro'),('Espaço de Leitura Alfredo Machado','Copacabana','Zona Sul'),
 ('Biblioteca Ziraldo (Cidade das Artes)','Barra da Tijuca','Zona Sudoeste'),('Biblioteca Municipal Milton Santos (Areninha Jacob do Bandolim)','Pechincha','Zona Sudoeste'),
 ('Biblioteca Municipal Moacyr Teixeira','a confirmar','?'),('Biblioteca Municipal Jorge Amado (Areninha Herbert Vianna)','Maré','Zona Norte'),
 ('Biblioteca Municipal Marques Rebelo','Tijuca','Zona Norte'),('Biblioteca Municipal João do Rio','Irajá','Zona Norte'),
 ('Biblioteca Municipal Manuel Ignácio da Silva Alvarenga','Campo Grande','Zona Oeste')]
for n,b,rg in bib: add(n,SMC,'Biblioteca municipal','Livros & Debates|Infantil',b,rg,'Pública municipal',P,OK,O2)
add('Ecomuseu do Quarteirão Cultural do Matadouro de Santa Cruz',SMC,'Museu municipal','Artes Visuais|Infantil','Santa Cruz','Zona Oeste','Pública municipal',P,OK,O2)

# ---------- acréscimos a verificar (lacunas de território) ----------
O3='acréscimo — lacuna territorial (a verificar)'
V='Site (leitura automática)'; IG='Leitura assistida (Instagram) + canal de envio'
sesc=[('Sesc Copacabana','Copacabana','Zona Sul'),('Sesc Tijuca','Tijuca','Zona Norte'),('Sesc Madureira','Madureira','Zona Norte'),
 ('Sesc Ramos','Ramos','Zona Norte'),('Sesc Engenho de Dentro','Engenho de Dentro','Zona Norte'),('Sesc Campo Grande','Campo Grande','Zona Oeste')]
for n,b,rg in sesc: out.append(dict(nome=n,url='cultura.sescrio.org.br',tipo='Centro Cultural (Sistema S)',areas='Música|Teatro|Cinema|Livros & Debates|Infantil',bairro=b,regiao=rg,esfera='Sistema S',camada='Núcleo',metodo=V,frequencia='Semanal',status='a verificar',origem=O3,observacoes='Desdobramento da linha Sesc RJ; confirmar unidades ativas.'))
gaps=[('Biblioteca Parque Estadual','cultura.rj.gov.br','Biblioteca','Livros & Debates|Cinema|Infantil','Centro','Centro','Pública estadual',V,'Confirmar canal de programação.'),
 ('Bibliotecas Parque de Manguinhos e Rocinha','cultura.rj.gov.br','Biblioteca','Livros & Debates|Infantil','Manguinhos / Rocinha','Várias','Pública estadual',V,'Verificar se estão em funcionamento.'),
 ('Museu da Maré','instagram.com/museudamare','Museu comunitário','Artes Visuais|Livros & Debates','Maré','Zona Norte','Comunitária / independente',IG,''),
 ('Galpão Bela Maré / Observatório de Favelas','observatoriodefavelas.org.br','Centro Cultural','Artes Visuais|Livros & Debates','Maré','Zona Norte','Instituição privada sem fins lucrativos',V,''),
 ('Museu Bispo do Rosário Arte Contemporânea','museubispodorosario.com','Museu','Artes Visuais','Colônia Juliano Moreira (Jacarepaguá)','Zona Sudoeste','Pública municipal',V,'Confirmar URL.'),
 ('Fórum de Ciência e Cultura da UFRJ','forum.ufrj.br','Universidade','Livros & Debates|Música|Cinema','Urca / Centro','Várias','Pública federal',V,''),
 ('Casa da Ciência da UFRJ','casadaciencia.ufrj.br','Universidade / Centro Cultural','Livros & Debates|Artes Visuais|Infantil','Botafogo','Zona Sul','Pública federal',V,''),
 ('Centro Cultural da UERJ (Teatro Odylo Costa Filho e outros)','uerj.br','Universidade','Teatro|Música|Livros & Debates','Maracanã','Zona Norte','Pública estadual',V,'Confirmar canal de programação.'),
 ('Pontos de Cultura do município do Rio','cultura.prefeitura.rio','Rede / programa público','Multitemático','Toda a cidade','Toda a cidade','Comunitária / independente',IG,'Mapear pontos ativos com programação aberta.')]
for n,u,t,a,b,rg,e,m,o in gaps: out.append(dict(nome=n,url=u,tipo=t,areas=a,bairro=b,regiao=rg,esfera=e,camada='Núcleo',metodo=m,frequencia='Semanal',status='a verificar',origem=O3,observacoes=o))

# canal aberto de envio
out.append(dict(nome='Canal aberto de envio de programação',url='(a criar: formulário/e-mail do projeto)',tipo='Canal participativo',areas='Multitemático',bairro='Toda a cidade',regiao='Toda a cidade',esfera='Comunitária / independente',camada='Núcleo',metodo='Envio direto pelos espaços e coletivos',frequencia='Contínua',status='a criar',origem='plano diretor',observacoes='Prioridade para espaços sem site (rodas, cineclubes, coletivos).'))

# ordenar: camada, região, nome ; numerar
ordc={'Núcleo':0,'Radar':1,'Apoio':2,'Arquivada':3}
ordr={'Centro':0,'Zona Sul':1,'Zona Sudoeste':2,'Zona Norte':3,'Zona Oeste':4,'Várias':5,'Toda a cidade':6,'?':7,'Fora do município':8}
out.sort(key=lambda d:(ordc[d['camada']],ordr.get(d['regiao'],9),norm(d['nome'])))
cols=['id','nome','url','tipo','areas','bairro','regiao','esfera','camada','metodo','frequencia','status','origem','observacoes']
with open('/home/claude/agenda-rio/dados/fontes.csv','w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=cols,delimiter=';'); w.writeheader()
    for k,d in enumerate(out,1): d['id']=f'F{k:03d}'; w.writerow(d)
print(len(out))
