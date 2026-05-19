% =========================================================
% PDS - Estudo Dirigido Parte 3 - Questão 04
% Janelamento – Hamming vs Retangular
% =========================================================

clear; clc; close all;

N  = 64;
f0 = 0.1;
n  = 0:N-1;
x  = sin(2*pi*f0*n);

% Sem janela (janela retangular implícita)
X_rect = abs(fft(x, N)) / N;

% Com janela de Hamming
w_hamm = hamming(N)';
X_hamm = abs(fft(x .* w_hamm, N)) / N;

% Eixo frequência
f = (0:N-1) / N;

% --- Plot ---
figure('Name','Questão 4 – Janelamento','Position',[100 100 950 600]);

subplot(3,1,1);
plot(n, x, 'k'); hold on;
plot(n, w_hamm .* max(abs(x)), 'r--', 'DisplayName','Janela Hamming (escalada)');
xlabel('n'); ylabel('Amplitude');
title('Sinal Original e Janela de Hamming');
legend; grid on;

subplot(3,1,2);
stem(f, X_rect, 'b', 'MarkerSize', 3);
xlabel('Freq. Normalizada'); ylabel('Magnitude');
title('Espectro SEM janela (Retangular)  – vazamento espectral visível');
xlim([0 0.5]); grid on;

subplot(3,1,3);
stem(f, X_hamm, 'r', 'MarkerSize', 3);
xlabel('Freq. Normalizada'); ylabel('Magnitude');
title('Espectro COM janela de Hamming  – lóbulos laterais reduzidos');
xlim([0 0.5]); grid on;

saveas(gcf,'../resultados/q04_janelamento.png');
