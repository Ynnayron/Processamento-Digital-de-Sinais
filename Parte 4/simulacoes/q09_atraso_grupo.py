"""
Questao 9 - Atraso de grupo: calculo e comparacao entre filtros

"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.signal import firwin, butter, group_delay

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "resultados")
os.makedirs(OUT_DIR, exist_ok=True)

fs = 1000.0
fc = 30.0

coef_fir = firwin(61, fc, fs=fs)
b_iir, a_iir = butter(4, fc, fs=fs)

w_fir, gd_fir = group_delay((coef_fir, 1.0), w=4000, fs=fs)
w_iir, gd_iir = group_delay((b_iir, a_iir), w=4000, fs=fs)

# atraso de grupo teorico do FIR de fase linear: (ordem-1)/2 amostras
atraso_teorico_fir = (len(coef_fir) - 1) / 2

fig, ax = plt.subplots(figsize=(9, 5.5))
ax.plot(w_fir, gd_fir, label="FIR (ordem 61) - atraso constante", color="tab:blue")
ax.plot(w_iir, gd_iir, label="IIR Butterworth (ordem 4) - atraso variavel", color="tab:red")
ax.axvline(fc, color="gray", linestyle="--", linewidth=1)
ax.set_xlim(0, 150)
ax.set_ylim(0, max(gd_iir[w_iir <= 150].max(), atraso_teorico_fir) * 1.2)
ax.set_xlabel("Frequencia (Hz)")
ax.set_ylabel("Atraso de grupo (amostras)")
ax.set_title("Atraso de grupo: FIR vs IIR")
ax.legend()
fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "q09_atraso_grupo.png"), dpi=150)
plt.close(fig)

faixa_passagem = w_iir <= fc
print("Questao 9 - Atraso de grupo")
print(f"FIR: atraso de grupo teorico = (ordem-1)/2 = {atraso_teorico_fir:.1f} amostras "
      f"({atraso_teorico_fir/fs*1000:.2f} ms) -- constante em toda a faixa")
print(f"FIR: atraso medido min={gd_fir[faixa_passagem].min():.2f}  "
      f"max={gd_fir[faixa_passagem].max():.2f} amostras (praticamente igual ao teorico)")
print(f"IIR: atraso de grupo na banda de passagem varia de "
      f"{gd_iir[faixa_passagem].min():.2f} a {gd_iir[faixa_passagem].max():.2f} amostras")
print("Importancia: em sistemas de comunicacao digital, se diferentes componentes")
print("de frequencia de um simbolo chegam com atrasos distintos, ocorre interferencia")
print("entre simbolos vizinhos (ISI), degradando a taxa de erro de bit (BER).")
print(f"Grafico salvo em: {OUT_DIR}/q09_atraso_grupo.png")
