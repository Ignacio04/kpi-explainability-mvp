
# Relato

## Problema

KPIs são frequentemente apresentados como valores agregados, o que pode dificultar a compreensão de como o resultado foi obtido. No contexto do meu trabalho de mestrado, esse problema está relacionado à explicabilidade de indicadores gerados a partir de dados de questionários organizacionais.

Para explorar essa questão de forma prática, foi desenvolvido um MVP de uma interface capaz de apresentar não apenas o valor final de um KPI, mas também os dados e as etapas utilizadas em seu cálculo.

## Abordagem

O projeto foi desenvolvido como uma aplicação React + TypeScript + Vite independente do Gen_Connect. O escopo foi deliberadamente reduzido para permitir a experimentação em um período curto, utilizando apenas dados estáticos.

Foi escolhido um único KPI baseado em respostas de uma escala de 1 a 5. A aplicação apresenta:

- valor final do KPI;
- quantidade de respostas;
- distribuição das respostas;
- fórmula utilizada;
- soma e média das respostas;
- valores individuais utilizados no cálculo;
- explicação textual rastreável ao cálculo.

A fórmula utilizada no protótipo é:

`KPI = (média das respostas / 5) × 100`

## Uso do Spec Kit / OpenSpec

O desenvolvimento foi organizado utilizando especificações e artefatos para descrever o objetivo, o escopo e as tarefas antes da implementação.

A especificação ajudou a limitar o desenvolvimento ao problema definido para o MVP, evitando a inclusão de funcionalidades como backend, banco de dados, autenticação ou integração com sistemas externos.

Durante a implementação, os artefatos foram utilizados como referência para verificar se a solução permanecia dentro do escopo definido.

## Resultado

O resultado foi uma aplicação standalone que demonstra uma forma simples de tornar o cálculo de um KPI mais transparente.

Para o conjunto de dados utilizado, são apresentadas 14 respostas, cuja soma é 55. A média aritmética é 3,93 em uma escala máxima de 5, resultando em um KPI de aproximadamente 78,6%.

O protótipo permite visualizar diretamente a relação entre os dados de entrada, a fórmula e o resultado final, servindo como uma primeira exploração do problema de explicabilidade que será aprofundado no mestrado.

## Limitações e próximos passos

O MVP utiliza dados estáticos e uma única fórmula de cálculo. Portanto, ainda não contempla diferentes tipos de KPI, dados reais, interação com usuários ou técnicas mais avançadas de explicabilidade.

Como próximos passos, seria possível avaliar diferentes formas de apresentar explicações, comparar estratégias de visualização e investigar como usuários interpretam essas explicações em KPIs mais complexos.