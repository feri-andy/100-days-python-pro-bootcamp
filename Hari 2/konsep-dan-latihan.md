# Hari 2: Memahami Jenis Data dan Cara Memanipulasi String

## Konsep yang dipraktikkan
- Tipe Data Primitif Python
    ```
    1. String => "kata-kata"
    2. Integer => 12345
    3. Float => 123.45
    4. Booleans => True / False
    ```
- Kesalahan Tipe, Pemeriksaan Tipe, dan Konversi Tipe
    ```shell
    print("jumlah karakter: " + len("manusia")) ❌

    Traceback (most recent call last):
    File "d:\The Codes\100-days-python-pro-bootcamp\Hari 2\main.py", line 1, in <module>
        print("jumlah karakter: " + len("manusia"))
          ~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~
    TypeError: can only concatenate str (not "int") to str
    ```

    ```python
    print("jumlah karakter: " + str(len("manusia"))) ✔️
    ```
- Tipe Data
- Operasi Matematika di Python
    ```
    operator pembagi menjadi 'int' tanpa desimal => //  
    operator kuadrat => **
    ```
- Manipulasi Angka dan f-string di Python


## 1. Latihan BMI Calculator (operasi matematika)
Indeks massa tubuh (BMI) adalah ukuran yang digunakan dalam kedokteran untuk melihat apakah seseorang kekurangan berat badan atau kelebihan berat badan. Ini adalah rumus yang digunakan untuk menghitungnya:

BMI sama dengan berat badan seseorang dibagi dengan kuadrat tinggi badan orang tersebut.

Konversikan kalimat tersebut menjadi kode pada baris bmi = \
Gunakan operator `round(variabel, 2)` untuk membulatkan desimal di belakang angka

```python
height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi =

print(bmi)
```
