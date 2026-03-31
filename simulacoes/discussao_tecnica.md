# Discussão Técnica – Resultados das Simulações
## PDS – Parte 1: Sinais e Sistemas Discretos

---

## Simulação 1 – Sequências Elementares

O impulso unitário δ[n] confirmou seu papel como elemento fundamental: ao ser deslocado e ponderado, pode reconstruir qualquer sinal discreto pela expressão `x[n] = Σ x[k]·δ[n−k]`. O degrau unitário u[n] demonstra continuidade a partir de n=0, sendo útil para delimitar o suporte de outros sinais.

A exponencial real com `a=0.8` exibiu decaimento exponencial, com energia finita (calculada em aproximadamente 4.5 unidades), confirmando sua classificação como **sinal de energia**. A exponencial complexa com `ω₀=π/6` revelou perfeitamente as componentes cossenoidal e senoidal, verificando a fórmula de Euler.

## Simulação 2 – Operações com Sinais

O deslocamento de `n₀=5` amostras causou o esperado atraso no sinal original. A operação de inversão resultou em reflexão em torno de n=0, tornando o sinal causal (suportado em n≤0) em anticausal. O escalonamento por fator 2 simplesmente dobrou as amplitudes, sem alterar a forma do sinal.

Estas operações são fundamentais na implementação de filtros digitais, onde convolução é realizada via multiplicações, somas e deslocamentos.

## Simulação 3 – Energia e Potência

| Sinal            | Energia    | Potência   | Classificação     |
|------------------|------------|------------|-------------------|
| Exp. a=0.9       | Converge   | → 0        | Sinal de energia  |
| Constante = 1    | → ∞        | = 1        | Sinal de potência |
| cos(πn/8)        | → ∞        | = 0.5      | Sinal de potência |

Os gráficos de energia acumulada confirmaram que a exponencial decrescente possui energia finita, enquanto sinais periódicos (cosseno) e constantes acumulam energia indefinidamente, com potência média estabilizando em valor constante.

## Simulação 4 – Classificação de Sistemas

- **y[n] = 2·x[n]** — sem memória, linear e causal. A saída é simplesmente escalonada. Verificou-se que ao dobrar a entrada, a saída dobrou (superposição válida).

- **Média Móvel (M=5)** — com memória, linear, causal e invariante no tempo. O filtro suavizou o sinal cossenoidal, reduzindo amplitudes nas frequências mais altas. É a base de filtros FIR causais.

- **y[n] = x[n]²** — não-linear: `T{x₁+x₂} ≠ T{x₁}+T{x₂}`. O sinal de entrada cossenoidal tornou-se sempre positivo com frequência duplicada, evidenciando distorção harmônica.

- **y[n] = n·x[n]** — variante no tempo: o fator `n` muda a característica do sistema ao longo do eixo temporal. Uma entrada cos(ω₀n) deslocada não produz a saída deslocada correspondente.

## Simulação 5 – Sinal de Sensor de Vibração

O sinal simulado representou uma máquina rotativa com componente principal em **50 Hz** e harmônica em **120 Hz**, com ruído aditivo gaussiano. O espectro via FFT identificou claramente os dois picos de frequência, validando o teorema de Nyquist (Fs=1000 Hz ≫ 2×120=240 Hz).

A média móvel com M=10 amostras funcionou como **filtro passa-baixa** causal com memória, atenuando ruído e harmônicas de alta frequência. Trata-se de um sistema LIT, BIBO-estável (Σ|h[n]|=1 < ∞) e realizável em tempo real.

A energia janelada variou ao longo do tempo, refletindo flutuações do ruído. Em aplicações industriais, monitorar esta energia é técnica padrão para detecção de anomalias em máquinas (e.g., desequilíbrio de eixo, folgas mecânicas).

## Conclusão Geral

As simulações demonstraram de forma prática os conceitos teóricos fundamentais:
1. Sinais discretos são obtidos por amostragem e representados por sequências elementares.
2. Operações de deslocamento, inversão e escalonamento são blocos básicos de todo processamento digital.
3. A classificação de sistemas determina restrições de implementação — sistemas causais são obrigatórios em tempo real; a estabilidade BIBO garante saídas controladas.
4. O problema norteador (PBL) foi respondido: modelou-se o sinal de sensor como sinal de potência amostrado a 1 kHz, e identificou-se o filtro de média móvel como sistema LIT, causal, estável e com memória, adequado ao correto processamento digital do sinal.
