# Muhammad Zedi Mumtaz
# 122140223
# Tugas Praktikum PBO RB Minggu 2 Soal 1

class Mahasiswa:
    def __init__(self, nim, nama, angkatan, isMahasiswa=True):
        self.__nim = nim
        self.__nama = nama
        self.__angkatan = angkatan
        self.__isMahasiswa = isMahasiswa

    def get_nim(self):
        return self.__nim

    def set_nim(self, nim):
        self.__nim = nim

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def get_angkatan(self):
        return self.__angkatan

    def set_angkatan(self, angkatan):
        self.__angkatan = angkatan

    def info(self):
        return f"NIM: {self.__nim}, Nama: {self.__nama}, Angkatan: {self.__angkatan}, Status: {'Mahasiswa' if self.__isMahasiswa else 'Bukan Mahasiswa'}"

    def status_mahasiswa(self):
        return self.__isMahasiswa

    def tahun_kelulusan(self):
        return self.__angkatan + 4 if self.__isMahasiswa else "Tidak berlaku"

mahasiswa1 = Mahasiswa("122140223", "Muhammad Zedi Mumtaz", 2022)
print(mahasiswa1.info())
print("Status Mahasiswa:", mahasiswa1.status_mahasiswa()) 
print("Tahun Kelulusan Perkiraan:", mahasiswa1.tahun_kelulusan())

print("\n")

mahasiswa2 = Mahasiswa("123140222", "Jedoy", 2023, isMahasiswa=False)
print(mahasiswa2.info())
print("Status Mahasiswa:", mahasiswa2.status_mahasiswa())
print("Tahun Kelulusan Perkiraan:", mahasiswa2.tahun_kelulusan())
