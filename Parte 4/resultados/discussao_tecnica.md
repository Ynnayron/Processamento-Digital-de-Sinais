# Discussão Técnica — Simulações de Filtros Digitais

Este documento relaciona os resultados obtidos em cada simulação (pasta `/simulacoes`, gráficos em `/resultados`) com os conceitos apresentados no resumo teórico.

## Questão 1 — Filtro passa-baixa em sinal com duas senoides
O sinal de 5 Hz e 80 Hz foi filtrado por um FIR passa-baixa com corte em 20 Hz. A componente de 80 Hz foi atenuada em **-45,5 dB**, praticamente desaparecendo, enquanto a de 5 Hz manteve **94% da amplitude original**. Isso confirma na prática a definição de resposta em frequência: o filtro multiplica cada componente espectral por um ganho diferente, dependendo de sua posição em relação à frequência de corte.

## Questão 2 — Redução de ruído branco com filtro FIR
Um seno de 10 Hz contaminado por ruído branco (SNR inicial de 3,2 dB) foi filtrado por um FIR de ordem 101 com corte em 30 Hz, elevando o SNR para **16,0 dB** (ganho de 12,8 dB). O resultado mostra que, mesmo um filtro simples, ao concentrar a energia do ruído fora da banda de passagem, recupera de forma eficaz um sinal correlacionado em baixa frequência.

## Questão 3 — Comparação com filtro IIR Butterworth
Repetindo o experimento com um IIR Butterworth de ordem 4 (apenas 4 polos, contra 101 coeficientes do FIR), a comparação direta inicialmente indicou SNR de apenas 1,8 dB — pior do que o sinal sem filtrar. Investigando a causa, identificamos um atraso de fase de 13 amostras (13 ms) introduzido pelo IIR em 10 Hz, mesmo com magnitude próxima de 1 nessa frequência. Ao realinhar o sinal por esse atraso, o SNR subiu para **15,4 dB**, praticamente equivalente ao FIR, mas usando uma ordem 25 vezes menor. Esse resultado ilustra de forma direta o que a bibliografia (Proakis e Manolakis) descreve: IIR atinge seletividade equivalente ao FIR com ordem muito menor, à custa de uma fase não linear que precisa ser considerada na análise.

## Questão 4 — Respostas em frequência FIR vs IIR
Com a mesma frequência de corte (30 Hz), o FIR de ordem 21 apresentou um roll-off suave, o FIR de ordem 101 um roll-off muito mais abrupto (lóbulos laterais abaixo de -60 dB), e o IIR de ordem 4 atingiu uma queda mais rápida que o FIR de ordem 21 usando uma fração dos coeficientes. Em compensação, a fase do IIR é uma curva suave, enquanto a do FIR é (por trechos) uma reta — a assinatura visual da fase linear.

## Questão 5 — Polos, zeros e estabilidade
O filtro Butterworth corretamente projetado apresentou todos os polos com módulo entre 0,84 e 0,93 (dentro do círculo unitário → estável). Ao perturbar artificialmente o coeficiente de realimentação `a[1]`, um dos polos foi deslocado para módulo 4,75 — fora do círculo unitário — tornando o sistema instável. Esse experimento evidencia, de forma visual, por que a verificação da posição dos polos é etapa obrigatória no projeto de qualquer filtro IIR: pequenas mudanças nos coeficientes de realimentação podem levar um sistema estável a divergir.
