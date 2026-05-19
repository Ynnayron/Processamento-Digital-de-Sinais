# PDS – Estudo Dirigido Parte 3
## Análise no Domínio da Frequência

**Instituto Federal da Paraíba – IFPB**  
Processamento Digital de Sinais · Engenharia de Computação
Aluno: Ynnayron Juan Lopes da Silva

---

## Estrutura do Repositório

```
 teoria/
   └── resumo_teorico.docx      ← Resumo teórico (DTFT, DFT, FFT, Z, aliasing, janelamento)

 simulacoes/
   ├── questao_01.m             ← Senoide discreta + FFT (f₀=0,1 / N=128)
   ├── questao_02.m             ← Soma de duas senoides e espectro composto
   ├── questao_03.m             ← Aliasing por redução da taxa de amostragem
   ├── questao_04.m             ← Janelamento: Retangular vs Hamming
   ├── questao_05.m             ← Senoide + ruído aditivo (SNR = 5 dB)
   ├── questao_06.m             ← DFT direta (definição) vs fft()
   ├── questao_07.m             ← Resposta ao impulso H(z) = 1/(1−0,8z⁻¹)
   ├── questao_08.m             ← Resolução espectral
   ├── questao_09.m             ← harmônicos
   ├── questao_10.m             ← vibração simulada
   └── discussao_tecnica.pdf           ←  discussao sobre as simulações e seus resultados

 resultados/
   └── *.png                    ← Gráficos gerados pelas simulações
```

---

## Conteúdos Abordados

| Tópico | Questões |
|--------|----------|
| FFT e espectro de magnitude | Q1, Q2, Q6 |
| Aliasing | Q3 |
| Janelamento (Hamming/Hann) | Q4 |
| Análise com ruído | Q5 |
| Transformada-Z / Estabilidade | Q7 |
| Resolução espectral | Q8 |
| Harmônicos e diagnóstico | Q9 |
| Sinal real simulado | Q10 |



---

## Problema Norteador (PBL)

> *Como identificar, a partir do conteúdo espectral de um sinal real, informações relevantes sobre o comportamento dinâmico de um sistema físico e quais limitações práticas devem ser consideradas durante a aquisição e análise desses dados?*

A Questão 10 aborda diretamente esse problema, simulando a análise espectral de um sinal de vibração de máquina rotativa com componente de falha em rolamento (175 Hz) sobreposta à frequência de rotação (50 Hz) e ruído.

---

## Referências

- OPPENHEIM, A. V.; SCHAFER, R. W. *Discrete-Time Signal Processing*. 3. ed. Pearson, 2010.  
- PROAKIS, J. G.; MANOLAKIS, D. G. *Digital Signal Processing*. 4. ed. Pearson, 2007.  
- LATHI, B. P. *Modern Digital and Analog Communication Systems*. 4. ed. Oxford, 2009.
