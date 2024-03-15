# Muhammad Zedi Mumtaz
# 122140223
# Tugas Praktikum PBO RB Minggu 3

class Produk:
    jumlah_item = 0
    daftar_item = []

    def __init__(self, nama, stok, harga):
        self.__nama = nama
        self.__stok = stok
        self.__harga = harga

        Produk.jumlah_item += 1
        Produk.daftar_item.append((nama, stok, harga))

    @staticmethod
    def lihat_item():
        print("Jumlah barang pada toko:", Produk.jumlah_item, "buah")
        for idx, item in enumerate(Produk.daftar_item, start=1):
            nama, stok, harga = item
            print(f"{idx}. {nama} seharga Rp {harga} (stok: {stok})")

    def __del__(self):
        Produk.jumlah_item -= 1
        for idx, item in enumerate(Produk.daftar_item):
            nama, _, _ = item
            if nama == self.__nama:
                del Produk.daftar_item[idx]
                print(f"{nama} dihapus dari toko!")
                break

Item1 = Produk("Galon Aqua 19L", 31, 23000)
Item2 = Produk("Gas LPG 5 kg", 24, 88000)
Item3 = Produk("Beras Ramos 5 kg", 17, 68000)

Produk.lihat_item()

del Item1

Produk.lihat_item()
