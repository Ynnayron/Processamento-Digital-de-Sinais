# PDS – Estudo Dirigido 1
## Processamento Digital de Sinais

---

## Problema Norteador (PBL)

> *Como representar matematicamente o comportamento temporal de um sensor real e quais propriedades estruturais devem ser analisadas para garantir o correto processamento digital desse sinal?*

**Resposta resumida:** O sinal do sensor é modelado como sequência discreta `x[n] = x(nTs)`, obtida por amostragem com `Fs ≥ 2·Fmax`. O processamento adequado exige um sistema **LIT, causal e BIBO-estável**, como o filtro de média móvel implementado na Simulação 5.

---

## Estrutura do Repositório

```
pds_estudo_dirigido/
├── README.md
├── teoria/
│   └── resumo_teorico.md          # Fundamentação teórica completa
├── simulacoes/
│   ├── simulacoes_pds.py          # Código Python comentado (5 simulações)
│   ├── discussao_tecnica.md       # Análise e interpretação dos resultados
└── resultados/
    ├── sim1_sequencias_elementares.png
    ├── sim2_operacoes_sinais.png
    ├── sim3_energia_potencia.png
    ├── sim4_classificacao_sistemas.png
    └── sim5_sensor_vibracao.png
```

---

## Simulações Desenvolvidas

| # | Título | Conteúdo abordado |
|---|--------|-------------------|
| 1 | Sequências Elementares | Impulso, degrau, exponencial real e complexa |
| 2 | Operações com Sinais | Deslocamento, inversão, escalonamento |
| 3 | Energia e Potência | Classificação e cálculo acumulado |
| 4 | Classificação de Sistemas | Memória, linearidade, causalidade, variância |
| 5 | Sensor de Vibração | Sinal real, FFT, filtragem, energia janelada |

---


##  Referências

- OPPENHEIM, A. V.; SCHAFER, R. W. *Discrete-Time Signal Processing*. Pearson, 2010.
- LATHI, B. P. *Signal Processing and Linear Systems*. Oxford, 1998.
- PROAKIS, J. G.; MANOLAKIS, D. G. *Digital Signal Processing*. Pearson, 2006.
