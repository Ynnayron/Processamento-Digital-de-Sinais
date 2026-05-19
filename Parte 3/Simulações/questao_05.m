% =========================================================
% PDS - Estudo Dirigido Parte 3 - Questão 05
% Senoide + Ruído Aditivo – Análise Espectral
% =========================================================

clear; clc; close all;
rng(42);           % semente para reprodutibilidade

N  = 256;
f0 = 0.15;
n  = 0:N-1;
SNR_dB = 5;        % baixo SNR para dificultar identificação visual

sinal  = sin(2*pi*f0*n);
ruido  = randn(1, N) * 10^(-SNR_dB/20);
x_ruid = sinal + ruido;

% FFT
f_ax  = (0:N-1) / N;
X_s   = abs(fft(sinal,  N)) / N;
X_r   = abs(fft(x_ruid, N)) / N;

% --- Plot ---
figure('Name','Questão 5 – Sinal + Ruído','Position',[100 100 950 650]);

subplot(2,2,1);
plot(n, sinal, 'b'); xlabel('n'); ylabel('s(n)');
title('Sinal puro'); grid on;

subplot(2,2,2);
plot(n, x_ruid, 'r'); xlabel('n'); ylabel('x(n)');
title(sprintf('Sinal + Ruído  (SNR = %d dB)', SNR_dB)); grid on;

subplot(2,2,3);
stem(f_ax, X_s, 'b', 'MarkerSize', 3); xlim([0 0.5]);
xlabel('Freq. Normalizada'); ylabel('Magnitude');
title('Espectro – sinal puro'); grid on;

subplot(2,2,4);
stem(f_ax, X_r, 'r', 'MarkerSize', 3); xlim([0 0.5]);
xlabel('Freq. Normalizada'); ylabel('Magnitude');
title('Espectro – sinal ruidoso  (pico ainda identificável)');
xline(f0,'--k',sprintf('f_0=%.2f',f0),'LabelVerticalAlignment','bottom'); grid on;

saveas(gcf,'../resultados/q05_ruido.png');
