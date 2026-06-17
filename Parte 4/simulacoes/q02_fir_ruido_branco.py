"""
Questao 2 - Filtro FIR passa-baixa aplicado a um sinal com ruido branco


"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "resultados")
os.makedirs(OUT_DIR, exist_ok=True)


np.random.seed(42)               # reprodutibilidade (usado tambem na Questao 3)
fs = 1000.0
T = 1.0
t = np.arange(0, T, 1 / fs)

f0 = 10.0                                  # frequencia do sinal de interesse
sinal_limpo = np.sin(2 * np.pi * f0 * t)
ruido = np.random.normal(0, 0.5, size=t.shape)
sinal_ruidoso = sinal_limpo + ruido


ordem = 101
fc = 30.0
coef_fir = firwin(ordem, fc, fs=fs)
sinal_filtrado_fir = lfilter(coef_fir, 1.0, sinal_ruidoso)

# compensa o atraso de grupo do FIR (ordem-1)/2 amostras para comparacao justa
atraso = (ordem - 1) // 2
sinal_filtrado_fir_alinhado = sinal_filtrado_fir[atraso:]
sinal_limpo_alinhado = sinal_limpo[: len(sinal_filtrado_fir_alinhado)]

# --- 3. Metricas de qualidade (SNR) ---
def snr_db(sinal_ref, sinal_com_erro):
    erro = sinal_ref - sinal_com_erro
    return 10 * np.log10(np.sum(sinal_ref ** 2) / np.sum(erro ** 2))

snr_antes = snr_db(sinal_limpo, sinal_ruidoso)
snr_depois_fir = snr_db(sinal_limpo_alinhado, sinal_filtrado_fir_alinhado)

fig, axs = plt.subplots(2, 1, figsize=(10, 7))

axs[0].plot(t, sinal_ruidoso, color="tab:gray", label="Sinal com ruido", linewidth=0.8)
axs[0].plot(t, sinal_limpo, color="tab:green", label="Sinal limpo (referencia)", linewidth=1.5)
axs[0].set_title(f"Sinal contaminado por ruido branco (SNR = {snr_antes:.1f} dB)")
axs[0].set_xlabel("Tempo (s)")
axs[0].set_xlim(0, 0.3)
axs[0].legend()

axs[1].plot(t[: len(sinal_filtrado_fir_alinhado)], sinal_filtrado_fir_alinhado,
            color="tab:orange", label="Sinal filtrado (FIR)")
axs[1].plot(t, sinal_limpo, color="tab:green", linestyle="--", label="Sinal limpo (referencia)")
axs[1].set_title(f"Sinal apos filtro FIR passa-baixa (SNR = {snr_depois_fir:.1f} dB)")
axs[1].set_xlabel("Tempo (s)")
axs[1].set_xlim(0, 0.3)
axs[1].legend()

fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "q02_fir_ruido_branco.png"), dpi=150)
plt.close(fig)

np.savez(os.path.join(os.path.dirname(__file__), "_q02_sinais.npz"),
         t=t, sinal_limpo=sinal_limpo, sinal_ruidoso=sinal_ruidoso)

print("Questao 2 - Filtro FIR passa-baixa (ruido branco)")
print(f"SNR antes da filtragem:  {snr_antes:.2f} dB")
print(f"SNR depois (FIR):        {snr_depois_fir:.2f} dB")
print(f"Ganho de SNR:            {snr_depois_fir - snr_antes:.2f} dB")
print(f"Grafico salvo em: {OUT_DIR}/q02_fir_ruido_branco.png")
