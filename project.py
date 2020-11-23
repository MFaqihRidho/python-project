print("Selamat datang di game!")

nama = input("Siapa Namamu? ")
umur = int(input("Berapa Umurmu? "))

print(f"Halo {nama} dan kamu berumur {umur}")

if umur >= 15:
    print("Kamu cukup umur untuk memainkan game ini!")
    play = input("Mau main gak?(ya/tidak) ").lower()
    if play == "ya":
        choice_1 = input("Mau ke kanan atau kiri?(kanan/kiri) ").lower()
        if choice_1 == "kanan":
            choice_2 = input("Kamu mau lewat sungai dan berenang atau keliling aja?(berenang/keliling) ").lower()
            if choice_2 == "berenang":
                print("Kamu mati dimakan hiu")
            elif choice_2 == "keliling":
                choice_3 = input("Kamu kecapekan dna kamu melihat rumah dan gua kamu mau kemana?(gua/rumah) ").lower()
                if choice_3 == "rumah":
                    print("Kamu mati karena yang punya rumah gak suka dan bunuh kamu")
                elif choice_3 == "gua":
                    print("Kamu beristrahat di gua dan bangun pagi dan kamu selamat\nselamat kamu menang!")
        elif choice_1 == "kiri":
            print("Kamu Mati jatuh")
        else:
            print("kamu Tersesat")
    else:
        print("Yaudah Dadah")
else:
    print("sekolah bukannya main game!")






