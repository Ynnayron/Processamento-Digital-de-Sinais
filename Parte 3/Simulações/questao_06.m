% =========================================================
% PDS - Estudo Dirigido Parte 3 - Questão 06
% DFT direta (definição) vs. fft() – comparação
% =========================================================

clear; clc; close all;

% Sinal curto para viabilizar DFT direta
N  = 16;
f0 = 0.1;
n  = 0:N-1;
x  = sin(2*pi*f0*n) + 0.5*cos(2*pi*0.25*n);

% ---- DFT via definição: X[k] = sum_{n=0}^{N-1} x[n] * e^{-j2pi*k*n/N} ----
X_dft = zeros(1, N);
for k = 0:N-1
    for m = 0:N-1
        X_dft(k+1) = X_dft(k+1) + x(m+1) * exp(-1j*2*pi*k*m/N);
    end
end

% ---- FFT da biblioteca ----
X_fft = fft(x, N);

% Diferença máxima (deve ser ~eps de máquina)
err = max(abs(X_dft - X_fft));
fprintf('Erro máximo entre DFT direta e fft(): %.2e\n', err);

% Custo computacional teórico
ops_dft = N^2;
ops_fft = N * log2(N);
fprintf('Operações DFT direta: %d  |  FFT (O(N log N)): %.1f\n', ops_dft, ops_fft);

% ---- Plot ----
figure('Name','Questão 6 – DFT vs FFT','Position',[100 100 900 500]);
k = 0:N-1;

subplot(2,1,1);
stem(k, abs(X_dft), 'bo', 'MarkerSize', 6, 'DisplayName','DFT direta');
hold on;
stem(k, abs(X_fft), 'r+', 'MarkerSize', 6, 'DisplayName','fft()');
xlabel('Índice k'); ylabel('|X[k]|');
title(sprintf('Comparação DFT direta × fft()  –  Erro máx: %.1e', err));
legend; grid on;

subplot(2,1,2);
categories = {'DFT direta (N^2)', 'FFT (N log_2 N)'};
ops = [ops_dft, ops_fft];
bar(ops, 'FaceColor', [0.3 0.6 0.9]);
set(gca,'XTickLabel', categories);
ylabel('Número de operações');
title(sprintf('Custo Computacional  (N = %d)', N));
grid on;

saveas(gcf,'../resultados/q06_dft_vs_fft.png');
