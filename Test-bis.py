import pygame, pygame.mixer, os.path
from pygame.locals import*
import classe_test_up
# Initialise pygame
pygame.init()

# DÃ©finir quelque couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE =  (  0,   0, 255)
GREY = (128, 128, 128)
PURPLE = (98, 14, 104)

# temps:
time = pygame.time.get_ticks()
def timer(time, time1):
    if time1<time+1000:
        z=1
    else:
        z=2
    return(z)

# Mesures de la fenÃªtre
size = [800, 750]
screen = pygame.display.set_mode(size)

#images boutons:
	# coordonnées:
bt1 = x_bt1, y_bt1= (200, 100)	# Titre: Tetris

bt2 = x_bt2, y_bt2= (350,350)	# Play

bt3 = x_bt3, y_bt3= (350, 450)	# Option

bt4 = x_bt4, y_bt4= (345, 550)  # Quitter

	#images associées:

Presentation = pygame.image.load("Images/FIRST.png")
damier = pygame.image.load("Images/Damier_tetris.png")
		# titre Tetris:
T0 = pygame.image.load("Images/Tetris_0.png")
T1 = pygame.image.load("Images/Tetris_1.png")
T2 = pygame.image.load("Images/Tetris_2.png")
T3 = pygame.image.load("Images/Tetris_3.png")
T4 = pygame.image.load("Images/Tetris_4.png")
T5 = pygame.image.load("Images/Tetris_5.png")
t=0
liste = [T0, T1, T2, T3, T4, T5]
		# bouton Play:
play = pygame.image.load("Images/Play_0.png")
play_s1 = pygame.image.load("Images/Play_1.png")
play_s2 = pygame.image.load("Images/Play_2.png")

playlist = [play, play_s1, play_s2]

		# Option:
option = pygame.image.load("Images/Option_0.png")
option_s1 = pygame.image.load("Images/Option_1.png")
option_s2 = pygame.image.load("Images/Option_2.png")

optionlist = [option, option_s1, option_s2]

                # Quitter
quitter = pygame.image.load("Images/quitter_0.png")
quitter_s1 = pygame.image.load("Images/quitter_1.png")
quitter_s2 = pygame.image.load("Images/quitter_2.png")

quit_list = [quitter, quitter_s1, quitter_s2]

                # retour

back = pygame.image.load("Images/Back_0.png")
back_s1 = pygame.image.load("Images/Back_1.png")
back_s2 = pygame.image.load("Images/Back_2.png")

back_list = [back_s1, back_s2]

nbr_touch = 0    #bouton sélectionné

    #son

son_base1 = pygame.mixer.Sound("Sons/g.wav")
son_base2 = pygame.mixer.Sound("Sons/son_tetris1.wav")
son_base3 = pygame.mixer.Sound("Sons/Kid_koala.wav")
son_play = pygame.mixer.Sound("Sons/sms1.wav")
son_enter = pygame.mixer.Sound("Sons/sms2.wav")
son_retour = pygame.mixer.Sound("Sons/sms_retour.wav")
son_jeu = pygame.mixer.Sound("Sons/Meydn.wav")
son_fast = pygame.mixer.Sound("Sons/Creo.wav")

g, windows, sound = 0, 0, 1    #g: la musique jouer ; windows: fenêtre en cours
                               #d'ouverture; sound: gestion du son dans option



#---------------------------------------------

pygame.display.set_caption("My Game")
 
# Permet de fermer le jeu si l'utilisateur appuie sur la croix rouge en haut à  droite
done = False

# gÃ©rer le rafraichissement de la fenÃªtre
clock = pygame.time.Clock()
 
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # background image.
    screen.fill(BLACK)
    #temps après lancer de pygame (en ms)
    time1 = pygame.time.get_ticks()
    
    #   musique principale
    if windows == 0 or windows == 2:
        if time1>108000:
            g=2
        if g==0:
            son_base1.play(loops=0, maxtime=0, fade_ms=0)
            g = 1
        if g==1 and time1>8000:
            son_base2.play(loops=0, maxtime=0, fade_ms=0)
            g=2
        if g==2 and time1>10000:
            son_base3.play(loops=0, maxtime=0, fade_ms=0)
            g=10
        #   répétition en boucle
        for i in range(10):
            if time1>10000+(i*98000) and time1<10001+(i*98000):
                g=2


    if windows == 0 or windows == 2 or windows == "pause":
        if event.type == KEYDOWN and event.key == K_DOWN:
            nbr_touch += 1
            if nbr_touch < 4 :
                son_base2.play()
                son_base2.fadeout(100)
            if nbr_touch == 4:
                nbr_touch = 0
        if event.type == KEYDOWN and event.key == K_UP:
            nbr_touch -= 1
            if nbr_touch > -1 :
                son_base2.play()
                son_base2.fadeout(100)
            if nbr_touch == -1:
                nbr_touch = 3

    #       image de présentation
    if time1<8000:
        screen.blit(Presentation, (0,0))
        if event.type == KEYDOWN and event.key == K_KP_ENTER:
            time1=8001
            
    if windows == 0 and time1>8000:
        #   TETRIS clignotant
        screen.blit(liste[t], bt1)
        t+=1
        if t>=6:
            t=0

        #Boutons:

        if nbr_touch == 1:
            screen.blit(playlist[timer(time, time1)], bt2)
            if time+1500<time1:
                time=time1
        else:
            screen.blit(play, bt2)

        if nbr_touch == 2:
            screen.blit(optionlist[timer(time, time1)], bt3)
            if time+1500<time1:
                time=time1
        else:
            screen.blit(option, bt3)

        if nbr_touch == 3:
            screen.blit(quit_list[timer(time, time1)], bt4)
            if time+1500<time1:
                time=time1
        else:
            screen.blit(quitter, bt4)


        if event.type == KEYDOWN and event.key == K_KP_ENTER or event.type == KEYDOWN and event.key == K_RETURN:
            if nbr_touch == 1:
                windows = 1
                son_play.play()
            if nbr_touch == 2:
                windows = 2
                son_enter.play()
            if nbr_touch == 3:
                done = True

    if windows == 2:
        if event.type == KEYDOWN and event.key == K_BACKSPACE:
            windows = 0


    if windows == "pause":
        if nbr_touch == 3:
            screen.blit(quit_list[timer(time, time1)], bt2)
            if time+1500<time1:
                time=time1
        else:
            screen.blit(quitter, bt2)
        if event.type == KEYDOWN and event.key == K_KP_ENTER or event.type == KEYDOWN and event.key == K_RETURN:
            if nbr_touch == 3:
                windows = 0

    if windows == 1:
        son_base3.stop()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            windows = "pause"
        if g==10:
            son_jeu.play()
            g=2

                    # --- Déssine la canevas écran du jeu --- #

        #fond du canevas
        image = pygame.image.load("Images/fond_jeu_1.jpg")
        position = (0,0)
        screen.blit(image, position)

        #damier du tetris
        damier = pygame.image.load("Images/Damier_tetris.png")
        screen.blit(damier, position)


        #score
        pygame.draw.rect(screen, BLACK, [460, 80, 300, 200])
        pygame.draw.rect(screen, BLACK, [460, 80, 300, 200], 5)
                #ajouter le code ---------------------------------------------------#
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # nbr de raffraichissement par seconde
    clock.tick(15)
 
# Ferme la fenêtre et quitte.
pygame.quit()