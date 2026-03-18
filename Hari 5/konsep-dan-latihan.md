# Hari 5: Python Loops

## Konsep yang Dipraktikkan
- Menggunakan  `for` loops dengan List Python
> digunakan untuk mengiterasi urutan (list, tuple, string, dictionary, set) atau objek iterable lainnya, menjalankan blok kode berulang kali untuk setiap item
```python
# Iterasi melalui list
buah = ["apel", "pisang", "ceri"]
for b in buah:
    print(b)

# Iterasi melalui string
for karakter in "Python":
    print(karakter)

```
- Perulangan `for` dan fungsi ```range()```
``` python
# Mengulang 5 kali (0-4)
for i in range(5):
    print(i)

# Mengulang dengan langkah/step (genap 0-10)
for i in range(0, 11, 2):
    print(i)
```

⚠️ Indentasi sangat penting!!!

## Latihan: 
Mencari Skor Tertinggi
```python
student_scores = [180, 124, 165, 173, 189, 169, 146]

# menggunakan operator 'max'
```

The Gauss Challenge
```python
# cari tahu jumlah angka dari 1 sampai dengan 100, termasuk dengan angka 1 dan 100.
# 1+2+3+4+5+6+7+.....+95+96+97+98+99+100 = ?
```
## Quizz: FizzBuzz
Tulis program yang secara otomatis mencetak solusi permainan FizzBuzz. Berikut adalah aturan permainan FizzBuzz:
- Program Anda harus mencetak setiap angka dari 1 hingga 100 secara berurutan, termasuk angka 100.
- Namun, jika angka tersebut habis dibagi 3, maka alih-alih mencetak angka, seharusnya mencetak "Fizz".
- Jika angka tersebut habis dibagi 5, maka alih-alih mencetak angka, seharusnya mencetak "Buzz".
- Dan jika angka tersebut habis dibagi 3 dan 5, misalnya 15, maka alih-alih angka tersebut, seharusnya dicetak "FizzBuzz".
- Contoh output:
```python
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```