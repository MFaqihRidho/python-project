nomor = int(input("Nomor Berapa: "))

def dot():
    global nomor
    global num
    if len(nomor) > 3:
        num.insert(-3,".")
        if len(nomor) > 6:
            num.insert(-7,".")
            if len(nomor) > 9:
                num.insert(-11,".")

def dot2():
    global kali
    global kal
    if len(kali) > 3:
        kal.insert(-3,".")
        if len(kali) > 6:
            kal.insert(-7,".")
            if len(kali) > 9:
                kal.insert(-11,".")



if nomor > 1:
    for i in range(2,nomor):
        if (nomor % i == 0):
            kali = nomor // i
            nomor = str(nomor)
            num = list(nomor)
            kali = str(kali)
            kal = list(kali)
            dot()
            dot2()
            n = "".join(num)
            k = "".join(kal)
            print("Bukan bilangan prima")
            print(i,"kali",k,"=", n)
            break
    else:
        nomor = str(nomor)
        num = list(nomor)
        dot()
        n = "".join(num)
        print(n," adalah bilangan prima")
else:
    print("Bukan bilangan prima")





