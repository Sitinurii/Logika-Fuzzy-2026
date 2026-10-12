import psycopg2


# =========================================
# KONEKSI DATABASE
# =========================================

db = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="nuri123#",
    database="fuzzy_modul1"
)

print("Koneksi database berhasil!")


# =========================================
# FUNGSI KEANGGOTAAN
# =========================================

def fungsi_bayi_naik(x):
    return (x - 0) / (2.5 - 0)


def fungsi_bayi_turun(x):
    return (5 - x) / (5 - 2.5)


def fungsi_anak_naik(x):
    return (x - 6) / (8.5 - 6)


def fungsi_anak_turun(x):
    return (11 - x) / (11 - 8.5)


def fungsi_remaja_naik(x):
    return (x - 10) / (14.5 - 10)


def fungsi_remaja_turun(x):
    return (19 - x) / (19 - 14.5)


def fungsi_pemuda_naik(x):
    return (x - 15) / (19.5 - 15)


def fungsi_pemuda_turun(x):
    return (24 - x) / (24 - 19.5)


def fungsi_dewasa_naik(x):
    return (x - 20) / (42.5 - 20)


def fungsi_dewasa_turun(x):
    return (65 - x) / (65 - 42.5)


def fungsi_lansia_naik(x):
    return (x - 65) / (70 - 65)


def fungsi_lansia_turun(x):
    return (80 - x) / (80 - 70)


# =========================================
# MAPPING NAMA FUNGSI
# =========================================

fungsi = {
    "fungsi_bayi_naik": fungsi_bayi_naik,
    "fungsi_bayi_turun": fungsi_bayi_turun,

    "fungsi_anak_naik": fungsi_anak_naik,
    "fungsi_anak_turun": fungsi_anak_turun,

    "fungsi_remaja_naik": fungsi_remaja_naik,
    "fungsi_remaja_turun": fungsi_remaja_turun,

    "fungsi_pemuda_naik": fungsi_pemuda_naik,
    "fungsi_pemuda_turun": fungsi_pemuda_turun,

    "fungsi_dewasa_naik": fungsi_dewasa_naik,
    "fungsi_dewasa_turun": fungsi_dewasa_turun,

    "fungsi_lansia_naik": fungsi_lansia_naik,
    "fungsi_lansia_turun": fungsi_lansia_turun
}


# =========================================
# FUZZIFIKASI
# =========================================

def fuzzifikasi_usia(x, kategori):

    cursor = db.cursor()

    query = """
        SELECT usia_min, usia_max, nilai_fuzzy
        FROM fungsi_usia
        WHERE kategori = %s
        AND %s >= usia_min
        AND %s <= usia_max
        ORDER BY usia_min
        LIMIT 1
    """

    cursor.execute(query, (kategori, x, x))

    data = cursor.fetchone()

    cursor.close()

    if data is None:
        return None, None, None

    usia_min, usia_max, nama_fungsi = data

    if nama_fungsi == "0":
        return usia_min, usia_max, 0

    if nama_fungsi in fungsi:
        fungsi_y = fungsi[nama_fungsi]
        nilai = fungsi_y(x)

        return usia_min, usia_max, nilai

    raise ValueError(
        f"Fungsi '{nama_fungsi}' belum dibuat di Python."
    )


# =========================================
# PENGUJIAN
# =========================================

data_uji = [
    ("Bayi", 1),
    ("Bayi", 3),

    ("Anak-anak", 7),
    ("Anak-anak", 10),

    ("Remaja", 12),
    ("Remaja", 17),

    ("Pemuda", 17),
    ("Pemuda", 22),

    ("Dewasa", 30),
    ("Dewasa", 50),

    ("Lansia", 68),
    ("Lansia", 75)
]


print("\nHasil Fuzzifikasi")
print("-" * 80)
print(f"{'Kategori':<15}{'Usia':<10}{'Interval':<15}{'Fungsi':<25}{'μ(x)':<10}")
print("-" * 80)


for kategori, usia in data_uji:

    usia_min, usia_max, nilai = fuzzifikasi_usia(
        usia,
        kategori
    )

    cursor = db.cursor()

    query = """
        SELECT nilai_fuzzy
        FROM fungsi_usia
        WHERE kategori = %s
        AND %s >= usia_min
        AND %s <= usia_max
        ORDER BY usia_min
        LIMIT 1
    """

    cursor.execute(query, (kategori, usia, usia))

    data = cursor.fetchone()

    cursor.close()

    nama_fungsi = data[0]

    print(
        f"{kategori:<15}"
        f"{usia:<10}"
        f"{usia_min}-{usia_max:<15}"
        f"{nama_fungsi:<25}"
        f"{nilai:.2f}"
    )


# =========================================
# MENUTUP DATABASE
# =========================================

db.close()

print("-" * 80)
print("Program selesai.")