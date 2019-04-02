import pygame
import CONST

class tablo:

    def __init__(self):
        self.tablo = [[0,0,0,0,0,0,0,0,0,0] for i in range(20)] # Indique presence des blocs
        self.score = 0
        self.isvide = True
        
    
    # Actualise le tablo, les scores/combos
    def test(self):
        combo = 0
        for i in range(len(self.tablo)): # remplacer len jailaflemmedecompter
            if not 0 in self.tablo[i]:
                for j in range(i,19):
                    self.tablo[j] = self.tablo[j+1] # ca marche paa 
                self.score += int(x)
                combo += 1
                i -= 1

        if combo >= 4:
            self.score = int(x)
        # a continuer pour les combos et les scores

    def update(self, estArrive=False, positionsAvant=[], positionsApres=[]): # update position du bloc + test si le bloc a fini de tomber      
        if not estArrive:
            for (x,y) in positionsAvant:
                self.tablo[y][x] = 0
            for (x,y) in positionsApres:
                self.tablo[y][x] = 1 # + la couleur
            self.isvide = False
        else:
            self.isvide = True




class newBlock:

    def __init__(self, forme, tablo):
        #donne une position de chaque bloc dans le tablo sous forme d'une liste de tuple = (x,y)
        # commence en (6,19)
        self.orient = 'DOWN'
        self.jsp = give_position(forme[self.orient], tablo)
        self.positions = forme
        
        


    def deplacement(self,direction,tablo):
        if direction == 'BAS':
            peutDescendre = True
            for (x,y) in self.positions[self.orient]:
                if y>0 and tablo[y-1][x]==0:
                    continue
                else:
                    peutDescendre = False
                    break
            if peutDescendre:
                posAvant = self.positions[self.orient].copy()
                for cle in self.positions.keys():
                    for i in range(4):
                        self.positions[cle][i] = (x,y) = (x,y-1)
                tablo.update(posAvant, self.positions[self.orient]) 
            else:
                tablo.update(estArrive=True)    # les argument à revoir
            
        elif direction == 'DROITE':
            for (x,y) in self.positions[self.orient]:
                if x<9 and tablo[y][x+1]==0:
                    continue
                else:
                    peutDroite = False
                    break
            if peutDroite:
                posAvant = self.positions[self.orient].copy()
                for cle in self.positions.keys():
                    for i in range(4):
                        self.positions[cle][i] = (x,y) = (x+1,y)
                tablo.update(posAvant, self.positions[self.orient])

        elif direction=='GAUCHE':
            for (x,y) in self.positions[self.orient]:
                if x>1 and tablo[y][x-1]==0:
                    continue
                else:
                    peutGauche = False
                    break
            if peutGauche:
                posAvant = self.positions[self.orient].copy()
                for cle in self.positions.keys():
                    for i in range(4):
                        self.positions[cle][i] = (x,y) = (x-1,y)
                tablo.update(posAvant, self.positions[self.orient])


    def rotation(self, forme, tablo):
        # test de possibilité de rotation + update positions
        if self.forme=='carre':
            pass       # si c'est un carre pas besoin de tourner (c'est pas pass faut changer)
        elif self.forme==('elleG' or 'elleD' or 'leThe'):
            t = ['DOWN','RIGHT','UP','RIGHT']
        else:
            t = ['DOWN', 'UP']
        orientation = t[t.index(self.orient)]
        for (x,y) in self.positions[t[orientation-1]]:
            peutTourner = True
            if 0<x<11 and y>0 and tablo.tablo[y][x]==0:
                continue
            else:
                peutTourner = False
                break
        if peutTourner:
            posAvant = self.positions[self.orient].copy()
            self.orient = orientation
            tablo.update(posAvant, self.positions[self.orient])


def give_position(forme, tablo):  # forme vient de CONST et tablo est le tablo utilisé
    for (x,y) in forme:
        tablo.tablo[y][x] = 1 # ajouter code couleur ...a definir
    return(forme)
    

    
        


