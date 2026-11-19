# Todos os Rios

Agenda cultural aberta do Rio de Janeiro. Guia semanal público e gratuito, com calendários assináveis e dados abertos.

O projeto parte do direito à cidade: a informação sobre a vida cultural do Rio é um bem comum e deve circular livre, sem cadastro, sem rastreadores e sem plataformas fechadas.

**Situação:** protótipo. Poucas fontes ainda; a edição publicada é de teste.

## O que há aqui

| Pasta | Conteúdo |
|---|---|
| `docs/` | O site publicado: página principal, calendários (`calendarios/*.ics`), dados abertos (`dados/`) e o estudo de design (`estudo-a/`) |
| `documentos/` | Plano diretor, guia de design e relatório do primeiro protótipo |
| `dados/` | Mapa de fontes (`fontes.csv`) e a base de cada edição (`edicoes/<data>/`): eventos, conferência independente, destaques e relatório de exceções |
| `ferramentas/` | Gerador do site e dos calendários (`gerar.py`), modelos visuais e o registro da redação de cada edição |

## Como uma edição é feita

1. Coleta nas fontes e redação das fichas, guardando o trecho da fonte de cada informação.
2. Conferência independente, campo a campo, e conferência mecânica por regras.
3. Escolha dos destaques ("A boa") segundo critérios públicos.
4. `python3 ferramentas/gerar.py <data-da-edição>` gera o site, os calendários, os dados abertos e o relatório.

## Licenças

- Textos: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.pt-br)
- Dados: [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/)
- Código: [MIT](https://opensource.org/license/mit)
- Fontes tipográficas embutidas no estudo de design: Archivo e Source Serif 4, ambas sob SIL Open Font License.

Pode copiar, reutilizar e adaptar, inclusive comercialmente, desde que cite a fonte e mantenha abertas as obras derivadas de textos e dados.
