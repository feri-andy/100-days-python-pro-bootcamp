print("Selamat datang di pulau Kamidi.\nMisi anda adalah mencari peta harta karun di pulau ini.")
pilihan1 = input("Kamu sekarang berada di sebuah persimpangan, jalan mana yang kamu pilih? Kanan atau kiri? ").lower()

if pilihan1 == "kiri":
    print("Kamu tiba di sebuah sungai yang lebar.\nApakah kamu akan menunggu ada kapal? Atau nekat berenang? Ketik tunggu atau renang .")
    pilihan2 = input().lower()
    if pilihan2 == "tunggu":
        print("Kamu berhasil menyeberangi sungai dengan kapal. Sekarang dihadapanmu terdapat 3 pintu dengan warna merah, kuning, dan biru.\nPeti harta ada di balik salah satu pintu tersebut.\nPintu mana yang kamu pilih? Ketik merah, kuning, atau biru. ")
        pilihan3 = input().lower
        if pilihan3 == "merah":
            print("Kamu terjebak dalam ruangan penuh dengan api membara.\nKamu menjadi arang gosong.\nGagal. Permainan selesai.")
        elif pilihan3 == "biru":
            print("Kamu terjebak dalam ruangan yang berisikan binatang-binatang buas.\nKamu diterkam dan tewas.\nGagal. Permainan selesai")
        elif pilihan3 == "kuning":
            print("Selamat! Peti harta kamu temukan!\nPermainan selesai.")
        else:
            print("Kamu tidak memberikan input yang benar.\nPermainan berakhir.")
    elif pilihan2 == "renang":
        print("Kamu nekat berenang, namun tidak disangka sungai tersebut penuh dengan buaya lapar.\nKamu tenggelam dan dimangsa buaya.\nGagal. Permainan selesai.")
    else:
        print("Kamu tidak memberikan input yang benar.\nPermainan berakhir.")
elif pilihan1 == "kanan":
    print("Kamu terkena sebuah jebakan beruang.\nGagal. Permainan selesai.")
else:
    print("Kamu tidak memberikan input yang benar.\nPermainan berakhir.")