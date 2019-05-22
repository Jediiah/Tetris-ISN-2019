import pygame, pygame.mixer, os.path
import pygame.locals
import pygame.freetype
from random import randint
from copy import deepcopy
import CLASSES, CONST

# Initialise pygame
pygame.init()


# création du bloc
def SelecBloc(bloc):
    global tabloJeu
    if bloc=='carre':
	    blocTombe = CLASSES.newBlock('carre', deepcopy(CONST.carre), tabloJeu)
    elif bloc=='laBarre':
	    blocTombe = CLASSES.newBlock('laBarre', deepcopy(CONST.laBarre), tabloJeu)
    elif bloc=='leThe':
	    blocTombe = CLASSES.newBlock('leThe', deepcopy(CONST.leThe), tabloJeu)
    elif bloc=='eclaireD':
	    blocTombe = CLASSES.newBlock('eclaireD', deepcopy(CONST.eclaireD), tabloJeu)
    elif bloc=='eclaireG':
	    blocTombe = CLASSES.newBlock('eclaireG', deepcopy(CONST.eclaireG), tabloJeu)
    elif bloc=='elleD':
	    blocTombe = CLASSES.newBlock('elleD', deepcopy(CONST.elleD), tabloJeu)
    elif bloc=='elleG':
	    blocTombe = CLASSES.newBlock('elleG', deepcopy(CONST.elleG), tabloJeu)
    return(blocTombe)


#'''================================================================================================='''
#'''========================    Cette partie est un menu    ========================================='''
#'''================================================================================================='''

# temps:
time = pygame.time.get_ticks()
def timer(time, time1):   # Nidhal, faut expliquer un peu
    if time1<time+1000:
        z=1
    else:
        z=2
    return(z)

# Mesures et initialisation de la fenetre
size = [800, 750]
screen = pygame.display.set_mode(size)

#images boutons:
	# coordonnées:
bt1 = x_bt1, y_bt1= (200, 100)	# Titre: Tetris

bt2 = x_bt2, y_bt2= (350,350)	# Play

bt3 = x_bt3, y_bt3= (350, 450)	# Option

bt4 = x_bt4, y_bt4= (345, 550)  # Quitter


#images associées:  ****************************************
Presentation = pygame.image.load("Images/FIRST.png")
GameOver = pygame.image.load("Images/gameoverteris.jpg")

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

		# bouton Option:
option = pygame.image.load("Images/Option_0.png")
option_s1 = pygame.image.load("Images/Option_1.png")
option_s2 = pygame.image.load("Images/Option_2.png")

optionlist = [option, option_s1, option_s2]

        # bouton Quitter
quitter = pygame.image.load("Images/quitter.png")
quitter_s1 = pygame.image.load("Images/quitter_1.png")
quitter_s2 = pygame.image.load("Images/quitter_2.png")
quit_list = [quitter, quitter_s1, quitter_s2]

        # retour
back = pygame.image.load("Images/Back.png")
# **************************************************



# ------------  Son  --------------------------
son_base1 = pygame.mixer.Sound("Sons/g.wav")
son_base2 = pygame.mixer.Sound("Sons/son_tetris1.wav")
son_base3 = pygame.mixer.Sound("Sons/Kid_koala.wav")
son_play = pygame.mixer.Sound("Sons/sms1.wav")
son_enter = pygame.mixer.Sound("Sons/sms2.wav")
son_retour = pygame.mixer.Sound("Sons/sms_retour.wav")

g = 0        # g: la musique jouee ;
windows = 1  # windows: fenetre en cours d'ouverture;
sound = 1    # sound: gestion du son dans option 
#---------------------------------------------


nbr_touch = 0  # numero du bouton sélectionné
pygame.display.set_caption("My Game") # titre de la fenetre
 
done = False 

# parametres de rafraichissement de la fenetre
clock = pygame.time.Clock()

 
#'''================================================================================================='''
#'''============================  Boucle Principale  ================================================'''
#'''================================================================================================='''

while not done:
    # --- explique dans le truc (ref)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(CONST.NOIR) # fond de la fenetre en noir
    time1 = pygame.time.get_ticks() # temps après lancer de pygame (en ms)
    
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

# je sais plus Nidhal refait stp
#    if g==10 and time1>108000:     Pour répéter en boucle le son
#        time1=8000
#        g=1
    

    #image de présentation
    #if time1<8000:
        #screen.blit(Presentation, (0,0))
        
    # Menu principal
    elif windows==0 and time1>0:
        # TETRIS clignotant
        screen.blit(liste[t], bt1)
        t+=1
        if t>=6:
            t=0

        # Gestion des Boutons: -----------------------------------
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


        if event.type == KEYDOWN and (event.key == K_KP_ENTER or event.key == K_RETURN):
            if nbr_touch == 1:
                windows = 1
                son_play.play()
            if nbr_touch == 2:
                windows = 2
                son_enter.play()
            if nbr_touch == 3:
                done = True

    elif windows == 2:
        if event.type == KEYDOWN and event.key == K_BACKSPACE:
            windows = 0

# a detailler au dessus Nidhal ----------------------------------   

#'''================================================================================================='''
#'''========================    Fin du Menu    ======================================================'''
#'''================================================================================================='''         



#'''================================================================================================='''
#'''===============================  TETRIS !!!!!!  ================================================='''
#'''================================================================================================='''

    elif windows==1:

        def plus_espaces(t):
            str_t = [[] for i in range(20)]
            for i in range(len(t)):
                for item in t[i]:
                    temp = str(item)
                    cote = 'd'
                    while len(temp) < 8:
                        if cote == 'd':
                            temp = ' ' + temp
                            cote = 'g'
                        elif cote == 'g':
                            temp = temp + ' '
                            cote = 'd'
                    str_t[-i].append(temp)
            return(str_t)



       #son_base3.stop()
        # -- Déssine l'écran du jeu -- #
        #fond 
        imageFond = pygame.image.load("Images/fond_jeu.jpg")
        screen.fill(CONST.BLANC)
        
        # delimitation de la zone de jeu (le cadrillage)
        platoJeu = screen.subsurface(50,25,345,609)
        imageJeu = pygame.image.load("Images/Damier_20.png")
        platoJeu.blit(imageJeu, (0,0))

        # création d'une surface d'affichage des scores
        afficheScore = screen.subsurface(350,250,355,270)

        # création de l'affichage de prévisualisation de la pièce
        visuPiece = screen.subsurface(350,50,355,150)
        fondVisu = pygame.image.load("Images/fondVisu.png")
        visuPiece.blit(fondVisu, (0,0))

        # Création du tableau de jeu
        tabloJeu = CLASSES.tablo() 
        tempScore = 1

        pygame.font.init()
        policeScore = pygame.font.Font(None, 56) # la police utilisée pour afficher le score   

        graviteForce = 500
        gravite = pygame.USEREVENT + 1 # création d'un nouvel événement
        pygame.time.set_timer(gravite, graviteForce) # Cet événement est produit toutes les 500ms (descente automatique)

        # pour séléctionner aléatoirement la prochaine pièce
        listeBlocs = ['carre','laBarre','leThe','eclaireD','eclaireG','elleG','elleD']
        prochainBloc = listeBlocs[randint(0,6)] 

        # signe pause
        pause_img = pygame.image.load("Images/pause.png")

       #  Boucle principale du jeu   
        while windows==1 and tabloJeu.gameOver==False:

            # s'il n y a pas de piece en mouvement dans le jeu
            if tabloJeu.isvide:
                blocTombe = SelecBloc(prochainBloc) # création de la piece
                tabloJeu.isvide = False
                prochainBloc = listeBlocs[randint(0,6)] # séléction de la prochaine pièce

                # affichage de la prochaine pièce
                visuPiece.blit(fondVisu, (0,0))
                visuPiece.blit(CONST.ImagesPrevisualisation[prochainBloc], (20,40))


            # permet de détecter les inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                    done = True
                    windows = 0

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pause = True
                    platoJeu.blit(pause_img, (200, 100))
                    while pause:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                                pause = False
                        
                        pygame.display.flip() # ajoute les elements crees sur la fenetre de jeu
                        clock.tick(5) # limite la vitesse de boucle


                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    blocTombe.deplacement('DROITE', tabloJeu)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    blocTombe.deplacement('GAUCHE',tabloJeu)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    blocTombe.deplacement('BAS',tabloJeu)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    blocTombe.rotation(tabloJeu)
                if event.type == gravite:
                    blocTombe.deplacement('BAS',tabloJeu)

            # si le score du joueur change on actualise l'affichage de celui-ci
            if tabloJeu.score!=tempScore:
                textScore = policeScore.render('Score : ' + str(tabloJeu.score), False, (0,0,0))
                textLignes = policeScore.render('Lignes : ' + str(tabloJeu.score), False, (0,0,0))
                screen.fill(CONST.BLANC)
                afficheScore.blit(textScore, (5,40))
                afficheScore.blit(textLignes, (5,70))
                tempScore = tabloJeu.score

            # je compte dans une grille de 10x20 avec des cases de 30x30px (subspace de 300x600)
            platoJeu.blit(imageJeu, (0,0))
            for i in range(20):
                for j in range(10):
                    if tabloJeu.tablo[i][j] != 0:
                        platoJeu.blit(CONST.lesImages[tabloJeu.tablo[i][j]], (3+(j*29), 609-(((i+2)*29)-3)))
                        
            
            pygame.display.flip() # ajoute les elements crees sur la fenetre de jeu
            clock.tick(15) # limite la vitesse de boucle


        gameover = 1
        while gameover==1:
            screen.blit(GameOver, (220,336))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key==(pygame.K_BACKSPACE or pygame.K_ESCAPE):
                    gameover = 0 # retour au menu

            pygame.display.flip() # ajoute les elements crees sur la fenetre de jeu
            clock.tick(30) # limite la vitesse de boucle


#'''================================================================================================='''
#'''========================    Fin du TETRIS   ====================================================='''
#'''================================================================================================='''
    
    # ajoute les elements crees sur la fenetre principale (menu)
    pygame.display.flip()

    # nbr de raffraichissement par seconde
    clock.tick(15)
 
# Ferme la fenêtre et quitte.
pygame.quit()




