% =========================================================
% PDS - Estudo Dirigido Parte 3 - Questão 02
% Soma de duas senoides e análise espectral
% =========================================================

clear; clc; close all;

N  = 256;
f1 = 0.1;    % 1ª frequência normalizada
f2 = 0.3;    % 2ª frequência normalizada

n = 0:N-1;
x1 = sin(2*pi*f1*n);
x2 = sin(2*pi*f2*n);
x  = x1 + x2;        % sinal composto

% FFT
X     = fft(x, N);
X_mag = abs(X) / N;
f     = (0:N-1) / N;

% --- Plot ---
figure('Name','Questão 2 – Duas Senoides','Position',[100 100 950 600]);

subplot(3,1,1);
plot(n, x1, 'b'); xlabel('n'); ylabel('x_1(n)');
title(sprintf('Senoide 1  –  f_1 = %.1f', f1)); grid on;

subplot(3,1,2);
plot(n, x2, 'r'); xlabel('n'); ylabel('x_2(n)');
title(sprintf('Senoide 2  –  f_2 = %.1f', f2)); grid on;

subplot(3,1,3);
stem(f, X_mag, 'k', 'MarkerSize', 3);
xlabel('Frequência Normalizada');  ylabel('|X(f)| / N');
title('Espectro FFT do Sinal Composto');
xline(f1,'--b', sprintf('f_1=%.1f',f1),'LabelVerticalAlignment','bottom');
xline(f2,'--r', sprintf('f_2=%.1f',f2),'LabelVerticalAlignment','bottom');
xlim([0 0.5]); grid on;

saveas(gcf,'../resultados/q02_duas_senoides.png');
