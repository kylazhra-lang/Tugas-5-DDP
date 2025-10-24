# Bagian 1: List Kendaraan
Kendaraan = ["NamaKendaraan", "JenisKendaraan", "ccKendaraan", "WarnaKendaraan", "RodaKendaraan"]

Kendaraan.extend(["HargaKendaraan", "TipeKendaraan"])

Kendaraan.insert(2, "MerkKendaraan")

print("Data List Kendaraan: ")
print(Kendaraan)

# Bagian 2: Match Case Menghitung Luas Bangun Datar
print("Program Menghitung Luas Bangun Datar")
print("1. Persegi")
print("2. Lingkaran")
print("3. Segitiga")

Hitung = int(input("Memilih Program (1/2/3): "))

match Hitung:
    case 1:
        Sisi = float(input("Masukkan Panjang Sisi: "))
        Luas = Sisi * Sisi
        print(f"Luas Persegi = {Luas}")
    case 2:
        r = float(input("Masukkan Jari-Jari Lingkaran: "))
        Luas = 3.14 * r * r
        print(f"Luas Lingkaran = {Luas}")
    case 3:
        Alas = float(input("Masukkan Alas Segitiga: "))
        Tinggi = float(input("Masukkan Tinggi Segitiga "))
        Luas = 0.5 * Alas * Tinggi
        print(f"Luas Segitiga = {Luas}")
    case _:
        print("SALAH PILIH!")