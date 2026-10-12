import numpy as np
import matplotlib.pyplot as plt


# ==========================================================
# 1. FUNGSI KEANGGOTAAN A
#    Ketersediaan Bandwidth Cukup
#    Segitiga [30, 60, 90]
# ==========================================================
def fungsi_a(x):
    kondisi = [
        x <= 30,
        (x > 30) & (x <= 60),
        (x > 60) & (x < 90),
        x >= 90
    ]

    pilihan = [
        0.0,
        (x - 30) / 30,
        (90 - x) / 30,
        0.0
    ]

    return np.select(kondisi, pilihan)


# ==========================================================
# 2. FUNGSI KEANGGOTAAN B
#    Packet Loss Rendah
#    Trapesium [40, 55, 75, 95]
# ==========================================================
def fungsi_b(x):
    kondisi = [
        x <= 40,
        (x > 40) & (x <= 55),
        (x > 55) & (x <= 75),
        (x > 75) & (x < 95),
        x >= 95
    ]

    pilihan = [
        0.0,
        (x - 40) / 15,
        1.0,
        (95 - x) / 20,
        0.0
    ]

    return np.select(kondisi, pilihan)


# ==========================================================
# 3. OPERASI IRISAN
# ==========================================================

def zadeh_min(mu_a, mu_b):
    return np.minimum(mu_a, mu_b)


def algebraic_product(mu_a, mu_b):
    return mu_a * mu_b


# ==========================================================
# 4. OPERASI GABUNGAN
# ==========================================================

def zadeh_max(mu_a, mu_b):
    return np.maximum(mu_a, mu_b)


def algebraic_sum(mu_a, mu_b):
    return mu_a + mu_b - (mu_a * mu_b)


# ==========================================================
# 5. OPERASI KOMPLEMEN
# ==========================================================

def komplemen(mu_a):
    return 1.0 - mu_a


# ==========================================================
# 6. MEMBUAT SEMESTA X
# ==========================================================

x = np.linspace(0, 100, 500)

mu_a = fungsi_a(x)
mu_b = fungsi_b(x)

hasil_min = zadeh_min(mu_a, mu_b)
hasil_product = algebraic_product(mu_a, mu_b)

hasil_max = zadeh_max(mu_a, mu_b)
hasil_sum = algebraic_sum(mu_a, mu_b)

hasil_not_a = komplemen(mu_a)


# ==========================================================
# 7. PLOT
# ==========================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 9))

# Grafik 1: Fungsi A, B, dan Komplemen A
axes[0, 0].plot(x, mu_a, label='A - Bandwidth Cukup')
axes[0, 0].plot(x, mu_b, label='B - Packet Loss Rendah')
axes[0, 0].plot(x, hasil_not_a, label='Komplemen A')

axes[0, 0].set_title('Fungsi Keanggotaan A, B dan Komplemen A')
axes[0, 0].set_xlabel('Throughput (Mbps)')
axes[0, 0].set_ylabel('Derajat Keanggotaan')
axes[0, 0].set_ylim(-0.05, 1.05)
axes[0, 0].grid(True)
axes[0, 0].legend()


# Grafik 2: Operasi Irisan
axes[0, 1].plot(x, hasil_min, label='Zadeh Min')
axes[0, 1].plot(x, hasil_product, label='Algebraic Product')

axes[0, 1].set_title('Operasi Irisan')
axes[0, 1].set_xlabel('Throughput (Mbps)')
axes[0, 1].set_ylabel('Derajat Keanggotaan')
axes[0, 1].set_ylim(-0.05, 1.05)
axes[0, 1].grid(True)
axes[0, 1].legend()


# Grafik 3: Operasi Gabungan
axes[1, 0].plot(x, hasil_max, label='Zadeh Max')
axes[1, 0].plot(x, hasil_sum, label='Algebraic Sum')

axes[1, 0].set_title('Operasi Gabungan')
axes[1, 0].set_xlabel('Throughput (Mbps)')
axes[1, 0].set_ylabel('Derajat Keanggotaan')
axes[1, 0].set_ylim(-0.05, 1.05)
axes[1, 0].grid(True)
axes[1, 0].legend()


# Grafik 4: Komplemen A
axes[1, 1].plot(x, mu_a, label='A')
axes[1, 1].plot(x, hasil_not_a, label='Komplemen A')

axes[1, 1].set_title('Komplemen A')
axes[1, 1].set_xlabel('Throughput (Mbps)')
axes[1, 1].set_ylabel('Derajat Keanggotaan')
axes[1, 1].set_ylim(-0.05, 1.05)
axes[1, 1].grid(True)
axes[1, 1].legend()


plt.tight_layout()

plt.savefig(
    'operasi_himpunan_fuzzy_komparasi.png',
    dpi=300
)

plt.show()


# ==========================================================
# 8. PENGUJIAN 4 NILAI THROUGHPUT
# ==========================================================

nilai_uji = [35, 50, 65, 80]

print("\nHasil Pengujian Operasi Himpunan Fuzzy")
print("-" * 110)

print(
    f"{'Throughput':<12}"
    f"{'μA':<10}"
    f"{'μB':<10}"
    f"{'Min':<10}"
    f"{'Product':<12}"
    f"{'Max':<10}"
    f"{'Alg.Sum':<12}"
    f"{'¬A':<10}"
)

print("-" * 110)

for nilai in nilai_uji:

    a = float(fungsi_a(np.array(nilai)))
    b = float(fungsi_b(np.array(nilai)))

    minimum = float(zadeh_min(a, b))
    product = float(algebraic_product(a, b))

    maximum = float(zadeh_max(a, b))
    jumlah = float(algebraic_sum(a, b))

    not_a = float(komplemen(a))

    print(
        f"{nilai:<12}"
        f"{a:<10.2f}"
        f"{b:<10.2f}"
        f"{minimum:<10.2f}"
        f"{product:<12.2f}"
        f"{maximum:<10.2f}"
        f"{jumlah:<12.2f}"
        f"{not_a:<10.2f}"
    )

print("-" * 110)