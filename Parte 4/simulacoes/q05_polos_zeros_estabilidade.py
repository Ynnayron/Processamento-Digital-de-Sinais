"""
Questao 5 - Polos e zeros de um filtro IIR e relacao com a estabilidade

"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.signal import butter, tf2zpk

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "resultados")
os.makedirs(OUT_DIR, exist_ok=True)

fs = 1000.0
fc = 30.0

# Filtro estavel: Butterworth ordem 4 corretamente projetado
b_estavel, a_estavel = butter(4, fc, fs=fs)
zeros_e, polos_e, _ = tf2zpk(b_estavel, a_estavel)

# Filtro instavel
a_instavel = a_estavel.copy()
a_instavel[1] *= 1.6   # altera o coeficiente de realimentacao
zeros_i, polos_i, _ = tf2zpk(b_estavel, a_instavel)


def plota_zplane(ax, zeros, polos, titulo):
    theta = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(theta), np.sin(theta), color="gray", linestyle="--", linewidth=1)
    ax.scatter(zeros.real, zeros.imag, marker="o", facecolors="none",
               edgecolors="tab:blue", s=80, label="zeros")
    ax.scatter(polos.real, polos.imag, marker="x", color="tab:red", s=80, label="polos")
    ax.axhline(0, color="black", linewidth=0.5)
    ax.axvline(0, color="black", linewidth=0.5)
    limite = max(1.8, 1.2 * np.max(np.abs(np.concatenate([zeros, polos, [1]]))))
    ax.set_xlim(-limite, limite)
    ax.set_ylim(-limite, limite)
    ax.set_aspect("equal")
    ax.set_title(titulo)
    ax.legend(loc="upper right")


fig, axs = plt.subplots(1, 2, figsize=(11, 5.5))
plota_zplane(axs[0], zeros_e, polos_e, "Filtro estavel\n(todos os polos dentro do circulo)")
plota_zplane(axs[1], zeros_i, polos_i, "Filtro instavel\n(ha polo fora do circulo)")
fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "q05_polos_zeros_estabilidade.png"), dpi=150)
plt.close(fig)

print("Questao 5 - Polos, zeros e estabilidade")
print("Filtro estavel - |polos| =", np.round(np.abs(polos_e), 4))
print("Filtro instavel - |polos| =", np.round(np.abs(polos_i), 4))
print("Estavel  -> todos |polo| < 1 ? ", np.all(np.abs(polos_e) < 1))
print("Instavel -> todos |polo| < 1 ? ", np.all(np.abs(polos_i) < 1))
print(f"Grafico salvo em: {OUT_DIR}/q05_polos_zeros_estabilidade.png")
