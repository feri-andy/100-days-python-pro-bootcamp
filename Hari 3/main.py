""" print("Selamat datang di wahana rollercoaster!")
tinggi = int(input("Berapa tinggi badan kamu? "))
total_bayar = 0

if tinggi >= 120:
    print("Kamu boleh naik rollercoaster.")
    umur = int(input("Berapa umur kamu saat ini? "))
    if umur <= 12:
        total_bayar = 5000
        print("Harga tiket: 5000")
    elif umur <= 18:
        total_bayar = 10000
        print("Harga tiket: 10000")
    else:
        total_bayar = 15000
        print("Harga tiket: 15000")

    foto = input("Apa anda ingin berfoto? Y atau T ")
    if foto == "Y":
        total_bayar += 5000
        
    print(f"Total harga: {total_bayar}")
else:
    print("Coba lagi saat kamu sudah lebih tinggi.") """

print("Selamat datang di Pizza Hat.")
print()
ukuran = input("Pizza ukuran apa yang anda ingin pesan? S, M, atau L ")
pepperoni = input("Ingin tambahan topping pepperoni? Y atau T ")
ekstra_keju = input("Tambahan ekstra keju? Y atau T ")

harga = 0

if ukuran == "S":
    harga += 15000
elif ukuran == "M":
    harga += 20000
elif ukuran == "L":
    harga += 25000
else:
    print("Anda salah memberikan input.")

if pepperoni == "Y":
    if ukuran == "S":
        harga += 2000
    else:
        harga += 3000

if ekstra_keju == "Y":
    harga += 1000

print()
print(f"Total harga: {harga}")


