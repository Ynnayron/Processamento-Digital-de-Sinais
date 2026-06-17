"""
Questao 10 - Aplicacao pratica: suavizacao de sinal de sensor (acelerometro)
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter, lfilter_zi

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "resultados")
os.makedirs(OUT_DIR, exist_ok=True)

np.random.seed(7)
fs = 200.0                 # taxa de amostragem tipica de um IMU de baixo custo (Hz)
T = 3.0
t = np.arange(0, T, 1 / fs)

# Movimento real: oscilacao lenta do corpo (ex.: braco robotico balancando a 1.5 Hz)
movimento_real = 9.8 + 1.5 * np.sin(2 * np.pi * 1.5 * t)

# Ruido de alta frequencia tipico de sensores MEMS + vibracao mecanica da estrutura
ruido_sensor = 0.6 * np.random.normal(size=t.shape)
vibracao_estrutural = 0.4 * np.sin(2 * np.pi * 45.0 * t)

leitura_bruta = movimento_real + ruido_sensor + vibracao_estrutural

# Filtro FIR passa-baixa simples (poucos coeficientes - adequado para um microcontrolador)
ordem = 31
fc = 5.0
coef = firwin(ordem, fc, fs=fs)
zi = lfilter_zi(coef, 1.0) * leitura_bruta[0]   # evita transiente artificial no inicio
leitura_filtrada, _ = lfilter(coef, 1.0, leitura_bruta, zi=zi)
atraso = (ordem - 1) // 2
leitura_filtrada_alinhada = leitura_filtrada[atraso:]
t_alinhado = t[: len(leitura_filtrada_alinhada)]

fig, ax = plt.subplots(figsize=(10, 5.5))
ax.plot(t, leitura_bruta, color="tab:gray", linewidth=0.8, label="Leitura bruta do sensor")
ax.plot(t, movimento_real, color="tab:green", linestyle="--", linewidth=1.3,
        label="Movimento real (referencia)")
ax.plot(t_alinhado, leitura_filtrada_alinhada, color="tab:orange", linewidth=1.5,
        label="Leitura apos filtro FIR (fc = 5 Hz)")
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Aceleracao (m/s^2)")
ax.set_title("Suavizacao de leitura de acelerometro com filtro FIR passa-baixa")
ax.legend()
fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "q10_aplicacao_pratica_sensor.png"), dpi=150)
plt.close(fig)

erro_bruto = np.std(leitura_bruta - movimento_real)
erro_filtrado = np.std(leitura_filtrada_alinhada - movimento_real[: len(leitura_filtrada_alinhada)])

print("Questao 10 - Aplicacao pratica (suavizacao de sinal de acelerometro)")
print(f"Desvio padrao do erro (bruto vs movimento real):    {erro_bruto:.3f} m/s^2")
print(f"Desvio padrao do erro (filtrado vs movimento real): {erro_filtrado:.3f} m/s^2")
print(f"Reducao do erro: {100*(1 - erro_filtrado/erro_bruto):.1f}%")
print(f"Atraso introduzido pelo filtro: {atraso} amostras ({atraso/fs*1000:.1f} ms)")
print(f"Grafico salvo em: {OUT_DIR}/q10_aplicacao_pratica_sensor.png")
