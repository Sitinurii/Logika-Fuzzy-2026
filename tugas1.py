import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt


def segitiga(x, a, b, c):
    x = np.asarray(x, dtype=float)
    y = np.zeros_like(x, dtype=float)

    # Naik dari a ke b
    mask_1 = (a <= x) & (x <= b)
    y[mask_1] = (x[mask_1] - a) / (b - a) if b != a else 1.0

    # Turun dari b ke c
    mask_2 = (b <= x) & (x <= c)
    y[mask_2] = (c - x[mask_2]) / (c - b) if c != b else 1.0

    return y


# Data kategori usia sesuai soal
# (nama, a, b, c)
data_usia = [
    ('Bayi / Anak Usia Dini', 0, 2.5, 5),
    ('Anak-anak', 6, 8.5, 11),
    ('Remaja (Adolescent)', 10, 14.5, 19),
    ('Pemuda (Youth)', 15, 19.5, 24),
    ('Dewasa (Adult)', 20, 42.5, 65),
    ('Lanjut Usia (Elderly/Lansia)', 60, 70, 80),
]

fig, axes = plt.subplots(2, 3, figsize=(15, 8))
axes = axes.flatten()

for idx, (nama, a, b, c) in enumerate(data_usia):
    ax = axes[idx]

    # Batas x untuk tiap grafik agar terlihat jelas
    x_min = max(0, a - 5)
    x_max = c + 5
    x = np.linspace(x_min, x_max, 500)
    y = segitiga(x, a, b, c)

    ax.plot(x, y, color='tab:blue', linewidth=2)
    ax.scatter([a, b, c], [0, 1, 0], color='tab:orange', zorder=5)

    ax.annotate(f'A({a},0)', (a, 0), xytext=(-10, -15), textcoords='offset points')
    ax.annotate(f'B({b},1)', (b, 1), xytext=(0, 8), textcoords='offset points')
    ax.annotate(f'C({c},0)', (c, 0), xytext=(10, -15), textcoords='offset points')

    ax.set_title(nama, fontsize=10, fontweight='bold')
    ax.set_xlabel('Usia (tahun)', fontsize=8)
    ax.set_ylabel('μ(x)', fontsize=8)
    ax.set_ylim(-0.1, 1.1)
    ax.set_xlim(x_min, x_max)
    ax.grid(True, linestyle='-', alpha=0.5)

fig.suptitle('Fungsi Keanggotaan Logika Fuzzy - Kriteria Usia', fontsize=14, fontweight='bold')
fig.tight_layout()

plt.savefig('semua_grafik_usia.png', dpi=300)
plt.close(fig)

print('Grafik berhasil dibuat dan disimpan ke semua_grafik_usia.png')