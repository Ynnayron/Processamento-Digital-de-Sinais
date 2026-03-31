import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os

os.makedirs("./resultados", exist_ok=True)

plt.rcParams.update({
    "figure.dpi": 150,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "axes.titlesize": 11,
    "axes.labelsize": 10,
})

# ─────────────────────────────────────────────────────────────
# SIMULAÇÃO 1 – Sequências Elementares
# ─────────────────────────────────────────────────────────────

def impulso(n):
    return (n == 0).astype(float)

def degrau(n):
    return (n >= 0).astype(float)

def exponencial_real(n, a=0.8):
    return (a ** n) * degrau(n)

def exponencial_complexa(n, omega=np.pi/4):
    return np.exp(1j * omega * n)

n = np.arange(-10, 31)

fig, axes = plt.subplots(4, 1, figsize=(10, 12))
fig.suptitle("Simulação 1 – Sequências Elementares", fontsize=13, fontweight="bold")

# Impulso
axes[0].stem(n, impulso(n), linefmt="C0-", markerfmt="C0o", basefmt="k-")
axes[0].set_title("Impulso Unitário  δ[n]")
axes[0].set_xlabel("n"); axes[0].set_ylabel("Amplitude")

# Degrau
axes[1].stem(n, degrau(n), linefmt="C1-", markerfmt="C1o", basefmt="k-")
axes[1].set_title("Degrau Unitário  u[n]")
axes[1].set_xlabel("n"); axes[1].set_ylabel("Amplitude")

# Exponencial real (a=0.8)
axes[2].stem(n, exponencial_real(n, a=0.8), linefmt="C2-", markerfmt="C2o", basefmt="k-")
axes[2].set_title("Exponencial Real  x[n] = (0.8)ⁿ · u[n]   (convergente)")
axes[2].set_xlabel("n"); axes[2].set_ylabel("Amplitude")

# Exponencial complexa – partes real e imaginária
xc = exponencial_complexa(n, omega=np.pi/6)
axes[3].stem(n, np.real(xc), linefmt="C3-", markerfmt="C3o", basefmt="k-", label="Re{x[n]}")
axes[3].stem(n, np.imag(xc), linefmt="C4--", markerfmt="C4^", basefmt="k-", label="Im{x[n]}")
axes[3].set_title("Exponencial Complexa  x[n] = e^(jπn/6)")
axes[3].set_xlabel("n"); axes[3].set_ylabel("Amplitude"); axes[3].legend()

plt.tight_layout()
plt.savefig("./resultados/sim1_sequencias_elementares.png", bbox_inches="tight")
plt.close()

# ─────────────────────────────────────────────────────────────
# SIMULAÇÃO 2 – Operações com Sinais
# ─────────────────────────────────────────────────────────────

n2 = np.arange(-15, 25)

# Sinal base: exponencial amortecida
x_base = np.where(n2 >= 0, 0.85**n2, 0.0)

fig, axes = plt.subplots(4, 1, figsize=(10, 12))
fig.suptitle("Simulação 2 – Operações com Sinais", fontsize=13, fontweight="bold")

# Original
axes[0].stem(n2, x_base, linefmt="C0-", markerfmt="C0o", basefmt="k-")
axes[0].set_title("Original  x[n] = (0.85)ⁿ · u[n]")
axes[0].set_ylabel("Amplitude")

# Deslocamento n0=5
x_delay = np.where(n2 - 5 >= 0, 0.85**(n2-5), 0.0)
axes[1].stem(n2, x_delay, linefmt="C1-", markerfmt="C1o", basefmt="k-")
axes[1].set_title("Deslocamento  x[n − 5]")
axes[1].set_ylabel("Amplitude")

# Inversão
x_inv = np.where(-n2 >= 0, 0.85**(-n2), 0.0)
axes[2].stem(n2, x_inv, linefmt="C2-", markerfmt="C2o", basefmt="k-")
axes[2].set_title("Inversão  x[−n]")
axes[2].set_ylabel("Amplitude")

# Escalonamento de amplitude (×2)
axes[3].stem(n2, 2 * x_base, linefmt="C3-", markerfmt="C3o", basefmt="k-")
axes[3].set_title("Escalonamento de Amplitude  2·x[n]")
axes[3].set_ylabel("Amplitude")

for ax in axes:
    ax.set_xlabel("n")

plt.tight_layout()
plt.savefig("./resultados/sim2_operacoes_sinais.png", bbox_inches="tight")
plt.close()

# ─────────────────────────────────────────────────────────────
# SIMULAÇÃO 3 – Energia e Potência
# ─────────────────────────────────────────────────────────────

n3 = np.arange(0, 50)

sinais = {
    "Exponencial  a=0.9  (sinal de energia)": 0.9**n3,
    "Constante  x[n]=1   (sinal de potência)": np.ones_like(n3, dtype=float),
    "Senoide  cos(πn/8)  (sinal de potência)": np.cos(np.pi * n3 / 8),
}

fig, axes = plt.subplots(3, 2, figsize=(12, 10))
fig.suptitle("Simulação 3 – Energia e Potência", fontsize=13, fontweight="bold")

for i, (label, sig) in enumerate(sinais.items()):
    energia_acum = np.cumsum(sig**2)
    potencia_acum = energia_acum / (np.arange(1, len(sig)+1))

    axes[i, 0].stem(n3, sig, linefmt="C%d-" % i, markerfmt="C%do" % i, basefmt="k-")
    axes[i, 0].set_title(label)
    axes[i, 0].set_ylabel("x[n]")
    axes[i, 0].set_xlabel("n")

    axes[i, 1].plot(n3, energia_acum, label="Energia acumulada", color="C%d" % i)
    axes[i, 1].plot(n3, potencia_acum, "--", label="Potência média", color="C%d" % ((i+1)%7))
    axes[i, 1].set_title("Energia e Potência acumuladas")
    axes[i, 1].set_xlabel("n")
    axes[i, 1].legend(fontsize=8)

plt.tight_layout()
plt.savefig("./resultados/sim3_energia_potencia.png", bbox_inches="tight")
plt.close()

# ─────────────────────────────────────────────────────────────
# SIMULAÇÃO 4 – Classificação de Sistemas
# ─────────────────────────────────────────────────────────────

n4 = np.arange(0, 60)
x_in = np.cos(2 * np.pi * 0.05 * n4)

def sys_sem_memoria(x):
    """Sem memória, linear: y[n] = 2·x[n]"""
    return 2 * x

def sys_media_movel(x, M=5):
    """Com memória, linear, causal: y[n] = (1/M) Σ x[n-k], k=0..M-1"""
    y = np.zeros_like(x)
    for i in range(len(x)):
        y[i] = np.mean(x[max(0, i-M+1):i+1])
    return y

def sys_nao_linear(x):
    """Sem memória, não-linear: y[n] = x[n]²"""
    return x**2

def sys_variante(x, n):
    """Variante no tempo: y[n] = n·x[n]"""
    return n * x

sistemas = [
    ("Sem Memória / Linear\ny[n] = 2·x[n]",        sys_sem_memoria(x_in)),
    ("Com Memória / Linear / Causal\ny[n] = Média Móvel (M=5)", sys_media_movel(x_in)),
    ("Sem Memória / Não-Linear\ny[n] = x[n]²",      sys_nao_linear(x_in)),
    ("Variante no Tempo\ny[n] = n·x[n]",            sys_variante(x_in, n4)),
]

fig, axes = plt.subplots(len(sistemas)+1, 1, figsize=(11, 14))
fig.suptitle("Simulação 4 – Classificação de Sistemas", fontsize=13, fontweight="bold")

axes[0].plot(n4, x_in, "k-o", ms=3, label="Entrada x[n]")
axes[0].set_title("Entrada  x[n] = cos(2π·0.05·n)")
axes[0].set_ylabel("Amplitude"); axes[0].set_xlabel("n")

for i, (titulo, y_out) in enumerate(sistemas):
    axes[i+1].plot(n4, x_in, "k--", alpha=0.3, ms=2, label="Entrada")
    axes[i+1].plot(n4, y_out, "C%d-" % i, lw=1.5, label="Saída y[n]")
    axes[i+1].set_title(titulo)
    axes[i+1].set_ylabel("Amplitude"); axes[i+1].set_xlabel("n")
    axes[i+1].legend(fontsize=8)

plt.tight_layout()
plt.savefig("./resultados/sim4_classificacao_sistemas.png", bbox_inches="tight")
plt.close()

# ─────────────────────────────────────────────────────────────
# SIMULAÇÃO 5 – Sinal de Sensor Real (vibração simulada)
# ─────────────────────────────────────────────────────────────

Fs = 1000          # Hz
T  = 2.0           # segundos
t  = np.linspace(0, T, int(Fs*T), endpoint=False)
n5 = np.arange(len(t))

# Vibração: sinal periódico + harmônica + ruído
sinal_continuo   = (1.5 * np.sin(2*np.pi*50*t) +
                    0.5 * np.sin(2*np.pi*120*t) +
                    0.15 * np.random.randn(len(t)))

# Amostragem com Fs=1000 Hz (já é discreta acima)
x_sensor = sinal_continuo.copy()

# Filtragem por média móvel (M=10) — sistema com memória, LIT, causal
M = 10
y_filtrado = sys_media_movel(x_sensor, M=M)

# Energia janelada
janela = 100
energia_janelada = np.array([
    np.sum(x_sensor[max(0,i-janela):i+1]**2)
    for i in range(len(x_sensor))
])

fig = plt.figure(figsize=(12, 10))
fig.suptitle("Simulação 5 – Sinal de Sensor de Vibração (Industrial)", fontsize=13, fontweight="bold")
gs  = gridspec.GridSpec(3, 2, figure=fig)

# Sinal bruto
ax1 = fig.add_subplot(gs[0, :])
ax1.plot(t[:500], x_sensor[:500], lw=0.8, color="steelblue", label="Sinal bruto x[n]")
ax1.plot(t[:500], y_filtrado[:500], lw=1.5, color="darkorange", label=f"Filtrado (MM M={M})")
ax1.set_title("Sinal Bruto vs. Média Móvel (primeiras 500 amostras)")
ax1.set_xlabel("Tempo (s)"); ax1.set_ylabel("Amplitude"); ax1.legend()

# Espectro de frequência
freqs    = np.fft.rfftfreq(len(x_sensor), d=1/Fs)
espectro = np.abs(np.fft.rfft(x_sensor)) / len(x_sensor)
ax2 = fig.add_subplot(gs[1, :])
ax2.plot(freqs, espectro, color="purple", lw=0.8)
ax2.set_title("Espectro de Frequência (FFT do sinal de vibração)")
ax2.set_xlabel("Frequência (Hz)"); ax2.set_ylabel("|X(f)|"); ax2.set_xlim([0, 300])

# Energia janelada
ax3 = fig.add_subplot(gs[2, 0])
ax3.plot(t, energia_janelada, color="crimson", lw=0.9)
ax3.set_title(f"Energia Janelada (janela={janela} amostras)")
ax3.set_xlabel("Tempo (s)"); ax3.set_ylabel("Energia")

# Histograma
ax4 = fig.add_subplot(gs[2, 1])
ax4.hist(x_sensor, bins=60, color="teal", edgecolor="white", alpha=0.85)
ax4.set_title("Distribuição das Amplitudes")
ax4.set_xlabel("Amplitude"); ax4.set_ylabel("Contagem")

plt.tight_layout()
plt.savefig("./resultados/sim5_sensor_vibracao.png", bbox_inches="tight")
plt.close()
