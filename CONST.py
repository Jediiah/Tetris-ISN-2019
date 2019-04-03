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
           'UP':[(7,18),(7,19),(7,20),(7,21)] } # Bleu

leThe = {'DOWN':[(5,19),(6,19),(7,19),(6,18)],   # Violet
          'UP':[(5,19),(6,19),(7,19),(6,18)],
          'LEFT' : [(5,19),(6,19),(7,19),(6,18)]
} # il manque les position droite et gauche

eclaireD = { 'DOWN':[(6,19),(7,19),(5,18),(6,18)],
            'UP':[(6,19),(5,19),(5,20),(6,18)] }# Vert

eclaireG = {'DOWN':[(5,19),(6,19),(6,18),(7,18)],
            'UP':[(7,19),(6,19),(6,18),(7,20)]} # Orange

elleD = {'UP':[(5,19),(5,18),(6,18),(7,18)],
         'DOWN':[(5,19),(7,19),(6,19),(7,18)],
         'LEFT':[(7,18),(7,19),(7,20),(6,18)],
         'RIGHT':[(6,17),(6,18),(6,19),(7,19)]}  # Rouge

elleG = {'UP':[(7,19),(5,18),(6,18),(7,18)], 
         'DOWN':[(7,19),(5,18),(6,19),(5,19)],
         'LEFT':[(6,19),(7,17),(7,18),(7,19)],
         'RIGHT':[(7,17),(6,17),(6,18),(6,19)]}  # Rose


# les images de blocs

lesImages = {
    'carre' : pygame.image.load("Images/jaune.png"),
    'laBarre' : pygame.image.load("Images/bleu.png"),
    'leThe' : pygame.image.load("Images/violet.png"),
    'eclaireD' : pygame.image.load("Images/vert.png"),
    'eclaireG' : pygame.image.load("Images/orange.png"),
    'elleG' : pygame.image.load("Images/rose.png"),
    'elleD' : pygame.image.load("Images/rouge.png"),
}