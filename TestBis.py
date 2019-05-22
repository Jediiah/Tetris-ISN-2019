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


#images associées:  ****************************************
Presentation = pygame.image.load("Images/FIRST.png")
GameOver = pygame.image.load("Images/gameoverteris.jpg")

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
    

#'''================================================================================================='''
#'''========================    Fin du Menu    ======================================================'''
#'''================================================================================================='''         



#'''================================================================================================='''
#'''===============================  TETRIS !!!!!!  ================================================='''
#'''================================================================================================='''

    if windows==1:

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
        tempLignes = 0

        pygame.font.init()
        policeScore = pygame.font.Font(None, 56) # la police utilisée pour afficher le score   

        graviteForce = 500
        gravite = pygame.USEREVENT + 1 # création d'un nouvel événement
        gravitation = pygame.time.set_timer(gravite, graviteForce) # Cet événement est produit toutes les 300ms (descente automatique)


        # pour séléctionner aléatoirement la prochaine pièce
        listeBlocs = ['carre','laBarre','leThe','eclaireD','eclaireG','elleG','elleD']
        prochainBloc = listeBlocs[randint(0,6)] 
         # affichage de la prochaine pièce
        visuPiece.blit(fondVisu, (0,0))
        visuPiece.blit(CONST.ImagesPrevisualisation[prochainBloc], (20,40))


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

            # vitesse de tombée
            if tabloJeu.lignes%1==0 and tabloJeu.lignes!=tempLignes:
                graviteForce = int(graviteForce*0.5)
                gravitation = pygame.time.set_timer(gravite, graviteForce) # Cet événement est produit toutes les 300ms (descente automatique)
                tempLignes = tabloJeu.lignes
                

            # permet de détecter les inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    windows = 3
                if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                    done = True
                    windows = 0
                # "echap" met la pause, echap pour en sortir
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pause = True
                    platoJeu.blit(pause_img, (100, 200))
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
                textLignes = policeScore.render('Lignes : ' + str(tabloJeu.lignes), False, (0,0,0))
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
        while gameover==1 and windows!=3:
            screen.blit(GameOver, (220,336))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key==(pygame.K_BACKSPACE or pygame.K_ESCAPE):
                    gameover = 0 # retour au menu
                if event.type == pygame.QUIT:
                    done = True
                    windows = 3

            pygame.display.flip() # ajoute les elements crees sur la fenetre de jeu
            clock.tick(5) # limite la vitesse de boucle


#'''================================================================================================='''
#'''========================    Fin du TETRIS   ====================================================='''
#'''================================================================================================='''
    
    # ajoute les elements crees sur la fenetre principale (menu)
    pygame.display.flip()

    # nbr de raffraichissement par seconde
    clock.tick(15)
 
# Ferme la fenêtre et quitte.
pygame.quit()




