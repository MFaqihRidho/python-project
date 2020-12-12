#1 Import Liblary
import pygame
from pygame.locals import *
import math
from random import randint

#2 Initialize Game
pygame.init()
height,width = 640,480
screen = pygame.display.set_mode((height,width))
icon = pygame.image.load("resources/images/shooting.png")
pygame.display.set_caption("Shooting Game")
pygame.display.set_icon(icon)
health_point = 194
countdown_timer = 90000

#Key mapping
keys = {"top" : False,"bottom" : False,"right" : False,"left" : False}

running = True

player_pos = [150,200] #posisi player

#exit code untuk win dan lose
exitcode = 0
EXIT_CODE_GAME_OVER = 0
EXIT_CODE_WIN = 1 

score = 0
bullets = [] #list Bulletnya

enemy_timer = 100 #waktu kemunculan
enemies = [[width,100]] #untuk menampun kordinat musuh

#3 Load game assets
#3.1 Load images
player = pygame.image.load("resources/images/player.png")
grass = pygame.image.load("resources/images/grass.png")
tanks = pygame.image.load("resources/images/tanks.png")
bulletss = pygame.image.load("resources/images/bullet.png")
zombie = pygame.image.load("resources/images/zombie 1.png")
health = pygame.image.load("resources/images/health.png")
health_bar = pygame.image.load("resources/images/healthbar.png")
win = pygame.image.load("resources/images/youwin.png")
lose = pygame.image.load("resources/images/gameover.png")
blood = pygame.image.load("resources/images/blood.png")

player = pygame.transform.scale(player,(100,100))
tanks = pygame.transform.scale(tanks,(400,400))
bulletss = pygame.transform.scale(bulletss,(85,85))
zombie = pygame.transform.scale(zombie,(100,100))
zombie = pygame.transform.flip(zombie,True,False)
blood = pygame.transform.scale(blood,(100,100))

#3.2 Load sound
pygame.mixer.init()
hit_sound = pygame.mixer.Sound("resources/audio/explode.wav")
enemy_hit_sound = pygame.mixer.Sound("resources/audio/zombie-17.wav")
shoot_sound = pygame.mixer.Sound("resources/audio/pistol.wav")
win_sound = pygame.mixer.Sound("resources/audio/you win.wav")
lose_sound = pygame.mixer.Sound("resources/audio/you lose.wav")

hit_sound.set_volume(0.05)
enemy_hit_sound.set_volume(0.05)
shoot_sound.set_volume(0.05)
win_sound.set_volume(0.5)
lose_sound.set_volume(0.5)

#Background Music
pygame.mixer.music.load("resources/audio/Battle.wav")
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(0.25)



#4 loop game

while running == True:
    #5 Clear screen
    screen.fill(0) 

    #6 Draw the game object
    #Draw The grass
    for x in range(int(width/grass.get_width()+2.5)):
        for y in range (int(height/grass.get_height()+1)):
            screen.blit(grass,(x * 100,y * 100))
    
    #Draw the bullets
    for bullet in bullets:
        bullet_index = 0
        velx=math.cos(bullet[0])*10
        vely=math.sin(bullet[0])*10
        bullet[1]+=velx
        bullet[2]+=vely
        if bullet[1] < -64 or bullet[1] > width or bullet[2] < -64 or bullet[2] > height:
            bullets.pop(bullet_index)
        bullet_index += 1
        #draw bulletss
        for projectile in bullets:
            new_bullet = pygame.transform.rotate(bulletss, 360-projectile[0]*57.29)
            screen.blit(new_bullet,(projectile[1],projectile[2]))

    #Draw enemy
    # waktu musuh akan dimulai
    enemy_timer -= 1
    if enemy_timer == 0:
        #buat musuh
        enemies.append([width,randint(50,height-200)])
        #reset enemy timer
        enemy_timer = randint(1,150)

    index = 0
    for enemy in enemies:
        #musuh bergerak dengan kecepatan 5 pixel ke kiri
        enemy[0] -= 2
        #Hapus musuh saat mencapai batas layar sebelah kiri
        if enemy[0] < 64:
            enemies.pop(index)

        #Benturan zombie dan tank
        enemy_rect = pygame.Rect(zombie.get_rect())
        enemy_rect.top = enemy[1] #ambil titik y
        enemy_rect.left = enemy[0] #ambil titik x
        if enemy_rect.left < 64:
            enemy.pop(index)
            health_point -= randint(5,15)
            hit_sound.play()
            print("Oh tidak ,kita diserang!!")

        #Benturan peluru dengan zombie
        index_bullet = 0
        for bullet in bullets:
            bullet_rect = pygame.Rect(bulletss.get_rect())
            bullet_rect.left = bullet[1]
            bullet_rect.top = bullet[2]
            if enemy_rect.colliderect(bullet_rect):
                score += 1
                enemies.pop(index)
                bullets.pop(index_bullet)
                enemy_hit_sound.play()
                screen.blit(blood,enemy_rect)
                print("Mati kau!!")
                print("Score : {}".format(score))
            index_bullet += 1
        index += 1



    #gambar musuh ke layar
    for enemy in enemies:
        screen.blit(zombie,enemy)

    #Draw HealthBar
    screen.blit(health_bar,(5,5))
    for hp in range(health_point):
        screen.blit(health,(hp + 8,8))

    #Draw clock
    font = pygame.font.Font(None,24)
    minutes = int((countdown_timer - pygame.time.get_ticks())/ 60000) # = 60 detik
    seconds = int((countdown_timer - pygame.time.get_ticks())/ 1000 % 60)
    time_text = "{:02}:{:02}".format(minutes,seconds)
    clock = font.render(time_text,True,(255,255,255))
    textRect = clock.get_rect()
    textRect.topright = [635,5]
    screen.blit(clock,textRect)


    #Draw the Tanks
    screen.blit(tanks,(-135,-50))
    screen.blit(tanks,(-135,125))

    #Draw the player
    mouse_posisiton = pygame.mouse.get_pos()
    angle = math.atan2(mouse_posisiton[1] - (player_pos[1]+32),mouse_posisiton[0] - (player_pos[0]+26))
    player_rotation = pygame.transform.rotate(player,360 - angle * 57.29)
    new_player_pos = (player_pos[0] - player_rotation.get_rect().width / 2,player_pos[1] - player_rotation.get_rect().height / 2)
    screen.blit(player_rotation,new_player_pos)
    

    #7 Update The screen
    pygame.display.flip()

    #8 Event Loop
    for event in pygame.event.get():
        #event saat tombol exit di klik
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        #Fire
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullets.append([angle,new_player_pos[0]+32,new_player_pos[1]+32])
            shoot_sound.play()

        #check the keydown and keyup
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys["top"] = True
            elif event.key == K_s:
                keys["bottom"] = True
            elif event.key == K_d:
                keys["right"] = True
            elif event.key == K_a:
                keys["left"] = True
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                keys["top"] = False
            elif event.key == K_s:
                keys["bottom"] = False
            elif event.key == K_d:
                keys["right"] = False
            elif event.key == K_a:
                keys["left"] = False

    #End of event loop
    if keys["top"]:
        player_pos[1] -= 3 #kurangi nilai y
    elif keys["bottom"]:
        player_pos[1] += 3 #tambah nilai y
    elif keys["left"]:
        player_pos[0] -= 3 #kurangi nilai x
    elif keys["right"]:
        player_pos[0] += 3 #tambah nilai x   

    #10 Win lose check
    if pygame.time.get_ticks() > countdown_timer:
        running = False
        exitcode = EXIT_CODE_WIN
        win_sound.play()
    if health_point <= 0:
        running = False
        exitcode = EXIT_CODE_GAME_OVER
        lose_sound.play()

#End of game loop


#11 win/lose display
if exitcode == EXIT_CODE_GAME_OVER:
    screen.blit(lose,(0,0))
else:
    screen.blit(win,(0,0))

#Tampilkan score
text = font.render("Score : {}".format(score),True,(255,255,255))
textRect = text.get_rect()
textRect.centerx = screen.get_rect().centerx
textRect.centery = screen.get_rect().centery + 23
screen.blit(text,textRect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()



        

















