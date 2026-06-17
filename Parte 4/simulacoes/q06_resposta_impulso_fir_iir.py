"""
Questao 6 - Resposta ao impulso: FIR vs IIR

"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.signal import firwin, butter, lfilter

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "resultados")
os.makedirs(OUT_DIR, exist_ok=True)

fs = 1000.0
fc = 30.0
N = 300  # numero de amostras observadas

impulso = np.zeros(N)
impulso[0] = 1.0

# FIR: ordem 41 -> resposta ao impulso e exatamente igual aos coeficientes
ordem_fir = 41
coef_fir = firwin(ordem_fir, fc, fs=fs)
h_fir = lfilter(coef_fir, 1.0, impulso)

# IIR Butterworth ordem 4
b_iir, a_iir = butter(4, fc, fs=fs)
h_iir = lfilter(b_iir, a_iir, impulso)

fig, axs = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

axs[0].stem(np.arange(N), h_fir, basefmt=" ", linefmt="tab:blue", markerfmt="")
axs[0].set_title(f"Resposta ao impulso - FIR (ordem {ordem_fir})")
axs[0].set_ylabel("h[n]")
axs[0].axvline(ordem_fir - 1, color="gray", linestyle="--", linewidth=1)
axs[0].text(ordem_fir + 5, max(h_fir) * 0.7, "h[n] = 0\npara n >= ordem", fontsize=9)

axs[1].stem(np.arange(N), h_iir, basefmt=" ", linefmt="tab:red", markerfmt="")
axs[1].set_title("Resposta ao impulso - IIR Butterworth (ordem 4)")
axs[1].set_xlabel("Amostra (n)")
axs[1].set_ylabel("h[n]")

fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "q06_resposta_impulso_fir_iir.png"), dpi=150)
plt.close(fig)

amostra_residual = np.argmax(np.abs(h_iir[200:]) < 1e-6) + 200 if np.any(np.abs(h_iir[200:]) < 1e-6) else None
print("Questao 6 - Resposta ao impulso FIR vs IIR")
print(f"FIR: h[n] e identico aos {ordem_fir} coeficientes do filtro; para n >= {ordem_fir}, h[n] = 0 EXATAMENTE")
print(f"     (nao ha realimentacao, entao a saida so pode depender das ultimas {ordem_fir} entradas)")
print(f"IIR: amplitude de h[n] na amostra 250: {h_iir[250]:.2e} (ainda diferente de zero)")
print(f"     amplitude de h[n] na amostra 299: {h_iir[299]:.2e}")
print("     a saida realimenta a propria saida anterior, entao o efeito do impulso")
print("     nunca se anula matematicamente, apenas decai geometricamente (~ |polo|^n)")
print(f"Grafico salvo em: {OUT_DIR}/q06_resposta_impulso_fir_iir.png")
