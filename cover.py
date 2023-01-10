import os
import transaksi_utama
 
def splashCover():
    os.system('cls')
    for i in range (1, 100):
        print("_",end="")
    print("")
    print("\nHai, selamat membeli tiket konser")
    print("\nTiket konser dijual secara terbatas!")
    print("\nCepatlah membeli!")
    print("\nJangan sampai terlewatkan!")
    print("")
    print("\nKonser ini bertemakan pesawat terbang yang berarti dapat terus membawamu terbang kemanapun.")
    print("")
    for i in range (1, 100):
        print("_",end="")
    print("")

def closing():
    print("")
    for i in range (1, 100):
        print("_",end="")
    print("")
    print("\nTerimakasih anda telah memilih aplikasi kami \n")
    print("Jika telah memesan tiket konser, perhatikan tanggal dan waktunya ya!\n")
    print("Jangan sampai terlewatkan yaa..\n")
    print("Jika belum memesan tiket, segeralah!\n")
    print("Jangan sampai kehabisan!")
    print("")
    print("SAMPAI JUMPA DIHARI KONSER YA!")
    print("")
    for i in range (1, 100):
        print("_",end="")
    print("")
    quit()

def pilihan():
    pilihan = input("\nSilakan ketikan kata senyum untuk masuk dan kata pulang untuk keluar ^^\n")
    if(pilihan == "senyum" or pilihan == "Senyum" or pilihan == "SENYUM"):
        print("Anda akan masuk ke halaman selanjutnya")
        print("Mohon ditunggu...")
        transaksi_utama.transaksi()
    elif(pilihan == "pulang" or pilihan == "Pulang" or pilihan == "PULANG"):
        print("\nAnda akan meninggalkan kami :(\n")
        print("Selamat tinggal!")
        print("")
        closing()
    else:
        print("Anda salah memasukkan kata. Ketikkan kata senyum untuk masuk dan kata pulang untuk keluar ^^")
        
