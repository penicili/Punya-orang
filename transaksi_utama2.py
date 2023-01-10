import os
import pembayaran

def transaksi():
    os.system('cls')
    for i in range (1, 100):
        print("_",end="")
    print("")
    print("\nDibawah ini, silakan Anda memilih kategori tempat duduk Anda sesuai dengan kantong dan kesenangan yaa..")
    print("\nKeterangan: \n 1. Kategori Rocket, Anda dapat terbang lebih dekat bersama kami! \nDengan harga Rp 1.200.000 \n")
    print("2. Kategori Jet, Anda dapat terbang dengan jarak bersama kami! \nDengan harga Rp 600.000 \n")
    print("3. Kategori Plane, Anda tetap dapat terbang bersama kami! \nDengan harga Rp 300.000 \n")
    print("4. Kategori Helicopter, Anda dapat terbang bersama kami secara online! \nDengan harga Rp 100.000")
    print("\nTentukan pilihanmu sekarang! \nJangan lama-lama yaa..")
    print("1. Rocket ")
    print("2. Jet ")
    print("3. Plane ")
    print("4. Helicopter \n")
    print("Reminder:")
    print("Anda hanya bisa memilih 1 kategori kursi untuk 1 account.")
    print("Ingat. Ketikkan angkanya saja ya 1 kali..\n")


def merchandise():
    print("\nInilah beberapa pilihan merchandisenya : ")
    print("1. T-shirt special konser - Rp 165.000 ")
    print("2. Lanyard keren - Rp 35.000 ")
    print("3. Lightstick - Rp 280.000 ")
    print("4. Sapu tangan Galaxy - Rp 50.000 ")
    print("5. Kipas manual - Rp 30.000 ")
    print("6. Photopack - Rp 80.000 ")
    print("0. -- Ngga dulu deh / beli ini aja deh --\n")


pilihanKategori = int(input("Silakan masukkan kategori kursi yang Anda inginkan.. (Ketikkan angkanya saja ya!) = "))
i = 0
hargaKursi = 0
banyakKursi = int(input("\nSilakan masukkan banyak kursi yang akan dipesan.. (Ketikkan angkanya saja ya!) = "))
while i < banyakKursi:
    i = i + 1
    if (pilihanKategori == 1):
        hargaKursi = hargaKursi + (1200000 * banyakKursi)
        break
    elif (pilihanKategori == 2):
        hargaKursi = hargaKursi + (600000 * banyakKursi)
        break
    elif (pilihanKategori == 3):
        hargaKursi = hargaKursi + (300000 * banyakKursi)
        break
    elif (pilihanKategori == 4):
        hargaKursi = hargaKursi + (100000 * banyakKursi)
        break
    else:
        print("Masukkan pilihan kategori yang sesuai ya (ketikkan angkanya saja) ^^")
        transaksi()

print("\nTotal harga kursi dengan kategori", pilihanKategori, "= Rp ", hargaKursi)
print("")
for i in range (1, 100):
    print("_",end="")
    print("")

print("\nSelanjutnya, silakan Anda memilih Merchandise ekslusif dari kami!")
merchandise()

banyakBarang = int(input("Silakan masukkan banyak pilihan kategori merchandise yang akan dibawa pulang.. (Ketikkan angkanya saja ya!) = "))
i = 0
jumlahHarga = 0
while i < banyakBarang:
    pilihanMerchandise = int(input("\nMasukkan pilihan merchandise = "))
    i = i + 1
    if (pilihanMerchandise == 1):
        jumlahMerchandise = int(input("\nMasukkan jumlah merchandise pilihan 1 = "))
        jumlahHarga = jumlahHarga + (165000 * jumlahMerchandise)
    elif (pilihanMerchandise == 2):
        jumlahMerchandise = int(input("\nMasukkan jumlah merchandise pilihan 2 = "))
        jumlahHarga = jumlahHarga + (35000 * jumlahMerchandise)
    elif (pilihanMerchandise == 3):
        jumlahMerchandise = int(input("\nMasukkan jumlah merchandise pilihan 3 = "))
        jumlahHarga = jumlahHarga + (280000 * jumlahMerchandise)
    elif (pilihanMerchandise == 4):
        jumlahMerchandise = int(input("\nMasukkan jumlah merchandise pilihan 4 = "))
        jumlahHarga = jumlahHarga + (50000 * jumlahMerchandise)
    elif (pilihanMerchandise == 5):
        jumlahMerchandise = int(input("\nMasukkan jumlah merchandise pilihan 5 = "))
        jumlahHarga = jumlahHarga + (30000 * jumlahMerchandise)
    elif (pilihanMerchandise == 6):
        jumlahMerchandise = int(input("\nMasukkan jumlah merchandise pilihan 6 = "))
        jumlahHarga = jumlahHarga + (80000 * jumlahMerchandise)
    elif (pilihanMerchandise == 0):
        print("\nTerimakasih telah melihat-lihat merchandise kami!")
        break
    else:
        print("\nMasukkan pilihan merchandise yang sesuai ya (ketikkan angkanya saja) ^^")
    merchandise()
        
print("\nTotal belanjaan merchandise = Rp ", jumlahHarga)
for i in range (1, 100):
    print("_",end="")
print("")

print("\nTotal uang yang perlu Anda keluarkan untuk membeli tiket dan juga membayar merchandise adalah Rp ", jumlahHarga + hargaKursi)
print("\nSilakan masuk ke menu pembayaran ya..")
pembayaran.bayar()