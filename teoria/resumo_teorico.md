# Resumo Teórico – Processamento Digital de Sinais
## Parte 1: Modelagem de Sinais e Sistemas Discretos
  


## 1. Sinais Contínuos e Discretos

Um **sinal** é uma função que carrega informação sobre o comportamento ou estado de um fenômeno físico. Matematicamente, pode ser representado como uma função de uma ou mais variáveis independentes.

### 1.1 Sinais Contínuos no Tempo (CT)
Um sinal contínuo `x(t)` é definido para todo valor real de `t`. Exemplos:
- Tensão em um circuito elétrico
- Temperatura medida por um sensor analógico
- Sinal de vibração de uma máquina

### 1.2 Sinais Discretos no Tempo (DT)
Um sinal discreto `x[n]` é definido apenas para valores inteiros de `n`. Ele é obtido pela **amostragem** de um sinal contínuo:

```
x[n] = x(nTs)
```

onde `Ts = 1/Fs` é o período de amostragem e `Fs` é a frequência de amostragem.

> **Teorema de Nyquist-Shannon:** Para reconstrução perfeita, a frequência de amostragem deve ser ao menos o dobro da frequência máxima presente no sinal: `Fs ≥ 2·Fmax`.

---

## 2. Sequências Elementares

### 2.1 Impulso Unitário (Delta de Kronecker)
```
δ[n] = 1,  se n = 0
δ[n] = 0,  se n ≠ 0
```
Qualquer sinal discreto pode ser expresso como combinação linear de impulsos deslocados:
`x[n] = Σ x[k]·δ[n−k]`

### 2.2 Degrau Unitário
```
u[n] = 1,  se n ≥ 0
u[n] = 0,  se n < 0
```
Relação com o impulso: `δ[n] = u[n] − u[n−1]`

### 2.3 Sequência Exponencial Real
```
x[n] = a^n · u[n],   a ∈ ℝ
```
- Se `|a| < 1`: sequência decrescente (convergente)
- Se `|a| > 1`: sequência crescente (divergente)
- Se `|a| = 1`: sequência constante

### 2.4 Exponencial Complexa
```
x[n] = A · e^(jω₀n) = A·[cos(ω₀n) + j·sin(ω₀n)]
```
Fundamental em análise espectral (Fourier).

---

## 3. Operações com Sinais

| Operação         | Notação         | Efeito                          |
|------------------|-----------------|---------------------------------|
| Deslocamento     | `x[n − n₀]`    | Atraso (n₀ > 0) ou avanço      |
| Inversão         | `x[−n]`        | Reflexão em torno de n = 0     |
| Escalonamento    | `x[αn]`        | Compressão (α > 1) ou expansão |
| Amplitude        | `A · x[n]`     | Amplificação/atenuação         |

---

## 4. Energia e Potência de Sinais

### Energia Total
```
E = Σ |x[n]|²   (soma de −∞ a +∞)
```

### Potência Média
```
P = lim (1/(2N+1)) · Σ |x[n]|²   (N → ∞)
```

### Classificação:
- **Sinal de energia:** `0 < E < ∞` → `P = 0`
- **Sinal de potência:** `0 < P < ∞` → `E = ∞`
- **Nem energia nem potência:** ambos divergem

---

## 5. Classificação de Sistemas Discretos

Um sistema discreto mapeia uma sequência de entrada `x[n]` em uma sequência de saída `y[n]`.

### 5.1 Memória
- **Sem memória:** a saída `y[n]` depende apenas de `x[n]`  
  *Exemplo:* `y[n] = 2·x[n]`
- **Com memória:** a saída depende de amostras passadas ou futuras  
  *Exemplo:* `y[n] = x[n] + x[n−1]`

### 5.2 Linearidade
Um sistema é **linear** se satisfaz os princípios de:
- **Aditividade:** `T{x₁[n] + x₂[n]} = T{x₁[n]} + T{x₂[n]}`
- **Homogeneidade:** `T{a·x[n]} = a·T{x[n]}`

Combinados: `T{a·x₁[n] + b·x₂[n]} = a·y₁[n] + b·y₂[n]`

### 5.3 Invariância no Tempo
Um sistema é **invariante no tempo (LIT)** se um deslocamento na entrada gera o mesmo deslocamento na saída:
```
x[n − n₀] → y[n − n₀]
```

### 5.4 Causalidade
- **Causal:** a saída em `n` depende apenas de `x[n], x[n−1], x[n−2], ...`
- **Não causal:** utiliza amostras futuras `x[n+k], k > 0`

> Em aplicações em tempo real, apenas sistemas causais são realizáveis.

### 5.5 Estabilidade BIBO
Um sistema é **estável BIBO** (*Bounded Input → Bounded Output*) se para toda entrada limitada a saída também é limitada:
```
|x[n]| ≤ Mx < ∞  →  |y[n]| ≤ My < ∞
```
Para sistemas LIT: condição equivalente é `Σ |h[n]| < ∞` (resposta ao impulso absolutamente somável).

### 5.6 Invertibilidade
Um sistema é **invertível** se existe um sistema inverso que recupera `x[n]` a partir de `y[n]`. Sistemas com perda de informação (ex: quadratura) geralmente não são invertíveis.

---

## 6. Relação com Aplicações em Engenharia

| Sinal Real                        | Representação Discreta         | Sistema Envolvido            |
|-----------------------------------|--------------------------------|------------------------------|
| Vibração em máquina rotativa      | `x[n]` amostrado a 10 kHz     | Filtro passa-banda LIT       |
| Temperatura de sensor industrial  | Exponencial + ruído branco     | Média móvel (com memória)    |
| Sinal elétrico digital            | Sequência binária              | Sistema sem memória          |
| Velocidade de eixo (encoder)      | Pulsos periódicos              | Contador / integrador        |
| Dado de sistema embarcado         | Amostragem em tempo real       | Sistema causal obrigatório   |

---

## 7. Referências Bibliográficas

- OPPENHEIM, A. V.; SCHAFER, R. W. *Discrete-Time Signal Processing*. 3. ed. Pearson, 2010.
- LATHI, B. P. *Signal Processing and Linear Systems*. Oxford University Press, 1998.
- PROAKIS, J. G.; MANOLAKIS, D. G. *Digital Signal Processing*. 4. ed. Pearson, 2006.
