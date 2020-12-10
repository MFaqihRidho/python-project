import random


def Guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Tebak Nomor dari 1 Sampai {x}: "))
        if guess < random_number:
            print("Lebih Tinggi")
        elif guess > random_number:
            print("Lebih Rendah")
    print(f"Selamat Kamu telah menebak Nomor {random_number} Dengan benar")

def Computer_Guess(x):
    low = 1
    high = x
    Guess = random.randint(low,high)
    correct = ""
    while correct != "c":
        if low != high:
            Guess = random.randint(low,high)
        else:
            Guess = low
        correct = input(f"Apakah {Guess} Adalah Nomornya?\nTekan (H) Jika terlalu tinggi\nTekan (L) Jika terlalu Rendah\nTekan (C) Jika Benar: ").lower()
        if correct == "h":
            high = Guess - 1
        elif correct == "l":
            low = Guess + 1
    print(f"Selamat Computer telah menebak Angka {Guess} dengan benar")















