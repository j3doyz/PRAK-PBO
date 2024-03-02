#Muhammad Zedi Mumtaz
#122140223
#Tugas Praktikum PBO RB MG 1 Soal 2

jari_jari = int(input("Inputkan jari-jari : "))
phi = 3.14

if jari_jari < 0 :
    print("Maaf, jari-jari lingkaran tidak boleh negatif")
else :
    luas = phi * jari_jari ** 2
    keliling = 2 * phi * jari_jari

    print("Luas lingkaran adalah : ", luas)
    print("Keliling lingkaran adalah : ", keliling)
