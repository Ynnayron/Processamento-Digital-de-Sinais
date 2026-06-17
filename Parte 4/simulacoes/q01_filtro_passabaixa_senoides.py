"""
Questao 1 - Filtro passa-baixa aplicado a um sinal com duas senoides

"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "resultados")
os.makedirs(OUT_DIR, exist_ok=True)

# --- 1. Geracao do sinal: duas senoides (5 Hz e 80 Hz) ---
fs = 1000.0                      # frequencia de amostragem (Hz)
T = 1.0                          # duracao (s)
t = np.arange(0, T, 1 / fs)

f_baixa = 5.0                    # componente de baixa frequencia (deve passar)
f_alta = 80.0                    # componente de alta frequencia (deve ser removida)

sinal = np.sin(2 * np.pi * f_baixa * t) + 0.8 * np.sin(2 * np.pi * f_alta * t)

# --- 2. Projeto do filtro FIR passa-baixa (janela de Hamming) ---
ordem = 101
fc = 20.0                        # frequencia de corte (Hz)
coef = firwin(ordem, fc, fs=fs)  # coeficientes do filtro FIR

sinal_filtrado = lfilter(coef, 1.0, sinal)

# --- 3. Analise no dominio da frequencia (FFT) ---
N = len(sinal)
freqs = np.fft.rfftfreq(N, d=1 / fs)
espectro_original = np.abs(np.fft.rfft(sinal)) / N
espectro_filtrado = np.abs(np.fft.rfft(sinal_filtrado)) / N

# --- 4. Graficos ---
fig, axs = plt.subplots(2, 2, figsize=(11, 7))

axs[0, 0].plot(t, sinal, color="tab:blue")
axs[0, 0].set_title("Sinal original (5 Hz + 80 Hz)")
axs[0, 0].set_xlabel("Tempo (s)")
axs[0, 0].set_ylabel("Amplitude")
axs[0, 0].set_xlim(0, 0.3)

axs[0, 1].plot(t, sinal_filtrado, color="tab:orange")
axs[0, 1].set_title("Sinal apos filtro passa-baixa (fc = 20 Hz)")
axs[0, 1].set_xlabel("Tempo (s)")
axs[0, 1].set_ylabel("Amplitude")
axs[0, 1].set_xlim(0, 0.3)

axs[1, 0].plot(freqs, espectro_original, color="tab:blue")
axs[1, 0].set_title("Espectro do sinal original")
axs[1, 0].set_xlabel("Frequencia (Hz)")
axs[1, 0].set_ylabel("|X(f)|")
axs[1, 0].set_xlim(0, 150)
axs[1, 0].axvline(fc, color="gray", linestyle="--", linewidth=1)

axs[1, 1].plot(freqs, espectro_filtrado, color="tab:orange")
axs[1, 1].set_title("Espectro do sinal filtrado")
axs[1, 1].set_xlabel("Frequencia (Hz)")
axs[1, 1].set_ylabel("|X(f)|")
axs[1, 1].set_xlim(0, 150)
axs[1, 1].axvline(fc, color="gray", linestyle="--", linewidth=1)

fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "q01_filtro_passabaixa_senoides.png"), dpi=150)
plt.close(fig)

# --- 5. Resultados numericos para o relatorio ---
amp_baixa_antes = espectro_original[np.argmin(np.abs(freqs - f_baixa))]
amp_alta_antes = espectro_original[np.argmin(np.abs(freqs - f_alta))]
amp_baixa_depois = espectro_filtrado[np.argmin(np.abs(freqs - f_baixa))]
amp_alta_depois = espectro_filtrado[np.argmin(np.abs(freqs - f_alta))]

print("Questao 1 - Filtro passa-baixa (duas senoides)")
print(f"Componente {f_baixa} Hz: antes={amp_baixa_antes:.4f}  depois={amp_baixa_depois:.4f}")
print(f"Componente {f_alta} Hz: antes={amp_alta_antes:.4f}  depois={amp_alta_depois:.4f}")
print(f"Atenuacao da componente de {f_alta} Hz: {20*np.log10(amp_alta_depois/amp_alta_antes):.1f} dB")
print(f"Grafico salvo em: {OUT_DIR}/q01_filtro_passabaixa_senoides.png")
