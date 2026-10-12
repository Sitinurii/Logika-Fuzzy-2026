import numpy as np
import matplotlib.pyplot as plt

# Fungsi keanggotaan Rendah
def mf_rendah(x):
    kondisi = [
        x <= 20.0,
        (x > 20.0) & (x < 40.0),
        x >= 40.0
    ]
    pilihan = [
        1.0,
        (40.0 - x) / (40.0 - 20.0),
        0.0
    ]
    return np.select(kondisi, pilihan)


# Fungsi keanggotaan Normal
def mf_normal(x):
    kondisi = [
        (x <= 30.0) | (x >= 70.0),
        (x > 30.0) & (x <= 50.0),
        (x > 50.0) & (x < 70.0)
    ]
    pilihan = [
        0.0,
        (x - 30.0) / (50.0 - 30.0),
        (70.0 - x) / (70.0 - 50.0)
    ]
    return np.select(kondisi, pilihan)


# Fungsi keanggotaan Tinggi
def mf_tinggi(x):
    kondisi = [
        x <= 60.0,
        (x > 60.0) & (x < 80.0),
        x >= 80.0
    ]
    pilihan = [
        0.0,
        (x - 60.0) / (80.0 - 60.0),
        1.0
    ]
    return np.select(kondisi, pilihan)


# Membuat grafik
x = np.linspace(0, 100, 500)

y_rendah = mf_rendah(x)
y_normal = mf_normal(x)
y_tinggi = mf_tinggi(x)

plt.figure(figsize=(10, 5))

plt.plot(x, y_rendah, label='Rendah', color='green', linewidth=2)
plt.plot(x, y_normal, label='Normal', color='orange', linewidth=2)
plt.plot(x, y_tinggi, label='Tinggi', color='red', linewidth=2)

plt.title('Variabel Linguistik Penggunaan CPU Server')
plt.xlabel('Penggunaan CPU (%)')
plt.ylabel('Derajat Keanggotaan')
plt.ylim(-0.05, 1.05)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()

# Pengujian fuzzifikasi CPU = 10%
cpu = 10

rendah = mf_rendah(cpu)
normal = mf_normal(cpu)
tinggi = mf_tinggi(cpu)

print()
print("Tabel Hasil Fuzzifikasi")
print("-" * 40)
print(f"{'CPU':<10}{'Rendah':<10}{'Normal':<10}{'Tinggi':<10}")
print("-" * 40)
print(f"{cpu:<10}{rendah:<10.2f}{normal:<10.2f}{tinggi:<10.2f}")

# Simpan grafik
plt.savefig('grafik_cpu_server.png', dpi=300)

plt.show()