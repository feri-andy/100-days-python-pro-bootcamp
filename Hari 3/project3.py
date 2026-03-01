print("Selamat datang di pulau Kamidi.\nMisi anda adalah mencari peti harta karun di pulau ini.")
pilih1 = input("Kamu berada di sebuah persimpangan, jalan mana yang kamu pilih? Kanan atau Kiri? ").lower()

if pilih1 == "kiri":
    print("Kamu sekarang berada di bibir sungai yang lebar dan mengalir deras. Apa yang akan kamu lakukan selanjutnya? Menunggu ada kapal yang lewat atau berenang. Ketik tunggu atau renang")
    pilih2 = input().lower()
    if pilih2 == "tunggu":
        print("Kamu dihadapkan dengan 3 buah pintu yang harus kamu pilih salah satu. Merah, kuning, atau biru. Pintu manakah yang akan membawamu ke peti harta karun?")
        pilih3 = input().lower()
        if pilih3 == "merah":
            print("Saat kamu berada dalam ruangan pintu merah, api tiba-tiba muncul dari sela dinding.\nSemburan api mengenai tubuh, dan memenuhi satu ruangan.\nKamu tidak bisa mengelak, tubuhmu hangus terbakar karena memilih pintu merah.\nKamu menjadi arang\nPermainan selesai.")
        elif pilih3 == "biru":
            print("Saat kamu berada dalam ruangan pintu biru, tiba-tiba pintu menutup sendiri dan terkunci.\nDi seberang, terbuka sebuah pintu besar, kemudian terlihat sosok-sosok binatang buas. Dengan sorot mata lapar.\nMereka menerkammu, mencabik-cabik tubuhmu, dan memperebutkan daging segarmu.\nKamu mati dimakan binatang buas.\nPermainan selesai.")
        else:
            print("Selamat! Kamu mendapatkan harta karunnya.\nNamun bisakah kamu keluar dari pulau ini?")
    else:
        print("Kamu nekat berenang menyeberangi sungai, tak disangka terdapat buaya besar yang sudah menanti. Kamu mati dimakan buaya. Permainan selesai.")
else:
    print("Kamu terkena perangkap beruang, kamu kehabisan darah dan mati. Permainan selesai.")