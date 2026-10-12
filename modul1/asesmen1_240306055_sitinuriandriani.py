
import numpy as np
import matplotlib.pyplot as plt


# =====================================
# FUNGSI KEANGGOTAAN RENDAH
# =====================================

def mf_rendah(x):
    if x <= 30:
        return 1.0
    elif x < 50:
        return (50 - x) / 20
    else:
        return 0.0


# =====================================
# FUNGSI KEANGGOTAAN SEDANG
# =====================================

def mf_sedang(x):
    if x <= 30 or x >= 70:
        return 0.0
    elif x <= 50:
        return (x - 30) / 20
    else:
        return (70 - x) / 20


# =====================================
# FUNGSI KEANGGOTAAN TINGGI
# =====================================

def mf_tinggi(x):
    if x <= 50:
        return 0.0
    elif x < 70:
        return (x - 50) / 20
    else:
        return 1.0


# =====================================
# DICTIONARY FUNGSI KEANGGOTAAN
# =====================================

variabel = {
    "CPU Usage": {
        "Rendah": mf_rendah,
        "Sedang": mf_sedang,
        "Tinggi": mf_tinggi
    },
    "RAM Usage": {
        "Rendah": mf_rendah,
        "Sedang": mf_sedang,
        "Tinggi": mf_tinggi
    },
    "Risiko Overload": {
        "Rendah": mf_rendah,
        "Sedang": mf_sedang,
        "Tinggi": mf_tinggi
    }
}


# =====================================
# FUNGSI FUZZIFIKASI
# =====================================

def fuzzifikasi(input_dict):
    hasil = {}

    for nama_variabel, nilai in input_dict.items():
        hasil[nama_variabel] = {}

        for label, fungsi in variabel[nama_variabel].items():
            hasil[nama_variabel][label] = fungsi(nilai)

    return hasil


# =====================================
# FUNGSI MENAMPILKAN GRAFIK
# TIGA GRAFIK DALAM SATU OUTPUT
# =====================================

def plot_variabel():
    x = np.linspace(0, 100, 500)

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    for ax, (nama_variabel, fungsi_dict) in zip(
        axes, variabel.items()
    ):
        for label, fungsi in fungsi_dict.items():
            y = [fungsi(nilai) for nilai in x]
            ax.plot(x, y, label=label)

        ax.set_title(nama_variabel)
        ax.set_xlabel("Nilai (%)")
        ax.set_ylabel("Derajat Keanggotaan")
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 1.1)
        ax.grid(True)
        ax.legend()

    plt.tight_layout()
    plt.savefig("grafik_semua_variabel.png", dpi=300)
    plt.show()
    plt.close()


# =====================================
# DATA PENGUJIAN
# =====================================

data_uji = [
    ("Beban Sangat Rendah", 10, 15),
    ("Beban Rendah", 30, 35),
    ("Beban Sedang", 50, 50),
    ("Beban Tinggi", 75, 80),
    ("Beban Sangat Tinggi", 95, 90)
]


# =====================================
# MENAMPILKAN HASIL FUZZIFIKASI
# =====================================

print("=" * 60)
print("HASIL FUZZIFIKASI SISTEM DETEKSI DINI BEBAN SERVER")
print("=" * 60)

for kasus, cpu, ram in data_uji:
    hasil = fuzzifikasi({
        "CPU Usage": cpu,
        "RAM Usage": ram
    })

    print("\nKasus:", kasus)
    print(f"CPU Usage: {cpu}%")
    print(f"RAM Usage: {ram}%")

    print("\nDerajat Keanggotaan CPU:")
    for label, nilai in hasil["CPU Usage"].items():
        print(f"  {label}: {nilai:.2f}")

    print("\nDerajat Keanggotaan RAM:")
    for label, nilai in hasil["RAM Usage"].items():
        print(f"  {label}: {nilai:.2f}")

    print("-" * 60)


# =====================================
# MENAMPILKAN SEMUA GRAFIK
# =====================================

plot_variabel()
