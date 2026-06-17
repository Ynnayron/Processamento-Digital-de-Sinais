# Resumo Teórico — Filtros Digitais

**Disciplina:** Processamento Digital de Sinais
**Estudo Dirigido — Parte 4**

## Conceito de filtro digital

Um filtro digital é um sistema que opera sobre uma sequência numérica (o sinal amostrado) para modificar seletivamente seu conteúdo espectral, reforçando certas faixas de frequência e atenuando outras. Diferentemente de um filtro analógico, construído com componentes físicos como resistores e capacitores, o filtro digital existe como um algoritmo: uma equação que combina amostras presentes e passadas da entrada (e, em alguns casos, saídas passadas) por meio de somas, multiplicações e atrasos. Essa natureza matemática traz vantagens como repetibilidade exata de comportamento, ausência de deriva por envelhecimento de componentes e a possibilidade de alterar características apenas mudando coeficientes em software.

## Diferenças entre filtros FIR e IIR

A distinção central está em como a saída atual é calculada. Um filtro **FIR** (Finite Impulse Response) gera a saída combinando apenas um número finito de amostras de entrada — não há realimentação. Por isso sua resposta ao impulso tem duração finita: após um número definido de amostras, ela se anula. Um filtro **IIR** (Infinite Impulse Response) usa realimentação, ou seja, a saída também depende de saídas anteriores, fazendo com que a resposta ao impulso, em princípio, nunca chegue exatamente a zero.

Essa diferença traz consequências práticas: filtros FIR são inerentemente estáveis, pois não têm polos fora da origem do plano z, e podem ter fase exatamente linear quando os coeficientes são simétricos, preservando a forma de onda. Em troca, costumam exigir ordem mais alta para atingir seletividade comparável a um IIR. Os filtros IIR, por usarem realimentação, alcançam respostas mais seletivas com poucos coeficientes (menor custo computacional), mas pagam o preço de fase tipicamente não linear e da necessidade de verificar a estabilidade do projeto.

Uma analogia útil: um FIR se comporta como um eco que desaparece sozinho após um intervalo fixo, enquanto um IIR se comporta como uma corda que continua vibrando por realimentação — vibração que pode se extinguir gradualmente (estável) ou crescer sem controle se o projeto não for adequado (instável).

## Resposta em frequência

A resposta em frequência descreve, para cada frequência, o quanto o filtro amplifica ou atenua uma componente senoidal e qual deslocamento de fase introduz. Se aplicarmos uma senoide pura na entrada de um sistema LTI, após o transitório a saída será uma senoide de mesma frequência, com amplitude escalada e fase deslocada conforme a resposta em frequência naquele ponto. Essa propriedade define a banda de passagem (ganho próximo de 1), a banda de rejeição (forte atenuação) e a banda de transição entre elas — é essa curva que mostra, por exemplo, se um passa-baixa está realmente eliminando as componentes de alta frequência indesejadas sem afetar as de interesse.

## Resposta de fase

Enquanto a magnitude informa o quanto cada frequência é atenuada, a fase informa o quanto cada componente é deslocada no tempo. Como um sinal real geralmente combina várias frequências, se cada uma for deslocada por um tempo diferente, a forma de onda se distorce mesmo sem nenhuma atenuação. Quando a fase varia linearmente com a frequência, todas as componentes são atrasadas pelo mesmo intervalo, preservando a forma do sinal. Filtros de fase não linear, comuns entre os IIR, podem distorcer transientes em áudio ou espalhar pulsos em sistemas digitais.

## Atraso de grupo

O atraso de grupo é a derivada da fase em relação à frequência (com sinal negativo) e representa o tempo que o envelope de um grupo estreito de frequências leva para atravessar o filtro. Em fase linear, o atraso de grupo é constante para todas as frequências — o sinal apenas é retardado, sem deformação. Em filtros IIR, o atraso de grupo costuma variar com a frequência, fazendo diferentes componentes chegarem em instantes distintos. Esse efeito é crítico em comunicação digital, onde atraso de grupo não uniforme pode causar interferência entre símbolos consecutivos.

## Estabilidade de filtros digitais

Um sistema é estável (no sentido BIBO) quando todos os polos de H(z) estão dentro do círculo unitário do plano z. Filtros FIR não têm realimentação, logo seus polos ficam todos na origem — incondicionalmente estáveis. Filtros IIR têm polos definidos pelos coeficientes de realimentação; um projeto mal ajustado pode posicionar um polo fora do círculo unitário, levando a saída a crescer indefinidamente, de forma análoga a um sistema de áudio em realimentação positiva que produz um apito crescente. Por isso a análise de polos e zeros é etapa obrigatória no projeto de qualquer IIR.

## Aplicações práticas

Filtros digitais aparecem em praticamente toda aplicação que envolve sinais. Em sistemas embarcados, filtros passa-baixa suavizam leituras ruidosas de acelerômetros e sensores de vibração. Em áudio, equalizam faixas de frequência e removem ruído de fundo. Em telecomunicações, filtros passa-faixa selecionam o canal de interesse antes da demodulação. No monitoramento industrial, filtros notch eliminam a interferência da rede elétrica (50/60 Hz) sobre sinais de instrumentação. Em TinyML, a filtragem digital costuma servir como pré-processamento, reduzindo ruído e simplificando o sinal antes de alimentar um modelo embarcado, diminuindo o custo computacional da inferência.
