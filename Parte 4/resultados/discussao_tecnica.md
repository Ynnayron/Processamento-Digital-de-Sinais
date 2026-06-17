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

## Questão 6 — Resposta ao impulso finita vs infinita
A resposta ao impulso do FIR (ordem 41) é, por definição, idêntica aos próprios coeficientes do filtro: ela se anula exatamente a partir da 41ª amostra, pois não há realimentação. Já a resposta ao impulso do IIR Butterworth ainda apresentava amplitude residual de ordem 10⁻⁹ na amostra 250 — teoricamente nunca chega a zero, apenas decai geometricamente como `|polo|^n`, confirmando a definição teórica de resposta infinita.

## Questão 7 — Filtro passa-faixa
Em um sinal com componentes de 10, 60 e 150 Hz, um passa-faixa Butterworth (banda de 45–75 Hz) preservou a componente de 60 Hz com apenas -0,2 dB de atenuação, enquanto as outras duas foram atenuadas em mais de -46 dB. O resultado mostra como um passa-faixa combina, na prática, as características de um passa-alta e um passa-baixa para isolar uma região espectral específica.

## Questão 8 — Fase linear vs não linear
Ajustando uma reta à fase do FIR na banda de passagem, o desvio máximo foi de 2,7×10⁻¹⁵ rad — fase exatamente linear, garantida pela simetria dos coeficientes. A fase do IIR, por outro lado, descreve uma curva visivelmente não linear. Esse resultado é a confirmação numérica direta do conceito teórico de fase linear discutido no resumo.

## Questão 9 — Atraso de grupo
O atraso de grupo do FIR foi constante em **30 amostras** em toda a banda de passagem (valor teórico (ordem-1)/2, confirmado numericamente). O atraso do IIR variou entre 13,8 e 20,8 amostras dentro da mesma banda, com um pico próximo à frequência de corte. Em um sistema de comunicação, essa variação significa que diferentes componentes de frequência de um mesmo símbolo chegariam ao receptor em instantes diferentes, gerando interferência entre símbolos vizinhos (ISI) — por isso sistemas sensíveis a forma de onda costumam preferir FIR ou exigir equalização de fase quando usam IIR.

## Questão 10 — Aplicação prática: suavização de sinal de acelerômetro
Um sinal sintético de acelerômetro (movimento real a 1,5 Hz, somado a ruído eletrônico e vibração estrutural a 45 Hz) foi suavizado por um FIR de ordem 31 com corte em 5 Hz. O desvio padrão do erro em relação ao movimento real caiu de 0,650 para 0,137 m/s² (redução de **78,9%**), ao custo de um atraso de 75 ms. Esse exemplo conecta diretamente com a aplicação tecnológica citada no enunciado ("redução de ruído em sensores") e com o compromisso fundamental discutido na teoria: mais filtragem (corte mais baixo, ordem mais alta) reduz ruído, mas aumenta o atraso introduzido — uma escolha de projeto que depende da aplicação (em malhas de controle em tempo real, esse atraso pode ser um fator limitante).

## Síntese geral
As dez simulações, em conjunto, reproduzem experimentalmente os conceitos do resumo teórico: FIR oferece estabilidade incondicional e fase linear ao custo de maior ordem; IIR oferece seletividade eficiente ao custo de fase não linear e da necessidade de verificar estabilidade; e a escolha entre eles, em uma aplicação real (como o problema norteador de monitoramento agrícola), depende do compromisso entre custo computacional, atraso aceitável e sensibilidade à distorção de forma de onda.

