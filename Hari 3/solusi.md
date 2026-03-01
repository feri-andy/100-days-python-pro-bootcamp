## Solusi Latihan 2
Jika BMI lebih besar atau sama dengan 25, maka akan dicetak "overweight".

Jika pemeriksaan pertama benar, kode akan berhenti berjalan, tetapi jika kondisi pertama salah maka akan dilakukan pemeriksaan elif berikutnya untuk melihat apakah lebih besar atau sama dengan 18,5. Jadi, jika tidak lebih besar dari 25 dan lebih besar dari 18,5, maka rentang 18,5-25 akan dicetak "normal".

Segala sesuatu yang lain akan berada di bawah 18,5 dan itu akan dicetak "underweight".
```python
    weight = 85
    height = 1.85
    
    bmi = weight / (height ** 2)
    
    if bmi >= 25:
        print("overweight")
    elif bmi >= 18.5:
        print("normal")
    else:
        print("underweight")
```

## Solusi Latihan 3
```python
    print("Selamat datang di Pizza Hat")
size = input("Pizza ukuran apa yang ingin anda pesan? S, M, atau L: ")
pepperoni = input("Apa anda menginginkan tambahan pepperoni? Y atau N: ")
ekstra_keju = input("Apa anda menginginkan ekstra keju? Y atau N: ")
total_harga = 0

# blok statement mencari tahu tagihan berdasarkan ukuran pesanan
if size == "S":
    total_harga += 15
elif size == "M":
    total_harga += 20
elif size == "L":
    total_harga += 25
else:
    print("Salah input.")

# blok statement mencari tahu tambahan tagihan berdasar pilihan pepperoni
if pepperoni == "Y":
    if size == "S":
        total_harga += 2
    else:
        total_harga += 3

# blok statement mencari tahu tambahan tagihan berdasar ekstra keju
if ekstra_keju == "Y":
        total_harga += 1
    
print(f"Total harga yang harus anda bayar: {total_harga}")
```