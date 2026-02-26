"""
    Tip Calculator
    Membuat sebuah tip kalkulator, jadi aplikasi ini akan menghitung berapa jumlah tagihan yang akan di split sesuai dengan jumlah orang yang ada.
    Program akan menerima input jumlah tagihan, kemudian persentase tip yang akan diberikan (10, 12, dan 15), dan yang terakhir adalah jumlah orang yang dibagi.
"""

print("Selamat datang di program tip kalkulator?")
tagihan = int(input("Berapa total tagihan? Rp\n"))
tips = int(input("Berapa tips yang ingin diberikan? 10, 12, atau 15\n"))
orang = int(input("Total bayar akan dibagi berapa orang?\n"))
final = round((tagihan + (tagihan*(tips/100)))/orang,2)
print(f"Masing-masing harus bayar: Rp{final}")