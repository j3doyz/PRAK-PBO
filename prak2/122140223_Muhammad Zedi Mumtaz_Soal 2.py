# Muhammad Zedi Mumtaz
# 122140223
# Tugas Praktikum PBO RB Minggu 2 Soal 2

class Gitar:
    def __init__(self, merek, model, harga):
        self.merek = merek
        self.model = model
        self.harga = harga

    def __str__(self):
        return f"{self.merek} {self.model} - Rp {self.harga}"

    def __del__(self):
        print(f"Gitar {self.merek} {self.model} telah terjual.")

def catat_terjual(func):
    def wrapper(self, indeks):
        gitar_terjual = self.gitar[indeks]
        del self.gitar[indeks]
        func(self, indeks)
        print(f"Gitar {gitar_terjual.merek} {gitar_terjual.model} telah terjual.")
    return wrapper

class TokoGitar:
    def __init__(self, nama):
        self.nama = nama
        self.gitar = []

    @catat_terjual
    def beli_gitar(self, merek, model, harga):
        gitar = Gitar(merek, model, harga)
        self.gitar.append(gitar)
        print(f"{merek} {model} telah ditambahkan ke penyimpanan.")

    def tampilkan_penyimpanan(self):
        if not self.gitar:
            print("Penyimpanan kosong.")
        else:
            print(f"Penyimpanan {self.nama}:")
            for idx, gitar in enumerate(self.gitar):
                print(f"{idx + 1}. {gitar}")

# Contoh penggunaan:
toko = TokoGitar("MZM Gitar")

toko.beli_gitar("Fender", "Stratocaster", 15000000)
toko.beli_gitar("Gibson", "Les Paul", 20000000)
toko.beli_gitar("Taylor", "814ce", 25000000)

toko.tampilkan_penyimpanan()

# Simulasi habis terjual
toko.beli_gitar(0)
toko.tampilkan_penyimpanan()
