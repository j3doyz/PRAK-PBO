# Muhammad Zedi Mumtaz
# 122140223
# Tugas Praktikum PBO RB Minggu 2 Soal 2

def validate_price(func):
    def wrapper(*args, **kwargs):
        harga = kwargs.get('harga')
        if harga is not None and not isinstance(harga, (int, float)):
            raise ValueError("Harga harus berupa nilai numerik.")
        return func(*args, **kwargs)
    return wrapper

class Buku:
    def __init__(self, judul, pengarang, harga):
        self.judul = judul
        self.pengarang = pengarang
        self.harga = harga

    def __str__(self):
        return f"{self.judul} oleh {self.pengarang} - Rp {self.harga}"

    def __del__(self):
        print(f"Buku '{self.judul}' telah terjual habis dan dihapus dari inventaris.")

class TokoBuku:
    def __init__(self):
        self.inventaris = []

    def tambah_buku(self, judul, pengarang, harga):
        buku = Buku(judul, pengarang, harga)
        self.inventaris.append(buku)

    def daftar_buku(self):
        if not self.inventaris:
            print("Tidak ada buku tersedia di toko.")
        else:
            print("\nBuku yang Tersedia:")
            for idx, buku in enumerate(self.inventaris, 1):
                print(f"{idx}. {buku}")

    def jual_buku(self, judul):
        for buku in self.inventaris:
            if buku.judul == judul:
                print(f"Terjual: {buku}")
                self.inventaris.remove(buku)
                del buku
                return
        print(f"Maaf, '{judul}' tidak tersedia di toko.")

class Customer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Pelanggan: {self.name}"

    def __del__(self):
        print(f"{self.name} telah membeli semua buku yang tersisa di toko.")

toko_buku = TokoBuku()
toko_buku.tambah_buku("DETEKTIF CONAN", "Gosho Aoyama", 25000)
toko_buku.tambah_buku("NARUTO", "Masashi Kishimoto", 30000)
toko_buku.tambah_buku("ONE PIECE", "Eiichiro Oda", 35000)

toko_buku.daftar_buku()

toko_buku.jual_buku("DETEKTIF CONAN")

toko_buku.daftar_buku()

pelanggan = Customer("Sakti")
print(pelanggan)
