# LANGKAH 1: VARIABEL DAN ATURAN PENAMAAN
print("=== Langkah 1: Variabel ===")
nama_depan = "Budi"
umur = 20
tinggi_badan = 170.5
is_aktif = True

print("Nama:", nama_depan)
print("Umur:", umur, "tahun")
print("Tinggi:", tinggi_badan, "cm")
print("Status Aktif:", is_aktif)

# LANGKAH 2: TIPE DATA DASAR
print("\n=== Langkah 2: Tipe Data Dasar ===")
angka_bulat = 25
angka_desimal = 3.14
teks = "Belajar Python"
status = False

print("Tipe angka_bulat:", type(angka_bulat))
print("Tipe angka_desimal:", type(angka_desimal))
print("Tipe teks:", type(teks))
print("Tipe status:", type(status))

# LANGKAH 3: TIPE DATA KOLEKSI
print("\n=== Langkah 3: Tipe Data Koleksi ===")
hobi = ["Membaca", "Koding", "Berenang"]
koordinat = (-6.1751, 106.8650)
mahasiswa = {"nama": "Siti", "nim": "123456", "ipk": 3.85}
angka_unik = {1, 2, 2, 3, 4, 4, 5}

print("List Hobi:", hobi)
print("Tuple Koordinat:", koordinat)
print("Dict Mahasiswa:", mahasiswa)
print("Nama Mahasiswa:", mahasiswa["nama"])
print("Set Angka Unik:", angka_unik)

# LANGKAH 4: KONVERSI TIPE DATA
print("\n=== Langkah 4: Konversi Tipe Data ===")
str_angka = "100"
int_angka = int(str_angka)
print("Hasil Penjumlahan (100 + 50):", int_angka + 50)

ipk_float = 3.75
ipk_int = int(ipk_float)
print("Float ke Int:", ipk_int)

tahun = 2024
pesan = "Tahun saat ini: " + str(tahun)
print(pesan)

daftar_buah = ["Apel", "Jeruk", "Apel", "Pisang", "Jeruk"]
buah_unik = set(daftar_buah)
print("Buah Unik:", buah_unik)
