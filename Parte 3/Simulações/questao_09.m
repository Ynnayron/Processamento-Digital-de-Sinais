
% =========================================================
% Questão 09 – Componente Harmônica e Diagnóstico de Vibração
% =========================================================


clear; clc; close all;

N   = 512;
f1  = 0.05;          % frequência fundamental
f2  = 2*f1;          % 2º harmônico
f3  = 3*f1;          % 3º harmônico

n   = 0:N-1;
x   = sin(2*pi*f1*n) + 0.5*sin(2*pi*f2*n) + 0.25*sin(2*pi*f3*n);

X     = abs(fft(x, N)) / N;
f_ax  = (0:N-1) / N;

figure('Name','Questão 9 – Harmônicos','Position',[100 100 900 500]);

subplot(2,1,1);
plot(n, x, 'k'); xlabel('n'); ylabel('x(n)');
title('Sinal com Fundamental + Harmônicos'); grid on;

subplot(2,1,2);
stem(f_ax, X, 'b', 'MarkerSize', 3); xlim([0 0.35]); grid on;
xlabel('Freq. Normalizada'); ylabel('|X[k]|/N');
title('Espectro – identificação de harmônicos');
for fi = [f1, f2, f3]
    xline(fi,'--r',sprintf('f=%.2f',fi),'LabelVerticalAlignment','bottom');
end