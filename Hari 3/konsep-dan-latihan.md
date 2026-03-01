# Hari 3: Alur Kontrol dan Operator Logika

## Konsep yang dipraktikkan
- Alur Kontrol dengan `if/else` dan Operator Kondisional
    
    ```python
        Equals: a == b
        Not Equals: a != b
        Less than: a < b
        Less than or equal to: a <= b
        Greater than: a > b
        Greater than or equal to: a >= b
    ```

    contoh
    ```python
        print("Selamat datang di wahana rollercoaster.")
        tinggi = int(input("Berapa tinggi badan anda? "))

        if tinggi > 120:
            print("Anda boleh menaiki wahana.")
        else:
            print("Minum susu yang banyak biar tambah tinggi.")
    ```
- Operator Modulo (modulus)\
    Mencari sisa hasil pembagian antara dua bilangan.\
    Contoh:
    ```python
        print(10 % 3)  # Output: 1 dari 3 sisa 1
        print(9 % 2)   # Output: 1 dari 4 sisa 1 (ganjil)
        print(8 % 2)   # Output: 0 (genap) atau habis terbagi
        print(10.5 % 3) # Output: 1.5 (mendukung float)
    ```
- Pernyataan `if` bersarang dan pernyataan `elif`
    ```python
        print("Selamat datang di wahana rollercoaster.")
        tinggi = int(input("Berapa tinggi badan anda? "))

        if tinggi >= 120:
            print("Anda boleh menaiki wahana.")
            umur = int(input("Berapa umur anda?"))
            if umur <= 12:
                print("Bayar karcis 15000")
            elif umur <= 18:
                print("Bayar karcis 20000")
            else:
                print("Bayar karcis 30000")
        else:
            print("Minum susu yang banyak biar tambah tinggi.")
    ```
- ​​Beberapa Pernyataan `if` secara Berurutan\
    ```python
        print("Selamat datang di wahana rollercoaster.")
        tinggi = int(input("Berapa tinggi badan anda? "))
        bayar = 0

        if tinggi >= 120:
            print("Anda boleh menaiki wahana. ")
            umur = int(input("Berapa umur anda? "))
            if umur <= 12:
                bayar = 15000
                print("Karcis anak-anak: 15000")
            elif umur <= 18:
                bayar = 20000
                print("Karcis remaja: 20000")
            else:
                print("Karcis dewasa: 30000")
                bayar = 30000

            mau_foto = input("Apakah anda menginginkan foto? ")
            if mau_foto == "y"
                bayar += 5000

            print(f"Total bayar: {bayar}")
        else:
            print("Minum susu yang banyak biar tambah tinggi.")
    ```
- Operator Logika
    - `and`
        >True `and` True = True\
        >True `and` False = False
        
    - `or`
        >True `or` False = True\
        >False `or` False = False
    - `not`
        >`not` True = False\
        >`not` False = True

# ⚠️NOTE! Indentasi harus selalu diperhatikan!
## Latihan 1 [Operator Modulo]
Tulis kode menggunakan apa yang telah Anda pelajari tentang operator modulo dan pemeriksaan kondisional di Python untuk memeriksa apakah sebuah angka berada di area input ganjil atau genap. Jika ganjil, cetak kata "Ganjil", jika tidak, cetak "Genap".

## Latihan 2 [Kalkulator BMI dengan Interpretasi]
Tambahkan beberapa pernyataan if/elif/else ke kalkulator BMI agar dapat menginterpretasikan nilai BMI yang dihitung.

Jika BMI di bawah 18,5 (tidak termasuk), cetak "kurang berat badan"
Jika BMI antara 18,5 (termasuk) dan 25 (tidak termasuk), cetak "berat badan normal"
Jika BMI 25 (termasuk) atau lebih, cetak "kelebihan berat badan"

```python
    weight = 85
    height = 1.85

    bmi = weight / (height ** 2)


```
[solusi](/Hari%203/solusi.md)

## Latihan 3 [Pizza Order]
Berdasarkan pesanan pengguna, hitung total tagihan mereka.\
Gunakan fungsi input() untuk mendapatkan preferensi pengguna, lalu jumlahkan total pesanan mereka dan beri tahu mereka berapa yang harus mereka bayar.

Pizza kecil (S): $15\
Pizza sedang (M): $20\
Pizza besar (L): $25\
Tambahkan pepperoni untuk pizza kecil (Y atau N): +$2\
Tambahkan pepperoni untuk pizza sedang atau besar (Y atau N): +$3\
Tambahkan keju ekstra untuk pizza ukuran apa pun (Y atau N): +$1\

hint:
```python
    # todo: cari tahu berapa yang harus dibayar berdasar ukuran pesanan

    # todo: cari tahu berapa tambahan total tagihan berdasar pilihan pepperoni

    # todo: cari tahu berapa tagihan akhir berdasarkan pilihan tambahan ekstra keju
```
[solusi](/Hari%203/solusi.md)
