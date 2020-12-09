#Global Variable
Papan = ["-","-","-",
         "-","-","-",
         "-","-","-"]

play = True

pemenang = None

player = "X"

def Display_Papan():
    print(Papan[0] + " | " + Papan[1] + " | " + Papan[2])
    print(Papan[3] + " | " + Papan[4] + " | " + Papan[5])
    print(Papan[6] + " | " + Papan[7] + " | " + Papan[8])

def Giliran():


    print("Giliran " + player)
    posisi = input("Pilih posisi nya 1 sampai 9: ")


    valid = False
    while not valid:

        while posisi not in ["1","2","3","4","5","6","7","8","9"]:
            posisi = input("Masukan nomor dari 1 sampai 9: ")

        posisi = int(posisi) - 1

        if Papan[posisi] == "-":
            valid = True
        else:
            print("kamu tidak bisa kesana")

    Papan[posisi] = player
    Display_Papan()

def Main_Game():
    Display_Papan()

    global play

    while play == True:
        Giliran()

        Game_over()

        Ganti_player()

        cek()

    # if pemenang == "X" or pemenang == "O":
    #     pass
    # elif pemenang == "Tie":
    #     pass


def Game_over():
    cek_menang()
    cek_seri()


def cek_menang():
    global pemenang

    baris_menang = cek_baris()

    kolom_menang = cek_kolom()

    diagonal_menang = cek_diagonal()

    if baris_menang:
        pemenang = baris_menang
    elif kolom_menang:
        pemenang = kolom_menang
    elif diagonal_menang:
        pemenang = diagonal_menang

def cek_seri():
    global play
    global pemenang

    if "-" not in Papan:
        play = False
        pemenang = "Tie"
    return
        

def Ganti_player():
    global player

    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"

def cek_baris():
    global play

    baris_1 = Papan[0] == Papan[1] == Papan[2] != "-"
    baris_2 = Papan[3] == Papan[4] == Papan[5] != "-"
    baris_3 = Papan[6] == Papan[7] == Papan[8] != "-"
    if baris_1 or baris_2 or baris_3:
        play = False

    if baris_1:
        return Papan[0]
    elif baris_2:
        return Papan[3]
    elif baris_3:
        return Papan[6]
    return


def cek_kolom():
    global play

    kolom_1 = Papan[0] == Papan[3] == Papan[6] != "-"
    kolom_2 = Papan[1] == Papan[4] == Papan[7] != "-"
    kolom_3 = Papan[2] == Papan[5] == Papan[8] != "-"
    if kolom_1 or kolom_2 or kolom_3:
        play = False

    if kolom_1:
        return Papan[0]
    elif kolom_2:
        return Papan[1]
    elif kolom_3:
        return Papan[2]
    return

def cek_diagonal():
    global play

    diagonal_1 = Papan[0] == Papan[4] == Papan[8] != "-"
    diagonal_2 = Papan[2] == Papan[4] == Papan[6] != "-"
    if diagonal_1 or diagonal_2:
        play = False

    if diagonal_1:
        return Papan[0]
    elif diagonal_2:
        return Papan[2]
    return

def pembersih():
    global pemenang
    pemenang = None
    global Papan
    Papan = ["-","-","-",
             "-","-","-",
             "-","-","-"]
    global play
    play = True 

def cek():
    if pemenang != None:
        if pemenang == "Tie":
            print(pemenang)
            cek = input("Mau main lagi ga? (y/g): ").lower()
            if cek == "y":
                pembersih()
                Main_Game()
        else:
            print(pemenang,"Menang!")
            cek = input("Mau main lagi ga? (y/g): ").lower()
            if cek == "y":
                pembersih()
                Main_Game()

Main_Game()







papan_1 = [-200,-200]
papan_2 = [0,-200]
papan_3 = [200,-200]
papan_4 = [-200,0]
papan_5 = [0,0]
papan_6 = [200,0]
papan_7 = [-200,200]
papan_8 = [0,200]
papan_9 = [200,200]
















#Papan
#Display papan
#Main Game
#Giliran
#Ganti player
#Cek menang:
    #Cek baris
    #Cek Kolom
    #Cek Diagonal
#Cek Seri





