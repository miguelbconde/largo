# Teste das plataformas de ingresso — 19/11/2026

Reconhecimento feito pelo coletor no GitHub (`ferramentas/coleta/plataformas_teste.py`), em duas rodadas, com poucas visitas e pausa entre elas, identificado como LargoBot, sem login. As respostas brutas ficaram no ramo temporário `teste-plataformas`, fora do site e da linha principal.

| Plataforma | Resultado | Por onde |
|---|---|---|
| **Ingresso.com** | Aberta. Tudo legível. | A porta de dados que o próprio site usa (`api-content.ingresso.com`) responde sem chave: lista de 42 cinemas do Rio, filmes em cartaz e a grade completa de cada cinema, com data, hora, sala e preço, para cerca de duas semanas. Só o Estação Claro Rio tem 169 sessões na grade lida. O IMS não tem grade ali (fechado para obras). Por ora a Ingresso.com só traz cinema no Rio. |
| **Sympla** | Aberta. Legível. | Cada página de eventos da cidade traz embutidos os dados do mecanismo de busca da Sympla: nome, início e fim, local com endereço e coordenadas, organizador e link. A busca informa cerca de 2.200 eventos no Rio, 271 deles em teatro. Dá para paginar (`?page=2`, `?page=3`…). Os dados trazem também o e-mail do organizador: pelo nosso protocolo, não é extraído. |
| **Ticketmaster** | Fechada. | O site responde com uma tela de verificação de identidade contra robôs. Pelo nosso protocolo, não rompemos barreiras técnicas. A chave oficial fica de fora: os termos proíbem guardar os dados além do necessário e obrigam a apagá-los em 24 horas a pedido, o que é incompatível com dados abertos. |
| **Eventim** | Sem resposta. | O site não respondeu às visitas vindas do GitHub (tempo esgotado), nem com espera de 60 segundos. Pode ser bloqueio de servidores de nuvem. Próximo teste: a ronda no computador da coordenação. |

**Achado político.** Equipamentos públicos vendem pela Sympla: o Teatro Correios Léa Garcia, da Prefeitura, aparece como organizador "Município do Rio de Janeiro". A programação pública passa por plataforma privada, que a guarda sob suas regras. Material para o indicador de cercamento e para o pedido à Prefeitura.

**Ticketmaster sem rota.** Os grandes shows que ela vende costumam acontecer em casas que já estão no cadastro (Farmasi Arena, Qualistage etc.). Por ora, cobrimos esses eventos pelo site das casas.
