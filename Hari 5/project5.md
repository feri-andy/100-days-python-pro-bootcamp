# Generator Password

## Versi sederhana
Buat kata sandi secara berurutan. Huruf, lalu simbol, lalu angka. Jika pengguna menginginkan 4 huruf, 2 simbol, dan 3 angka, maka kata sandinya mungkin terlihat seperti ini:\
fgdx$*924\
Anda dapat melihat bahwa semua huruf berada bersamaan. Semua simbol berada bersamaan dan semua angka juga berurutan. Cobalah untuk menyelesaikan masalah ini terlebih dahulu.

## Versi lebih lanjut
Setelah Anda menyelesaikan versi mudahnya. Pada versi lanjutan proyek ini, kata sandi akhirnya tidak mengikuti pola tertentu. Jadi contoh di atas mungkin terlihat seperti ini:\
x$d24g*f9\
Dan setiap kali Anda membuat kata sandi, posisi simbol, angka, dan hurufnya berbeda. Ini akan membuat kata sandi lebih sulit untuk dibobol. Cobalah untuk menyelesaikan tantangan ini.

```python
huruf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
angka = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
simbol = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '<', '>']
```