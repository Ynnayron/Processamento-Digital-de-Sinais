% =========================================================
% PDS - Estudo Dirigido Parte 3 - Questão 01
% Senoide discreta com FFT
% =========================================================

clear; clc; close all;

N  = 128;          % número de amostras
f0 = 0.1;          % frequência normalizada

% Geração da senoide discreta
n = 0:N-1;
x = sin(2*pi*f0*n);

% Cálculo da FFT
X = fft(x, N);
X_mag = abs(X) / N;                  % magnitude normalizada

% Eixo de frequência normalizada [0, 1)
f = (0:N-1) / N;

% --- Plot ---
figure('Name','Questão 1 – Senoide e FFT','Position',[100 100 900 500]);

subplot(2,1,1);
stem(n, x, 'b', 'MarkerSize', 3);
xlabel('Amostras (n)'); ylabel('Amplitude');
title('Sinal no Domínio do Tempo  (f_0 = 0.1, N = 128)');
grid on;

subplot(2,1,2);
stem(f, X_mag, 'r', 'MarkerSize', 3);
xlabel('Frequência Normalizada (ciclos/amostra)');
ylabel('|X(f)| / N');
title('Espectro de Magnitude via FFT');
xline(f0, '--k', sprintf('f_0 = %.1f', f0), 'LabelVerticalAlignment','bottom');
xlim([0 0.5]); grid on;

% Identificação do pico
[pk, idx] = max(X_mag(1:N/2));
fprintf('Frequência dominante detectada: f = %.4f (pico em índice %d)\n', f(idx), idx-1);
