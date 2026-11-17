# Protótipo 1 — relatório (15/11/2026)

Edição de teste: **15 a 25 de novembro de 2026**. O objetivo foi passar uma vez por todas as etapas, da coleta à publicação, com poucas fontes e dados reais.

## Resultado

- **73 atividades**: 46 eventos com 73 sessões e 27 exposições ou mostras em cartaz.
- **39 grátis** e **18 a preço popular** (inteira até R$ 40).
- **Por região:** Centro 31 · Zona Norte 21 · Zona Sul 11 · Zona Sudoeste 6 · Zona Oeste 3. Um evento ficou sem endereço.
- **Saídas geradas:** o site (uma página só, sem rastreadores), 13 calendários (geral, grátis, 6 áreas e 5 regiões) e dados abertos em CSV e JSON.

## Como cada fonte se comportou

| Fonte | Método | Resultado |
|---|---|---|
| PDF semanal da SMC | Navegador do computador + leitura do PDF | ✅ Excelente: cerca de 60 atividades, quase tudo estruturado. Só vale de quinta a quarta (aqui, até 18/11) |
| CCBB Rio | Site, páginas de cada evento | ✅ Bom: datas, horários, preços e classificação claros |
| Circo Voador | **API pública de eventos** (descoberta no teste) | ✅ Ótimo para automação. Falta o preço, que só aparece na ticketeira |
| Sesc RJ | Site, páginas de cada evento | ⚠️ Funciona, mas as datas futuras ficam escondidas atrás de "Ver mais" |
| IMS | Site | ❌ A sede no Rio está sem programação própria (atividades em instituições parceiras) |
| Theatro Municipal | Site | ❌ Certificado de segurança inválido; o site não abre |
| Imperator (Méier) | Site | ❌ Não carregou |
| Casa do Choro | Site | ❌ Em manutenção |

**Lição:** metade dos sites testados falhou de algum jeito. Isso confirma que o projeto precisa de três coisas:
1. o canal aberto de envio de programação;
2. fontes alternativas para cada espaço (redes, imprensa, ticketeiras na camada de Apoio);
3. o pedido de dados abertos à prefeitura.

## Dupla checagem

- O **conferente independente**, uma segunda instância de IA, conferiu os 73 eventos campo a campo contra o trecho da fonte. Encontrou **19 apontamentos em 17 eventos**:
  - **1 divergência real:** uma sessão sem amparo na fonte, que foi corrigida;
  - **18 dúvidas**, a maioria causada por trechos de fonte abreviados demais. Os trechos foram completados.
- A **conferência mecânica** (regras, sem IA) apontou 7 alertas: preço não informado em 5 eventos e endereço ausente em 1.
- Ao final, **71 eventos conferidos sem ressalva** e **2 publicados como "a confirmar"**: um com local deduzido pela posição no PDF e outro sem endereço na fonte.
- O relatório completo de exceções está em `dados/edicoes/2026-11-15/relatorio.md`.

**Melhoria para a próxima versão:** salvar automaticamente o texto integral de cada fonte no momento da coleta. Assim o conferente compara com a página inteira, e não só com o trecho escolhido pelo redator.

## Casos editoriais desta edição

Ficaram de fora:
- apresentações internas de escolas e academias (Arena Fernando Torres e Areninha Hermeto Pascoal);
- um seminário de formação;
- bazares e feiras de artesanato;
- trocas de livros;
- oficinas.

Caso-limite deixado de fora: a Feira MigrArtes (Parque Glória Maria), uma feira intercultural de migrantes com caráter de feira.

Problemas de qualidade encontrados no próprio PDF da prefeitura:
- restos de e-mail colados no texto;
- eventos de uma areninha aparecendo no bloco de outra (Renato Russo e Carlos Zéfiro);
- uma biblioteca sem endereço.

## Uso de IA

O conferente independente consumiu cerca de 100 mil tokens para 73 eventos. A redação das fichas foi feita nesta conversa. O consumo total do protótipo aparece em **Configurações > Uso** do app. Vale olhar agora, para termos a referência de quanto custa uma edição.

## Próximos passos sugeridos

1. Automatizar a coleta mecânica: PDF da SMC, API do Circo Voador e páginas do CCBB e do Sesc.
2. Ampliar as fontes da Zona Oeste e da Zona Sudoeste, hoje as mais fracas.
3. Criar o canal de envio e o endereço de contato.
4. Conta no GitHub e publicação da primeira versão pública.
