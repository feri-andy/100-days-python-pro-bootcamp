# print("Cek ganjil atau genap.")
# angka = int(input("Masukkan sembarang angka yang anda inginkan. "))

# if angka % 2 == 0:
#     print(f"Angka {angka} adalah genap")
# else:
#     print(f"Angka {angka} adalah ganjil")

print("Selamat datang di wahana rollercoaster.")
tinggi = int(input("Berapa tinggi badan anda? "))
bayar = 0

if tinggi >= 120:
    print("Anda boleh menaiki wahana.")
    umur = int(input("Berapa umur anda?"))
    if umur <= 12:
        bayar = 15000
        print("Karcis anak-anak: 15000")
    elif umur <= 18:
        bayar = 20000
        print("Karcis remaja: 20000")
    else:
        print("Karcis dewasa: 30000")
        bayar = 30000

    mau_foto = input("Apakah anda menginginkan foto?")
    if mau_foto == "y":
        bayar += 5000

    print(f"Total bayar: {bayar}")
else:
    print("Minum susu yang banyak biar tambah tinggi.")
