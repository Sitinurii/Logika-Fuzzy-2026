import numpy as np
import matplotlib.pyplot as plt


# Fungsi Crisp
def crisp_critical(jam, threshold=8):
    return np.where(jam >= threshold, 1.0, 0.0)


# Fungsi Fuzzy Linear
def fuzzy_critical(jam, a=4, b=12):
    derajat = (jam - a) / (b - a)
    return np.clip(derajat, 0.0, 1.0)


# Data pengujian
data_uji = np.array([
    2, 4, 6, 7.9, 8.0, 8.1, 10, 12, 16, 24
])


# Hitung derajat keanggotaan
hasil_crisp = crisp_critical(data_uji)
hasil_fuzzy = fuzzy_critical(data_uji)


# Tampilkan hasil
print("Jam\tCrisp\tFuzzy")

for jam, crisp, fuzzy in zip(data_uji, hasil_crisp, hasil_fuzzy):
    print(f"{jam}\t{crisp:.2f}\t{fuzzy:.2f}")


# Data untuk grafik
jam = np.linspace(0, 24, 500)

y_crisp = crisp_critical(jam)
y_fuzzy = fuzzy_critical(jam)


# Membuat grafik
plt.figure(figsize=(10, 5))

plt.step(
    jam,
    y_crisp,
    where='post',
    label='Crisp',
    linewidth=2
)

plt.plot(
    jam,
    y_fuzzy,
    label='Fuzzy Linear',
    linewidth=2
)

plt.title('Perbandingan Crisp dan Fuzzy pada Prioritas Tiket Helpdesk')
plt.xlabel('Waktu Tunggu (Jam)')
plt.ylabel('Derajat Keanggotaan')
plt.ylim(-0.05, 1.05)
plt.grid(True)
plt.legend()

plt.tight_layout()

# Simpan grafik
plt.savefig(
    'perbandingan_crisp_fuzzy_helpdesk.png',
    dpi=300
)

plt.show()
