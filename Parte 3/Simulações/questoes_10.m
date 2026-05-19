
% =========================================================
% Questão 10 – Sinal Real Simulado (vibração com falha)
% =========================================================

clear; clc; close all;
rng(7);

fs    = 1000;     % taxa de amostragem (Hz)
dur   = 1;        % duração (s)
t     = 0:1/fs:dur-1/fs;
N     = length(t);

f_rot = 50;       % frequência de rotação (Hz)
f_fal = 175;      % frequência de falha (rolamento simulado)

% Sinal: rotação + harmônico + falha + ruído
x = 1.0*sin(2*pi*f_rot*t) ...
  + 0.4*sin(2*pi*2*f_rot*t) ...
  + 0.3*sin(2*pi*f_fal*t) ...
  + 0.2*randn(1,N);

X_mag = abs(fft(x, N)) * 2/N;
f_ax  = (0:N/2-1) * fs/N;

figure('Name','Questão 10 – Vibração Simulada','Position',[100 100 950 500]);

subplot(2,1,1);
plot(t, x, 'k'); xlabel('Tempo (s)'); ylabel('Aceleração (u.a.)');
title('Sinal de Vibração Simulada (Domínio do Tempo)'); grid on;

subplot(2,1,2);
plot(f_ax, X_mag(1:N/2), 'b'); xlabel('Frequência (Hz)'); ylabel('Magnitude');
title('Espectro de Amplitude – Diagnóstico de Falha');
xline(f_rot,'--g',sprintf('Rotação %dHz',f_rot));
xline(2*f_rot,'--m',sprintf('2× %dHz',f_rot));
xline(f_fal,'--r',sprintf('Falha %dHz',f_fal));
xlim([0 400]); grid on;

