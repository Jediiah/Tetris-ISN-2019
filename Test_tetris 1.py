import pygame
 
# Le vrai test de TOUT !! ! !!!  LAVANTURE

# Initialise pygame
pygame.init()

# Définir quelque couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE =  (  0,   0, 255)
GREY = (128, 128, 128)
PURPLE = (98, 14, 104)

# Mesures de la fenêtre
size = [970, 751]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Permet de fermer le jeu si l'utilisateur appuie sur la croix rouge en haut à droite
done = False

# gérer le rafraichissement de la fenêtre
clock = pygame.time.Clock()
 
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    
    # background image.
    screen.fill(WHITE)


        # --- Déssine la canevas écran du jeu --- #

    #fond du canevas
    image = pygame.image.load("Images/fond_jeu.jpg")
    position = (0,0)
    screen.blit(image, position)

    #damier du tetris
    window = screen.subsurface((50, 5, 350, 700))
    window.fill(WHITE)
    y, x = 35, 35
    for i in range(20):
        pygame.draw.line(window, GREY, [0, y], [350,y], 1)
        y += 35
    for y in range(10):
        pygame.draw.line(window, GREY, [x, 0], [x,750], 1)
        x += 35
        
    # pygame.draw.rect(screen, BLACK, [50, 50, 300, 600], 5)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(15)
 
# Close the window and quit.
pygame.quit()
