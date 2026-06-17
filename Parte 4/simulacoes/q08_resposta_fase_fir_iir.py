"""
Questao 8 - Resposta de fase: FIR vs IIR e o conceito de fase linear

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

coef_fir = firwin(61, fc, fs=fs)         # ordem par de coeficientes -> simetria perfeita
b_iir, a_iir = butter(4, fc, fs=fs)

w_fir, h_fir = freqz(coef_fir, 1.0, worN=4000, fs=fs)
w_iir, h_iir = freqz(b_iir, a_iir, worN=4000, fs=fs)

fase_fir = np.unwrap(np.angle(h_fir))
fase_iir = np.unwrap(np.angle(h_iir))

# Verifica a linearidade ajustando uma reta a fase do FIR dentro da faixa de passagem
faixa = w_fir <= fc
coef_ajuste = np.polyfit(w_fir[faixa], fase_fir[faixa], 1)
reta_ajustada = np.polyval(coef_ajuste, w_fir[faixa])
erro_linearidade_fir = np.max(np.abs(fase_fir[faixa] - reta_ajustada))

fig, ax = plt.subplots(figsize=(9, 5.5))
ax.plot(w_fir, fase_fir, label="FIR (ordem 61) - fase linear", color="tab:blue")
ax.plot(w_iir, fase_iir, label="IIR Butterworth (ordem 4) - fase nao linear", color="tab:red")
ax.axvline(fc, color="gray", linestyle="--", linewidth=1)
ax.set_xlim(0, 150)
ax.set_xlabel("Frequencia (Hz)")
ax.set_ylabel("Fase (rad)")
ax.set_title("Resposta de fase: FIR vs IIR")
ax.legend()
fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "q08_resposta_fase_fir_iir.png"), dpi=150)
plt.close(fig)

print("Questao 8 - Resposta de fase: FIR vs IIR")
print(f"FIR: desvio maximo em relacao a uma reta ideal na banda de passagem: {erro_linearidade_fir:.2e} rad")
print("     (praticamente zero -> fase exatamente linear, garantida pela simetria dos coeficientes)")
print("IIR: a fase descreve uma curva, nao uma reta -> fase nao linear")
print("     cada frequencia e atrasada por um tempo diferente (ver atraso de grupo na Questao 9)")
print(f"Grafico salvo em: {OUT_DIR}/q08_resposta_fase_fir_iir.png")
