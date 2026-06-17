"""
Questao 3 - Filtro IIR Butterworth aplicado ao mesmo sinal ruidoso da Questao 2

"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter, butter

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "resultados")
os.makedirs(OUT_DIR, exist_ok=True)

# --- 1. Reaproveita exatamente o mesmo sinal ruidoso da Questao 2 ---
caminho_dados = os.path.join(os.path.dirname(__file__), "_q02_sinais.npz")
if not os.path.exists(caminho_dados):
    raise FileNotFoundError(
        "Execute primeiro 'q02_fir_ruido_branco.py' para gerar o sinal "
        "compartilhado (garante que a Questao 3 use exatamente o mesmo "
        "sinal ruidoso da Questao 2 para uma comparacao justa)."
    )
dados = np.load(caminho_dados)
t, sinal_limpo, sinal_ruidoso = dados["t"], dados["sinal_limpo"], dados["sinal_ruidoso"]
fs = 1000.0
fc = 30.0

# --- 2. Filtro FIR (igual a Questao 2, para comparacao lado a lado) ---
ordem_fir = 101
coef_fir = firwin(ordem_fir, fc, fs=fs)
sinal_fir = lfilter(coef_fir, 1.0, sinal_ruidoso)
atraso_fir = (ordem_fir - 1) // 2
sinal_fir_alinhado = sinal_fir[atraso_fir:]

# --- 3. Filtro IIR Butterworth ---
ordem_iir = 4
b_iir, a_iir = butter(ordem_iir, fc, fs=fs)
sinal_iir = lfilter(b_iir, a_iir, sinal_ruidoso)

# --- 4. Metricas (SNR) ---
def snr_db(ref, sinal):
    erro = ref - sinal
    return 10 * np.log10(np.sum(ref ** 2) / np.sum(erro ** 2))

snr_antes = snr_db(sinal_limpo, sinal_ruidoso)
snr_fir = snr_db(sinal_limpo[: len(sinal_fir_alinhado)], sinal_fir_alinhado)

# O IIR introduz uma fase nao linear: em 10 Hz ele desloca o sinal em
# ~14-15 amostras, mesmo sem atenuar a amplitude. Se compararmos direto
# (sem corrigir esse deslocamento), o "erro" fica artificialmente alto
# por causa da fase, nao por causa do ruido. Por isso buscamos o atraso
# que melhor alinha as duas curvas (correlacao cruzada) antes de medir o SNR -
# essa e exatamente a distorcao de fase discutida nas Questoes 8 e 9.
correlacao = np.correlate(sinal_iir - sinal_iir.mean(),
                           sinal_limpo - sinal_limpo.mean(), mode="full")
atraso_iir = correlacao.argmax() - (len(sinal_limpo) - 1)
sinal_iir_alinhado = sinal_iir[atraso_iir:]
sinal_limpo_alinhado_iir = sinal_limpo[: len(sinal_iir_alinhado)]

snr_iir_bruto = snr_db(sinal_limpo, sinal_iir)
snr_iir = snr_db(sinal_limpo_alinhado_iir, sinal_iir_alinhado)

# --- 5. Graficos comparativos ---
fig, axs = plt.subplots(3, 1, figsize=(10, 9), sharex=True)

axs[0].plot(t, sinal_ruidoso, color="tab:gray", linewidth=0.8)
axs[0].plot(t, sinal_limpo, color="tab:green", linewidth=1.3)
axs[0].set_title(f"Sinal ruidoso (SNR = {snr_antes:.1f} dB)")

axs[1].plot(t[: len(sinal_fir_alinhado)], sinal_fir_alinhado, color="tab:orange")
axs[1].plot(t, sinal_limpo, color="tab:green", linestyle="--")
axs[1].set_title(f"Filtro FIR, ordem {ordem_fir} (SNR = {snr_fir:.1f} dB)")

axs[2].plot(t[: len(sinal_iir_alinhado)], sinal_iir_alinhado, color="tab:red")
axs[2].plot(t, sinal_limpo, color="tab:green", linestyle="--")
axs[2].set_title(f"Filtro IIR Butterworth, ordem {ordem_iir}, alinhado em fase (SNR = {snr_iir:.1f} dB)")
axs[2].set_xlabel("Tempo (s)")

for ax in axs:
    ax.set_xlim(0, 0.3)

fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "q03_iir_butterworth_ruido.png"), dpi=150)
plt.close(fig)

print("Questao 3 - Comparacao FIR vs IIR Butterworth (ruido branco)")
print(f"SNR antes:                         {snr_antes:.2f} dB")
print(f"SNR com FIR (ord.101):              {snr_fir:.2f} dB")
print(f"SNR com IIR sem correcao de fase:   {snr_iir_bruto:.2f} dB")
print(f"Atraso de fase estimado do IIR:     {atraso_iir} amostras ({atraso_iir/fs*1000:.1f} ms)")
print(f"SNR com IIR apos alinhar a fase:    {snr_iir:.2f} dB")
print(f"Grafico salvo em: {OUT_DIR}/q03_iir_butterworth_ruido.png")
