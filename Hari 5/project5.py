huruf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
angka = ['1','2','3','4','5','6','7','8','9']
simbol = ['~', '!','@','#','$','%','^','&','*','(',')','+','<','>']

print("Selamat datang di PyPassword Generator.")
jml_huruf = int(input("Berapa banyak huruf yang kamu inginkan dalam password?\n"))
jml_angka = int(input("Berapa banyak angka yang kamu inginkan dalam password?\n"))
jml_simbol = int(input("Berapa banyak simbol yang kamu inginkan dalam password?\n"))

password_list = []
import random

for sandi in range(jml_huruf):
    password_list += random.choice(huruf)
    # print(password)

for sandi in range(jml_angka):
    password_list += random.choice(angka)
    # print(password)

for sandi in range(jml_simbol):
    password_list += random.choice(simbol)

random.shuffle(password_list)
# print(password_list)

password_string = ""
for sandi in password_list:
    password_string += sandi

print(f"Password baru anda: {password_string}")