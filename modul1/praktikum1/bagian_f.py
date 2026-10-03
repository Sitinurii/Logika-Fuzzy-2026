import numpy as np
import matplotlib.pyplot as plt

# 1. DEFINISI FUNGSI KARAKTERISTIK CRISP
def crisp_memuaskan(rating, threshold=4.0):
    """
    Fungsi karakteristik crisp.
    Mengembalikan 1 jika rating >= threshold, selain itu 0.
    """
    return np.where(rating >= threshold, 1.0, 0.0)


# 2. DEFINISI FUNGSI KEANGGOTAAN FUZZY LINEAR
def fuzzy_memuaskan(rating, a=2.5, b=4.5):
    """
    Fungsi keanggotaan fuzzy linear naik.
    """
    derajat = (rating - a) / (b - a)
    return np.clip(derajat, 0.0, 1.0)


# 3. DEFINISI FUNGSI KEANGGOTAAN FUZZY SIGMOID
def fuzzy_sigmoid(rating, x0=3.5, k=2.0):
    """
    Fungsi keanggotaan fuzzy berbentuk Sigmoid.
    """
    return 1 / (1 + np.exp(-k * (rating - x0)))


# 4. GENERASI DATA
ratings = np.linspace(1.0, 5.0, 500)

y_crisp = crisp_memuaskan(ratings, threshold=4.0)
y_fuzzy = fuzzy_memuaskan(ratings, a=2.5, b=4.5)
y_sigmoid = fuzzy_sigmoid(ratings, x0=3.5, k=2.0)


# 5. VISUALISASI PERBANDINGAN
plt.figure(figsize=(10, 5))

# Crisp
plt.step(
    ratings,
    y_crisp,
    label='Crisp (Threshold = 4.0)',
    color='#d9534f',
    linewidth=2.5,
    where='post'
)

# Fuzzy Linear
plt.plot(
    ratings,
    y_fuzzy,
    label='Fuzzy (Linear Naik [2.5, 4.5])',
    color='#0275d8',
    linewidth=2.5
)

# Fuzzy Sigmoid
plt.plot(
    ratings,
    y_sigmoid,
    label='Fuzzy (Sigmoid x0=3.5, k=2.0)',
    color='#5cb85c',
    linewidth=2.5
)

plt.title(
    'Perbandingan Crisp, Fuzzy Linear, dan Fuzzy Sigmoid',
    fontsize=13,
    fontweight='bold'
)

plt.xlabel('Rating Pengguna (Skala 1 - 5)', fontsize=11)
plt.ylabel('Derajat Keanggotaan / Nilai Kebenaran', fontsize=11)

plt.ylim(-0.05, 1.1)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left', fontsize=10)
plt.tight_layout()

# Simpan dan tampilkan grafik
plt.savefig('visualisasi_crisp_fuzzy_sigmoid.png', dpi=300)
plt.show()