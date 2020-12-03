import random

rps = ['Gunting','Batu','Kertas']
komputer_menang = 0
kamu_menang = 0

def win():
    global kamu_menang
    kamu_menang += 1
    print(f"\nKamu:{kamu_menang} vs Computer:{komputer_menang}\n")

def lose():
    global komputer_menang
    komputer_menang += 1
    print(f"\nKamu:{kamu_menang} vs Computer:{komputer_menang}\n")

def tie():
    print(f"\nKamu:{kamu_menang} vs Computer:{komputer_menang}\n")


main = True

while main:
    terpilih = random.choice(rps)
    pilih = int(input("1.Gunting\n2.Batu\n3.Kertas\n4.Udahan\nPilih salah satu: "))

    if pilih == 1:
        if terpilih == rps[0]:
            print(f"\nGunting vs {terpilih}\nSeri!")
            tie()
        if terpilih == rps[1]:
            print(f"\nGunting vs {terpilih}\nKamu kalah!")
            lose()
        if terpilih == rps[2]:
            print(f"\nGunting vs {terpilih}\nKamu menang!")
            win()

    if pilih == 2:
        if terpilih == rps[0]:
            print(f"\nBatu vs {terpilih}\nKamu menang!")
            win()
        if terpilih == rps[1]:
            print(f"\nBatu vs {terpilih}\nSeri!")
            tie()
        if terpilih == rps[2]:
            print(f"\nBatu vs {terpilih}\nKamu kalah!")
            lose()

    if pilih == 3:
        if terpilih == rps[0]:
            print(f"\nKertas vs {terpilih}\nKamu kalah!")
            lose()
        if terpilih == rps[1]:
            print(f"\nKertas vs {terpilih}\nKamu menang!")
            win()
        if terpilih == rps[2]:
            print(f"\nKertas vs {terpilih}\nSeri!")
            tie()
    
    if pilih == 4:
        main = False











