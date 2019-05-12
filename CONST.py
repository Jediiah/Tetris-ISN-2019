import pygame


NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
VERT = (0, 255, 0)
ROUGE = (255, 0, 0)
BLEU =  (  0,   0, 255)
GRIS = (128, 128, 128)
VIOLET = (98, 14, 104)
# Peut etre plus de couleurs ....


# Formes de Blocs : liste de coordonnees

carre = {'DOWN':[(6,19),(6,18),(7,19),(7,18)]}   # Jaune

laBarre = {'DOWN':[(5,19),(6,19),(7,19),(8,19)],
           'UP':[(7,17),(7,18),(7,19),(7,20)] } # Bleu

leThe = {'DOWN':[(5,19),(6,19),(7,19),(6,18)],   # Violet
          'UP':[(5,19),(6,19),(7,19),(6,20)],
          'LEFT':[(6,20),(6,19),(5,19),(6,18)],
          'RIGHT':[(6,20),(6,19),(7,19),(6,18)]} 

eclaireD = { 'DOWN':[(6,19),(7,19),(5,18),(6,18)],
            'UP':[(6,19),(7,19),(6,20),(7,18)]}# Vert

eclaireG = {'DOWN':[(5,19),(6,19),(6,18),(7,18)],
            'UP':[(7,19),(6,19),(6,18),(7,20)]} # Orange

elleD = {'UP':[(5,19),(6,19),(6,18),(6,17)],
         'DOWN':[(6,17),(6,18),(6,19),(7,17)],
         'LEFT':[(7,18),(6,18),(5,18),(5,17)],
         'RIGHT':[(5,18),(6,18),(7,18),(7,19)]}  # Rouge

elleG = {'UP':[(6,19),(6,18),(6,17),(7,19)], 
         'DOWN':[(6,19),(6,18),(6,17),(5,17)],
         'LEFT':[(5,18),(6,18),(7,18),(5,19)],
         'RIGHT':[(5,18),(6,18),(7,18),(7,17)]}  # Rose


# les images de blocs
lesImages = {
    'carre' : pygame.image.load("Images/BlocJaune.png"),
    'Jaune' : pygame.image.load("Images/BlocJaune.png"),
    'laBarre' : pygame.image.load("Images/BlocBleu.png"),
    'Bleu' : pygame.image.load("Images/BlocBleu.png"),
    'leThe' : pygame.image.load("Images/BlocViolet.png"),
    'Violet' : pygame.image.load("Images/BlocViolet.png"),
    'eclaireD' : pygame.image.load("Images/BlocVert.png"),
    'Vert' : pygame.image.load("Images/BlocVert.png"),
    'eclaireG' : pygame.image.load("Images/BlocOrange.png"),
    'Orange' : pygame.image.load("Images/BlocOrange.png"),
    'elleG' : pygame.image.load("Images/BlocRose.png"),
    'Rose' : pygame.image.load("Images/BlocRose.png"),
    'elleD' : pygame.image.load("Images/BlocRouge.png"),
    'Rouge' : pygame.image.load("Images/BlocRouge.png")
}

ImagesPrevisualisation = {
    'carre' : pygame.image.load("Images/carre.png"),
    'laBarre': pygame.image.load("Images/laBarre.png"),
    'leThe' : pygame.image.load("Images/leThe.png"),
    'eclaireD': pygame.image.load("Images/eclaireD.png"),
    'eclaireG': pygame.image.load("Images/eclaireG.png"),
    'elleG':  pygame.image.load("Images/elleG.png"),
    'elleD': pygame.image.load("Images/elleD.png")
}