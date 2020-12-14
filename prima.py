nomor = int(input("Nomor Berapa"))



if nomor > 1:
    for i in range(2,nomor):
        if (nomor % i == 0):
            print("Bukan bilangan prima")
            print(i,"kali",nomor // i,"=", nomor)
            break
    else:
        print(nomor," adalah bilangan prima")
else:
    print("Bukan bilangan prima")
