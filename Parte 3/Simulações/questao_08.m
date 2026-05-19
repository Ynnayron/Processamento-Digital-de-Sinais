% =========================================================
% PDS - Estudo Dirigido Parte 3 - Questão 08
% Resolução Espectral × Número de Amostras
% =========================================================

clear; clc; close all;

f0   = 0.1;
Ns   = [32, 128, 512];   % tamanhos de janela
cols = {'b','r','g'};

figure('Name','Questão 8 – Resolução Espectral','Position',[100 100 900 600]);

for i = 1:3
    N = Ns(i);
    n = 0:N-1;
    x = sin(2*pi*f0*n);
    X = abs(fft(x, N)) / N;
    f_ax = (0:N-1) / N;

    subplot(3,1,i);
    stem(f_ax, X, cols{i}, 'MarkerSize', 2);
    xlim([0 0.35]); grid on;
    xlabel('Freq. Normalizada'); ylabel('|X[k]|/N');
    title(sprintf('N = %d   –   Resolução = %.4f ciclos/amostra', N, 1/N));
    xline(f0,'--k');
end
sgtitle('Influência de N na Resolução Espectral');
