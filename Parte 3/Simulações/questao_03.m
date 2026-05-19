% =========================================================
% PDS - Estudo Dirigido Parte 3 - Questão 03
% Aliasing por redução da taxa de amostragem
% =========================================================

clear; clc; close all;

% Sinal analógico de referência
fa   = 1000;      % frequência do sinal (Hz)
fs1  = 8000;      % taxa adequada  (8× fa)
fs2  = 1500;      % taxa inadequada – abaixo de 2*fa (aliasing!)

dur  = 0.05;      % duração em segundos

% --- Amostragem adequada ---
t1 = 0 : 1/fs1 : dur;
x1 = sin(2*pi*fa*t1);
N1 = length(t1);
X1 = abs(fft(x1, N1)) / N1;
f1_axis = (0:N1-1) * fs1 / N1;

% --- Amostragem insuficiente ---
t2 = 0 : 1/fs2 : dur;
x2 = sin(2*pi*fa*t2);
N2 = length(t2);
X2 = abs(fft(x2, N2)) / N2;
f2_axis = (0:N2-1) * fs2 / N2;

% Frequência de aliasing esperada: |fa - fs2| = |1000 - 1500| = 500 Hz
f_alias = abs(fa - fs2);
fprintf('Frequência de aliasing esperada: %d Hz\n', f_alias);

% --- Plot ---
figure('Name','Questão 3 – Aliasing','Position',[100 100 950 600]);

subplot(2,2,1);
stem(t1*1e3, x1, 'b', 'MarkerSize', 2);
xlabel('Tempo (ms)'); ylabel('Amplitude');
title(sprintf('Tempo – fs = %d Hz (adequada)', fs1)); grid on;

subplot(2,2,2);
plot(f1_axis(1:N1/2), X1(1:N1/2), 'b');
xlabel('Frequência (Hz)'); ylabel('|X(f)|/N');
title('Espectro – fs adequada');
xline(fa,'--k',sprintf('%d Hz',fa)); xlim([0 fs1/2]); grid on;

subplot(2,2,3);
stem(t2*1e3, x2, 'r', 'MarkerSize', 3);
xlabel('Tempo (ms)'); ylabel('Amplitude');
title(sprintf('Tempo – fs = %d Hz (insuficiente)', fs2)); grid on;

subplot(2,2,4);
plot(f2_axis(1:N2/2), X2(1:N2/2), 'r');
xlabel('Frequência (Hz)'); ylabel('|X(f)|/N');
title('Espectro – aliasing visível');
xline(f_alias,'--k',sprintf('alias=%d Hz',f_alias)); xlim([0 fs2/2]); grid on;

