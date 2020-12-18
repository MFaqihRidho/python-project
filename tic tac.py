#Import
import pygame
from pygame.locals import *

#Untuk Layar
pygame.init()
height = 720
screen = pygame.display.set_mode((height,height))
pygame.display.set_caption("Tic Tac Toe")
icon = pygame.image.load("Images/icon.png")
pygame.display.set_icon(icon)
#Untuk loop
Running = True

#masukin gambar
#Papan
board = pygame.image.load("Images/Board.png")
#X Dan O
#X
x = pygame.image.load("Images/x5.png")
x_turn = pygame.image.load("Images/x turn.png")
x_win = pygame.image.load("Images/x win.png")
#O
o = pygame.image.load("Images/o5.png")
o_turn = pygame.image.load("Images/o turn.png")
o_win = pygame.image.load("Images/o win.png")
#reset
Reset = pygame.image.load("Images/Reset.png")
#State
state1 = False
state2 = False
state3 = False
state4 = False
state5 = False
state6 = False
state7 = False
state8 = False
state9 = False
statex = False
statex_turn = False
stateo = False
stateo_turn = False
state_reset = False
#count
count1 = False
count2 = False
count3 = False
count4 = False
count5 = False
count6 = False
count7 = False
count8 = False
count9 = False
#Baris
baris_1 = pygame.image.load("Images/Baris 1.png")
baris_2 = pygame.image.load("Images/Baris 2.png")
baris_3 = pygame.image.load("Images/Baris 3.png")
state_baris_1_x = False
state_baris_1_o = False
state_baris_2_x = False
state_baris_2_o = False
state_baris_3_x = False
state_baris_3_o = False
#Kolom
kolom_1 = pygame.image.load("Images/kolom 1.png")
kolom_2 = pygame.image.load("Images/kolom 2.png")
kolom_3 = pygame.image.load("Images/kolom 3.png")
state_kolom_1_x = False
state_kolom_1_o = False
state_kolom_2_x = False
state_kolom_2_o = False
state_kolom_3_x = False
state_kolom_3_o = False
#Diagonal
diagonal_1 = pygame.image.load("Images/Diagonal 1.png")
diagonal_2 = pygame.image.load("Images/Diagonal 2.png")
state_diagonal_1_x = False
state_diagonal_1_o = False
state_diagonal_2_x = False
state_diagonal_2_o = False
#Background
background = pygame.image.load("images/green.png")
#Lokasi
lok_papan = [-200,-200],[0,-200],[200,-200],[-200,0],[0,0],[200,0],[-200,200],[0,200],[200,200]
#Ganti player
current_player = "o"
player = x
player_2 = x
player_3 = x
player_4 = x
player_5 = x
player_6 = x
player_7 = x
player_8 = x
player_9 = x
#win
win = False

#Def
def tampil(gambar,lokasi):
    screen.blit(gambar,lokasi)

def tampilin(state,gambar,lokasi):
    if state is True:
        tampil(gambar,lokasi)

def tampil_player():
    tampilin(state1,player,lok_papan[0])
    tampilin(state2,player_2,lok_papan[1])
    tampilin(state3,player_3,lok_papan[2])
    tampilin(state4,player_4,lok_papan[3])
    tampilin(state5,player_5,lok_papan[4])
    tampilin(state6,player_6,lok_papan[5])
    tampilin(state7,player_7,lok_papan[6])
    tampilin(state8,player_8,lok_papan[7])
    tampilin(state9,player_9,lok_papan[8])

def tampil_win():
    tampilin(statex,x_win,(0,0))
    tampilin(stateo,o_win,(0,0))

def tampil_turn_x():
    global statex_turn
    if stateo == True or statex == True:
        statex_turn = False
    elif current_player == "o":
        statex_turn = True
    elif current_player == "x":
        statex_turn = False

def tampil_turn_o():
    global stateo_turn
    if stateo == True or statex == True:
        stateo_turn = False
    elif current_player == "x":
        stateo_turn = True
    elif current_player == "o":
        stateo_turn = False

def tampil_turn():
    tampil_turn_x()
    tampilin(statex_turn,x_turn,(0,0))
    tampil_turn_o()
    tampilin(stateo_turn,o_turn,(0,0))

def berhenti():
    global win
    if statex == True or stateo == True:
        win = True

def ganti():
    global current_player
    if current_player == "o":
        current_player = "x"
    elif current_player == "x":
        current_player = "o"

def ganti2():
    global current_player
    if current_player == "o":
        current_player = "x"
    elif current_player == "x":
        current_player = "o"

def ganti3():
    global current_player
    if current_player == "o":
        current_player = "x"
    elif current_player == "x":
        current_player = "o"

def ganti4():
    global current_player
    if current_player == "o":
        current_player = "x"
    elif current_player == "x":
        current_player = "o"

def ganti5():
    global current_player
    if current_player == "o":
        current_player = "x"
    elif current_player == "x":
        current_player = "o"

def ganti6():
    global current_player
    if current_player == "o":
        current_player = "x"
    elif current_player == "x":
        current_player = "o"

def ganti7():
    global current_player
    if current_player == "o":
        current_player = "x"
    elif current_player == "x":
        current_player = "o"

def ganti8():
    global current_player
    if current_player == "o":
        current_player = "x"
    elif current_player == "x":
        current_player = "o"

def ganti9():
    global current_player
    if current_player == "o":
        current_player = "x"
    elif current_player == "x":
        current_player = "o"


def Ganti_player_1():
    global current_player
    global player
    if current_player == "o":
        player = x
    elif current_player == "x":
        player = o

def Ganti_player_2():
    global current_player
    global player_2
    if current_player == "o":
        player_2 = x
    elif current_player == "x":
        player_2 = o

def Ganti_player_3():
    global current_player
    global player_3
    if current_player == "o":
        player_3 = x
    elif current_player == "x":
        player_3 = o

def Ganti_player_4():
    global current_player
    global player_4
    if current_player == "o":
        player_4 = x
    elif current_player == "x":
        player_4 = o

def Ganti_player_5():
    global current_player
    global player_5
    if current_player == "o":
        player_5 = x
    elif current_player == "x":
        player_5 = o

def Ganti_player_6():
    global current_player
    global player_6
    if current_player == "o":
        player_6 = x
    elif current_player == "x":
        player_6 = o

def Ganti_player_7():
    global current_player
    global player_7
    if current_player == "o":
        player_7 = x
    elif current_player == "x":
        player_7 = o

def Ganti_player_8():
    global current_player
    global player_8
    if current_player == "o":
        player_8 = x
    elif current_player == "x":
        player_8 = o

def Ganti_player_9():
    global current_player
    global player_9
    if current_player == "o":
        player_9 = x
    elif current_player == "x":
        player_9 = o


def tampil_o1():
    global state1
    state1 = True

def tampil_o2():
    global state2
    state2 = True

def tampil_o3():
    global state3
    state3 = True

def tampil_o4():
    global state4
    state4 = True

def tampil_o5():
    global state5
    state5 = True

def tampil_o6():
    global state6
    state6 = True
    
def tampil_o7():
    global state7
    state7 = True

def tampil_o8():
    global state8
    state8 = True

def tampil_o9():
    global state9
    state9 = True

def tampil_reset():
    global state_reset
    if statex == True or stateo == True:
        state_reset = True
        tampilin(state_reset,Reset,(0,0))

def reset1():
    global state1
    global state2
    global state3
    global state4
    global state5
    global state6
    global state7
    global state8
    global state9
    global statex
    global stateo
    global win
    global current_player
    global state_baris_1_x
    global state_baris_1_o
    global state_baris_2_x
    global state_baris_2_o
    global state_baris_3_x
    global state_baris_3_o
    global state_kolom_1_x
    global state_kolom_1_o
    global state_kolom_2_x
    global state_kolom_2_o
    global state_kolom_3_x
    global state_kolom_3_o
    global state_diagonal_1_x
    global state_diagonal_1_o
    global state_diagonal_2_x
    global state_diagonal_2_o
    global count1
    global count2
    global count3
    global count4
    global count5
    global count6
    global count7
    global count8
    global count9
    if stateo == True or statex == True:
        state1 = False
        state2 = False
        state3 = False
        state4 = False
        state5 = False
        state6 = False
        state7 = False
        state8 = False
        state9 = False
        statex = False
        stateo = False
        count1 = False
        count2 = False
        count3 = False
        count4 = False
        count5 = False
        count6 = False
        count7 = False
        count8 = False
        count9 = False
        state_baris_1_x = False
        state_baris_1_o = False
        state_baris_2_x = False
        state_baris_2_o = False
        state_baris_3_x = False
        state_baris_3_o = False
        state_kolom_1_x = False
        state_kolom_1_o = False
        state_kolom_2_x = False
        state_kolom_2_o = False
        state_kolom_3_x = False
        state_kolom_3_o = False
        state_diagonal_1_x = False
        state_diagonal_1_o = False
        state_diagonal_2_x = False
        state_diagonal_2_o = False
        win = False
        if current_player == "o":
            current_player = "o"
        elif current_player == "x":
            current_player = "x"

def count():
    global count1
    count1 = True

def baris_1_x():
    global statex
    global state_baris_1_x
    if state1 == True and state2 == True and state3 == True:
        if player == x and player_2 == x and player_3 == x:
            statex = True
            state_baris_1_x = True

def baris_1_o():
    global stateo
    global state_baris_1_o
    if state1 == True and state2 == True and state3 == True:
        if player == o and player_2 == o and player_3 == o:
            stateo = True
            state_baris_1_o = True

def baris_2_x():
    global statex
    global state_baris_2_x
    if state4 == True and state5 == True and state6 == True:
        if player_4 == x and player_5 == x and player_6 == x:
            statex = True
            state_baris_2_x = True

def baris_2_o():
    global stateo
    global state_baris_2_o
    if state4 == True and state5 == True and state6 == True:
        if player_4 == o and player_5 == o and player_6 == o:
            stateo = True
            state_baris_2_o = True

def baris_3_x():
    global statex
    global state_baris_3_x
    if state7 == True and state8 == True and state9 == True:
        if player_7 == x and player_8 == x and player_9 == x:
            statex = True
            state_baris_3_x = True

def baris_3_o():
    global stateo
    global state_baris_3_o
    if state7 == True and state8 == True and state9 == True:
        if player_7 == o and player_8 == o and player_9 == o:
            stateo = True
            state_baris_3_o = True

def baris():
    baris_1_x()
    tampilin(state_baris_1_x,baris_1,(0,0))
    baris_1_o()
    tampilin(state_baris_1_o,baris_1,(0,0))
    baris_2_x()
    tampilin(state_baris_2_x,baris_2,(0,0))
    baris_2_o()
    tampilin(state_baris_2_o,baris_2,(0,0))
    baris_3_x()
    tampilin(state_baris_3_x,baris_3,(0,0))
    baris_3_o()
    tampilin(state_baris_3_o,baris_3,(0,0))

def kolom_1_x():
    global statex
    global state_kolom_1_x
    if state1 == True and state4 == True and state7 == True:
        if player == x and player_4 == x and player_7 == x:
            statex = True
            state_kolom_1_x = True

def kolom_1_o():
    global stateo
    global state_kolom_1_o
    if state1 == True and state4 == True and state7 == True:
        if player == o and player_4 == o and player_7 == o:
            stateo = True
            state_kolom_1_o = True

def kolom_2_x():
    global statex
    global state_kolom_2_x
    if state2 == True and state5 == True and state8 == True:
        if player_2 == x and player_5 == x and player_8 == x:
            statex = True
            state_kolom_2_x = True

def kolom_2_o():
    global stateo
    global state_kolom_2_o
    if state2 == True and state5 == True and state8 == True:
        if player_2 == o and player_5 == o and player_8 == o:
            stateo = True
            state_kolom_2_o = True

def kolom_3_x():
    global statex
    global state_kolom_3_x
    if state3 == True and state6 == True and state9 == True:
        if player_3 == x and player_6 == x and player_9 == x:
            statex = True
            state_kolom_3_x = True

def kolom_3_o():
    global stateo
    global state_kolom_3_o
    if state3 == True and state6 == True and state9 == True:
        if player_3 == o and player_6 == o and player_9 == o:
            stateo = True
            state_kolom_3_o = True


def kolom():
    kolom_1_x()
    tampilin(state_kolom_1_x,kolom_1,(0,0))
    kolom_1_o()
    tampilin(state_kolom_1_o,kolom_1,(0,0))
    kolom_2_x()
    tampilin(state_kolom_2_x,kolom_2,(0,0))
    kolom_2_o()
    tampilin(state_kolom_2_o,kolom_2,(0,0))
    kolom_3_x()
    tampilin(state_kolom_3_x,kolom_3,(0,0))
    kolom_3_o()
    tampilin(state_kolom_3_o,kolom_3,(0,0))

def diagonal_1_x():
    global statex
    global state_diagonal_1_x
    if state1 == True and state5 == True and state9 == True:
        if player == x and player_5 == x and player_9 == x:
            statex = True
            state_diagonal_1_x = True

def diagonal_1_o():
    global stateo
    global state_diagonal_1_o
    if state1 == True and state5 == True and state9 == True:
        if player == o and player_5 == o and player_9 == o:
            stateo = True
            state_diagonal_1_o = True

def diagonal_2_x():
    global statex
    global state_diagonal_2_x
    if state3 == True and state5 == True and state7 == True:
        if player_3 == x and player_5 == x and player_7 == x:
            statex = True
            state_diagonal_2_x = True

def diagonal_2_o():
    global stateo
    global state_diagonal_2_o
    if state3 == True and state5 == True and state7 == True:
        if player_3 == o and player_5 == o and player_7 == o:
            stateo = True
            state_diagonal_2_o = True

def diagonal():
    diagonal_1_x()
    tampilin(state_diagonal_1_x,diagonal_1,(0,0))
    diagonal_1_o()
    tampilin(state_diagonal_1_o,diagonal_1,(0,0))
    diagonal_2_x()
    tampilin(state_diagonal_2_x,diagonal_2,(0,0))
    diagonal_2_o()
    tampilin(state_diagonal_2_o,diagonal_2,(0,0))


#Scale object
#papan
board = pygame.transform.scale(board,(720,720))
#X
x = pygame.transform.scale(x,(720,720))
#O
o = pygame.transform.scale(o,(720,720))
#Baris
baris_1 = pygame.transform.scale(baris_1,(720,720))
baris_2 = pygame.transform.scale(baris_2,(720,720))
baris_3 = pygame.transform.scale(baris_3,(720,720))
#Kolom
kolom_1 = pygame.transform.scale(kolom_1,(720,720))
kolom_2 = pygame.transform.scale(kolom_2,(720,720))
kolom_3 = pygame.transform.scale(kolom_3,(720,720))
#Diagonal
diagonal_1 = pygame.transform.scale(diagonal_1,(720,720))
diagonal_2 = pygame.transform.scale(diagonal_2,(720,720))
#background
background = pygame.transform.scale(background,(720,1000))
player = pygame.transform.scale(player,(720,720))


#Get rect
satu = pygame.draw.rect(screen,(255,255,255),(80,80,150,150))
dua = pygame.draw.rect(screen,(255,255,255),(280,80,150,150))
tiga = pygame.draw.rect(screen,(255,255,255),(480,80,150,150))

empat = pygame.draw.rect(screen,(255,255,255),(80,280,150,150))
lima = pygame.draw.rect(screen,(255,255,255),(280,280,150,150))
enam = pygame.draw.rect(screen,(255,255,255),(480,280,150,150))

tujuh = pygame.draw.rect(screen,(255,255,255),(80,480,150,150))
delapan = pygame.draw.rect(screen,(255,255,255),(280,480,150,150))
sembilan = pygame.draw.rect(screen,(255,255,255),(480,480,150,150))

reset = pygame.draw.rect(screen,(255,255,255),(300,10,100,50))

#Loop
while Running == True:
    #mulai layar
    # screen.fill(0)
    # global o
    pygame.time.delay(100)
    
    #Draw object
    tampil(background,(0,0))
    tampil(board,(0,0))
    tampil_player()
    tampil_win()
    tampil_turn()
    tampil_reset()
    baris()
    kolom()
    diagonal()
    berhenti()
    # tampilin(state_reset,Reset,(0,0))


    #screen update
    pygame.display.flip()
    pygame.display.update()

    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            posisi_mouse = pygame.mouse.get_pos()
            if satu.collidepoint(posisi_mouse) and count1 == False and win == False:
                tampil_o1()
                Ganti_player_1()
                ganti()
                count1 = True
            elif dua.collidepoint(posisi_mouse) and count2 == False and win == False:
                tampil_o2()
                Ganti_player_2()
                ganti2()
                count2 = True
            elif tiga.collidepoint(posisi_mouse) and count3 == False and win == False:
                tampil_o3()
                Ganti_player_3()
                ganti3()
                count3 = True
            elif empat.collidepoint(posisi_mouse) and count4 == False and win == False:
                tampil_o4()
                Ganti_player_4()
                ganti4()
                count4 = True
            elif lima.collidepoint(posisi_mouse) and count5 == False and win == False:
                tampil_o5()
                Ganti_player_5()
                ganti5()
                count5 = True
            elif enam.collidepoint(posisi_mouse) and count6 == False and win == False:
                tampil_o6()
                Ganti_player_6()
                ganti6()
                count6 = True
            elif tujuh.collidepoint(posisi_mouse) and count7 == False and win == False:
                tampil_o7()
                Ganti_player_7()
                ganti7()
                count7 = True
            elif delapan.collidepoint(posisi_mouse) and count8 == False and win == False:
                tampil_o8()
                Ganti_player_8()
                ganti8()
                count8 = True
            elif sembilan.collidepoint(posisi_mouse) and count9 == False and win == False:
                tampil_o9()
                Ganti_player_9()
                ganti9() 
                count9 = True
            elif reset.collidepoint(posisi_mouse) and (statex == True or stateo == True):
                reset1()    
            
            















