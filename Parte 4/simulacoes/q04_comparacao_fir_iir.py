"""
Questao 4 - Comparacao das respostas em frequencia: FIR vs IIR

"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.signal import firwin, butter, freqz

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "resultados")
os.makedirs(OUT_DIR, exist_ok=True)

fs = 1000.0
fc = 30.0

# Filtro FIR (janela de Hamming) - ordens diferentes para mostrar o
# compromisso entre ordem e seletividade
fir_baixa_ordem = firwin(21, fc, fs=fs)
fir_alta_ordem = firwin(101, fc, fs=fs)

# Filtro IIR Butterworth, ordem baixa (4) ja alcanca corte comparavel
b_iir, a_iir = butter(4, fc, fs=fs)

w1, h_fir_baixa = freqz(fir_baixa_ordem, 1.0, worN=4000, fs=fs)
w2, h_fir_alta = freqz(fir_alta_ordem, 1.0, worN=4000, fs=fs)
w3, h_iir = freqz(b_iir, a_iir, worN=4000, fs=fs)

fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].plot(w1, 20 * np.log10(np.abs(h_fir_baixa) + 1e-12), label="FIR ordem 21")
axs[0].plot(w2, 20 * np.log10(np.abs(h_fir_alta) + 1e-12), label="FIR ordem 101")
axs[0].plot(w3, 20 * np.log10(np.abs(h_iir) + 1e-12), label="IIR Butterworth ordem 4")
axs[0].axvline(fc, color="gray", linestyle="--", linewidth=1)
axs[0].set_ylim(-100, 5)
axs[0].set_xlim(0, 200)
axs[0].set_xlabel("Frequencia (Hz)")
axs[0].set_ylabel("Magnitude (dB)")
axs[0].set_title("Resposta em magnitude")
axs[0].legend()

axs[1].plot(w1, np.unwrap(np.angle(h_fir_baixa)), label="FIR ordem 21")
axs[1].plot(w2, np.unwrap(np.angle(h_fir_alta)), label="FIR ordem 101")
axs[1].plot(w3, np.unwrap(np.angle(h_iir)), label="IIR Butterworth ordem 4")
axs[1].axvline(fc, color="gray", linestyle="--", linewidth=1)
axs[1].set_xlim(0, 200)
axs[1].set_xlabel("Frequencia (Hz)")
axs[1].set_ylabel("Fase (rad)")
axs[1].set_title("Resposta de fase")
axs[1].legend()

fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "q04_comparacao_fir_iir.png"), dpi=150)
plt.close(fig)

print("Questao 4 - Comparacao FIR vs IIR (mesma frequencia de corte)")
print("FIR ordem 21:  transicao suave (roll-off lento), fase linear (reta)")
print("FIR ordem 101: transicao muito mais abrupta que o de ordem 21, fase")
print("               perfeitamente linear (reta, com saltos de pi nos zeros)")
print("IIR ordem 4:   com apenas 4 polos a queda ja e mais rapida que a do FIR")
print("               de ordem 21 (21 coeficientes) - maior seletividade por")
print("               coeficiente - mas a fase e claramente curva (nao linear)")
print(f"Grafico salvo em: {OUT_DIR}/q04_comparacao_fir_iir.png")
