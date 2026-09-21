# KPI Explainability MVP

MVP desenvolvido para a disciplina de Tendências de Software do PPGC/UFRGS.

## Sobre o projeto

Este projeto apresenta um protótipo de uma interface para explicabilidade de KPIs gerados a partir de respostas de questionários organizacionais.

A ideia surgiu a partir do problema de pesquisa do mestrado, relacionado à explicabilidade dos indicadores gerados pelo Gen_Connect. Porém, este projeto é **completamente independente do Gen_Connect** e não possui integração com seu código ou infraestrutura.

O objetivo do MVP é demonstrar como um KPI pode deixar de ser apresentado apenas como um número e passar a mostrar de forma transparente:

- quais dados foram utilizados;
- como os dados foram agregados;
- qual fórmula foi aplicada;
- quais etapas levaram ao resultado final.

## Escopo

O MVP utiliza dados estáticos e apresenta um único KPI baseado em respostas de uma escala de 1 a 5.

O cálculo utilizado é:

KPI = (média das respostas / 5) × 100

Para o conjunto de dados utilizado no protótipo:

- 14 respostas;
- soma das respostas: 55;
- média aritmética: 3,93;
- escala máxima: 5;
- KPI resultante: 78,6%.

A interface apresenta também a distribuição das respostas e os valores individuais utilizados no cálculo.

## Tecnologias

- React
- TypeScript
- Vite
- CSS

Não são utilizados backend, banco de dados, autenticação, APIs externas ou modelos de IA.

## Execução

Instale as dependências:

```bash
npm install