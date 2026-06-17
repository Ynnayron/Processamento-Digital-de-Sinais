"""
Questao 7 - Filtro passa-faixa para selecionar uma frequencia especifica
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "resultados")
os.makedirs(OUT_DIR, exist_ok=True)

fs = 1000.0
T = 1.0
t = np.arange(0, T, 1 / fs)

# Sinal composto por tres frequencias; queremos isolar a de 60 Hz
f1, f2, f3 = 10.0, 60.0, 150.0
sinal = (np.sin(2 * np.pi * f1 * t)
         + np.sin(2 * np.pi * f2 * t)
         + np.sin(2 * np.pi * f3 * t))

# Filtro passa-faixa Butterworth (banda 45-75 Hz, centrada em 60 Hz)
banda = [45.0, 75.0]
b, a = butter(4, banda, btype="bandpass", fs=fs)
sinal_filtrado = lfilter(b, a, sinal)

N = len(sinal)
freqs = np.fft.rfftfreq(N, d=1 / fs)
espectro_antes = np.abs(np.fft.rfft(sinal)) / N
espectro_depois = np.abs(np.fft.rfft(sinal_filtrado)) / N

fig, axs = plt.subplots(2, 2, figsize=(11, 7))

axs[0, 0].plot(t, sinal, color="tab:blue")
axs[0, 0].set_title("Sinal original (10 + 60 + 150 Hz)")
axs[0, 0].set_xlim(0, 0.2)
axs[0, 0].set_xlabel("Tempo (s)")

axs[0, 1].plot(t, sinal_filtrado, color="tab:orange")
axs[0, 1].set_title("Sinal apos filtro passa-faixa (45-75 Hz)")
axs[0, 1].set_xlim(0, 0.2)
axs[0, 1].set_xlabel("Tempo (s)")

axs[1, 0].plot(freqs, espectro_antes, color="tab:blue")
axs[1, 0].set_xlim(0, 200)
axs[1, 0].set_title("Espectro do sinal original")
axs[1, 0].set_xlabel("Frequencia (Hz)")
for f in (f1, f2, f3):
    axs[1, 0].axvline(f, color="gray", linestyle=":", linewidth=1)

axs[1, 1].plot(freqs, espectro_depois, color="tab:orange")
axs[1, 1].set_xlim(0, 200)
axs[1, 1].set_title("Espectro do sinal filtrado")
axs[1, 1].set_xlabel("Frequencia (Hz)")
for f in (f1, f2, f3):
    axs[1, 1].axvline(f, color="gray", linestyle=":", linewidth=1)

fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "q07_filtro_passafaixa.png"), dpi=150)
plt.close(fig)

def amp_em(freqs, espectro, f0):
    return espectro[np.argmin(np.abs(freqs - f0))]

print("Questao 7 - Filtro passa-faixa (isolando 60 Hz)")
for f in (f1, f2, f3):
    a_antes = amp_em(freqs, espectro_antes, f)
    a_depois = amp_em(freqs, espectro_depois, f)
    print(f"  {f:>5.0f} Hz: antes={a_antes:.3f}  depois={a_depois:.3f}  "
          f"atenuacao={20*np.log10((a_depois+1e-12)/(a_antes+1e-12)):.1f} dB")
print(f"Grafico salvo em: {OUT_DIR}/q07_filtro_passafaixa.png")
