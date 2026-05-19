% =========================================================
% PDS - Estudo Dirigido Parte 3 - Questão 07
% Resposta ao Impulso  H(z) = 1 / (1 - 0.8 z^{-1})
% =========================================================

clear; clc; close all;

% Coeficientes do filtro IIR:  y[n] = 0.8*y[n-1] + x[n]
b = [1];       % numerador
a = [1, -0.8]; % denominador

N = 60;        % duração da resposta ao impulso
h = impz(b, a, N);   % ou: filter(b,a,[1, zeros(1,N-1)])

% Verificação de estabilidade: polo em z = 0.8  (|polo| < 1 → ESTÁVEL)
polo = roots(a);
fprintf('Polo do sistema: z = %.2f   |polo| = %.2f  → %s\n', ...
        polo, abs(polo), ternary(abs(polo)<1,'ESTÁVEL','INSTÁVEL'));

% Decaimento exponencial esperado: h[n] = 0.8^n * u[n]
n   = 0:N-1;
h_teorico = 0.8.^n;

figure('Name','Questão 7 – Resposta ao Impulso','Position',[100 100 800 450]);
stem(n, h, 'b', 'MarkerSize', 4, 'DisplayName','impz()'); hold on;
plot(n, h_teorico, 'r--', 'DisplayName','0.8^n (teórico)');
xlabel('Amostras (n)'); ylabel('h[n]');
title('Resposta ao Impulso  –  H(z) = 1/(1 – 0.8z^{-1})');
legend; grid on;

saveas(gcf,'../resultados/q07_resposta_impulso.png');

% Função auxiliar (substitui operador ternário do Python)
function r = ternary(cond, a, b)
    if cond; r = a; else; r = b; end
end
