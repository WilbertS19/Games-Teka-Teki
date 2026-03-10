from game import check_guess
import random

secret_number = random.randint(1, 10)

print("=== Permainan Tebak Angka ===")
print("Tebak angka dari 1 sampai 10")

while True:
    guess = int(input("Masukkan tebakan angka: "))

    result = check_guess(secret_number, guess)

    if result == "Terlalu kecil":
        print("Angkanya terlalu kecil, coba lagi!")

    elif result == "Terlalu besar":
        print("Angkanya terlalu besar, coba lagi!")

    else:
        print("Selamat! Tebakan kamu benar 🎉")
        break