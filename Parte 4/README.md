# Estudo Dirigido — Parte 4: Filtros Digitais

Repositório da Parte 4 do Estudo Dirigido de Processamento Digital de Sinais, sobre projeto e análise de filtros digitais (FIR e IIR).

## Problema norteador (PBL)

Um sistema de monitoramento agrícola utiliza sensores para medir variáveis ambientais e operacionais, mas os sinais adquiridos apresentam ruídos e interferências do ambiente e dos circuitos eletrônicos. As simulações deste repositório investigam, de forma incremental, como projetar e validar filtros digitais capazes de reduzir esses ruídos sem comprometer a informação relevante para a tomada de decisão — culminando na Questão 10, que aplica esse raciocínio à suavização de um sinal de sensor.

## Estrutura do repositório

```
/teoria
    resumo_teorico.md          -> resumo teórico (conceitos de FIR, IIR, resposta em frequência/fase, atraso de grupo, estabilidade, aplicações)
/simulacoes
    q01_filtro_passabaixa_senoides.py
    q02_fir_ruido_branco.py
    q03_iir_butterworth_ruido.py
    q04_comparacao_fir_iir.py
    q05_polos_zeros_estabilidade.py
    q06_resposta_impulso_fir_iir.py
    q07_filtro_passafaixa.py
    q08_resposta_fase_fir_iir.py
    q09_atraso_grupo.py
    q10_aplicacao_pratica_sensor.py
/resultados
    q01...q10_*.png             -> gráficos gerados por cada script
    discussao_tecnica.md        -> discussão técnica relacionando teoria e prática (todas as questões)
README.md
```

## Como executar

Requer Python 3 com `numpy`, `scipy` e `matplotlib`:

```bash
pip install numpy scipy matplotlib
cd simulacoes
python3 q01_filtro_passabaixa_senoides.py
# ... (cada script roda de forma independente e salva seu gráfico em /resultados)
```

## Descrição das atividades desenvolvidas

| Questão | Tema | Resultado principal |
|---|---|---|
| 1 | Passa-baixa em duas senoides | Atenuação de -45,5 dB na componente indesejada |
| 2 | FIR + ruído branco | SNR de 3,2 dB → 16,0 dB |
| 3 | IIR Butterworth + ruído branco | SNR equivalente ao FIR (15,4 dB) com ordem 25x menor, após corrigir o atraso de fase |
| 4 | Comparação de respostas em frequência | IIR atinge maior seletividade por coeficiente; FIR mantém fase linear |
| 5 | Polos, zeros e estabilidade | Polo deslocado para fora do círculo unitário → sistema instável |
| 6 | Resposta ao impulso | FIR se anula exatamente; IIR decai geometricamente sem nunca zerar |
| 7 | Filtro passa-faixa | Isolamento de 60 Hz com -0,2 dB, demais componentes a -46 dB |
| 8 | Resposta de fase / fase linear | Desvio de fase do FIR em relação a uma reta: ~10⁻¹⁵ rad |
| 9 | Atraso de grupo | FIR constante (30 amostras); IIR varia de 13,8 a 20,8 amostras |
| 10 | Aplicação prática (sensor) | Redução de 78,9% no erro de leitura de um acelerômetro simulado |

A discussão técnica completa, relacionando cada resultado à teoria, está em [`resultados/discussao_tecnica.md`](resultados/discussao_tecnica.md).
