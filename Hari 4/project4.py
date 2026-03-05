batu ='''
          _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)
'''

gunting ='''
          _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)
'''

kertas ='''
          _______
      ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________)
'''

import random

print("Ketik 0 untuk Batu, 1 untuk Kertas, 2 untuk Gunting")
batu_kertas_gunting = [batu, kertas, gunting]
user_input = int(input("Pilihan user adalah: "))
if user_input >= 3 or user_input <= -1:
    print("salah input. kamu kalah.")
else:
    print(batu_kertas_gunting[user_input])

    comp_choice = random.randint(0, 2)
    print(f"Pilihan komputer adalah: {batu_kertas_gunting[comp_choice]}")
    if user_input == 0 and comp_choice == 2:
        print("kamu menang")
    elif comp_choice == 0 and user_input == 2:
        print("kamu kalah")
    elif comp_choice > user_input:
        print("kamu kalah")
    elif user_input > comp_choice:
        print("kamu menang")
    else:
        print("seri")