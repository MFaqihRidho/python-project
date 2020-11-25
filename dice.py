
import pygame
from pygame.locals import *
import random
#Untuk layar
pygame.init()
height = 500
screen = pygame.display.set_mode((height,height))
#Untuk Loop
running = True
#Import gambarnya
dice_1 = pygame.image.load("images/1.png")
dice_2 = pygame.image.load("images/2.png")
dice_3 = pygame.image.load("images/3.png")
dice_4 = pygame.image.load("images/4.png")
dice_5 = pygame.image.load("images/5.png")
dice_6 = pygame.image.load("images/6.png")

dice_1 = pygame.transform.scale(dice_1,(300,300))
dice_2 = pygame.transform.scale(dice_2,(300,300))
dice_3 = pygame.transform.scale(dice_3,(300,300))
dice_4 = pygame.transform.scale(dice_4,(300,300))
dice_5 = pygame.transform.scale(dice_5,(300,300))
dice_6 = pygame.transform.scale(dice_6,(300,300))
#Background
background = pygame.image.load("images/green.png")
background = pygame.transform.scale(background,(500,500))
#Random
pilih = [dice_1,dice_2,dice_3,dice_4,dice_5,dice_6]
pilih2 = [dice_2,dice_1,dice_4,dice_3,dice_6,dice_5]
terpilih = random.choice(pilih)
terpilih2 = random.choices(pilih2)
def tampil_1(x):
    screen.blit(x,(100,0))
def tampil_2(x):
    screen.blit(x,(100,200))
def terpilih_1():
    if terpilih == pilih[0]:
        tampil_1(terpilih)
    elif terpilih == pilih[1]:
        tampil_1(terpilih)
    elif terpilih == pilih[2]:
        tampil_1(terpilih)
    elif terpilih == pilih[3]:
        tampil_1(terpilih)
    elif terpilih == pilih[4]:
        tampil_1(terpilih)
    elif terpilih == pilih[5]:
        tampil_1(terpilih)
def terpilih_2():
    if terpilih2 == pilih2[0]:
        tampil_2(terpilih2)
    elif terpilih2 == pilih2[1]:
        tampil_2(terpilih2)
    elif terpilih2 == pilih2[2]:
        tampil_2(terpilih2)
    elif terpilih2 == pilih2[3]:
        tampil_2(terpilih2)
    elif terpilih2 == pilih2[4]:
        tampil_2(terpilih2)
    elif terpilih2 == pilih2[5]:
        tampil_2(terpilih2)

#Loop
while running == True:
    screen.fill(0)
    screen.blit(background,(0,0))
    terpilih_1()
    terpilih_2()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pilih = [dice_1,dice_2,dice_3,dice_4,dice_5,dice_6]
            terpilih = random.choice(pilih)
            terpilih2 = random.choice(pilih)
        #event saat tombol exit di klik
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)