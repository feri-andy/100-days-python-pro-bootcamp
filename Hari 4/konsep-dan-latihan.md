# Hari 4: Pengacakan dan Daftar Python

## Konsep yang Dipraktikkan
- Modul `random`
    ```python
    import random #wajib

    random.random() #angka float acak 0.0 hingga 1.0
    random.randint(a,b) #angka bilangan bulat (integer) acak antara a dan b
    random.choice(sequence) #pilih 1 secara acak dari list, tuple atau string
    random.shuffle(list) #acak urutan elemen dalam list
    random.sample(list,k) #ambil k elemen secara acak dari sebuah list
    ```
- Memahami Offset dan Menambahkan Item ke `list`\
    `list` = struktur data\
    [dokumentasi list](https://docs.python.org/3.13/library/stdtypes.html#list.append)
    ```python
    hewan = ["angsa", "bebek", "cumi"]

    # memberikan perubahan pada index [] item list
    hewan [1] = "keledai"
    # output list ["kuda", "keledai", "bebek"]

    # menambahkan item di akhir list
    hewan.append("badak")
    # output list ["kuda", "kelinci", "badak"]

    # menambahkan elemen dari daftar lain ke daftar
    hewan2 = ["lalat", "mamalia"]
    hewan.extend(hewan2)
    # output list ["angsa", "bebek", "cumi", "lalat", "mamalia"]

    # metode lain
    insert()
    remove()
    sort()
    reverse()
    sort()
    ```
- Kesalahan Indeks dan Bekerja dengan `nested list`\
    nested list = struktur data dimana sebuah list berisi list lain sebagai elemennya (sublist)
    ```python
    # kesalahan IndexError: list index out of range terjadi karena memanggil item di luar scope list.
    hewan = ["angsa", "bebek", "cumi"]
    print(hewan[5]) ❌ # tidak ada item pada index 5
    print(hewan[2]) ✔️ # item pada index 2 adalah cumi

    # Contoh Nested List
    fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
    vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

    dirty_dozen = [fruits, vegetables]

    # Mengakses "Kale"
    print(dirty_dozens[1][1]) 

    # penjelasan:
    # index [1] pertama adalah list vegetables
    # index [1] kedua adalah index [1] atau item ke-2 dari list vegetables

    ```

## Latihan 1: coin flip
Buat program pelemparan koin menggunakan apa yang telah Anda pelajari tentang pengacakan di Python. Program ini harus secara acak mencetak "Kepala" atau "Ekor" setiap kali dijalankan.

## Latihan 2: Banker Roulette
Cari tahu cara memilih nama secara acak dari daftar teman.
```python
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# opsi 1 > random.randint
# opsi 2 > random.choice
```