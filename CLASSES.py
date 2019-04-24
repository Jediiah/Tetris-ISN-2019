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
                self.score += 10 # a changer
                combo += 1
                i -= 1

        if combo >= 4:
            self.score = 10  # a changer
        # a continuer pour les combos et les scores

    def update(self, estArrive=False, formestr="",positionsAvant=[], positionsApres=[]): # update position du bloc + test si le bloc a fini de tomber      
        if not estArrive:
            for (xAvant,yAvant) in positionsAvant:
                self.tablo[yAvant][xAvant] = 0
            for (xApres,yApres) in positionsApres:
                self.tablo[yApres][xApres] = formestr # + la couleur
            self.isvide = False
        else:
            self.isvide = True




class newBlock:

    def __init__(self, laForme, forme, tablo):
        #donne une position de chaque bloc dans le tablo sous forme d'une liste de tuple = (x,y)
        # commence en (6,19)
        self.orient = 'DOWN'
        self.forme = laForme
        self.jsp = give_position(forme[self.orient], self.forme, tablo)
        self.positions = forme
        
        
    def deplacement(self,direction,tablo):

        if direction == 'BAS':
            peutDescendre = True
            print("BAS")
            for (x,y) in self.positions[self.orient]:
                if y>0 and ((x,y-1) in self.positions[self.orient] or tablo.tablo[y-1][x]==0):
                    continue
                elif not (x,y-1) in self.positions[self.orient]:
                    peutDescendre = False
                    break
            if peutDescendre:
                posAvant = self.positions[self.orient].copy()
                for cle in self.positions.keys():
                    for i in range(4):
                        (x,y) = self.positions[cle][i] 
                        self.positions[cle][i] = (x,y-1)
                tablo.update(formestr=self.forme, positionsAvant=posAvant, positionsApres=self.positions[self.orient]) 
            else:
                tablo.update(estArrive=True)    # les argument à revoir
            
        elif direction == 'DROITE':
            peutDroite = True
            print("Droite")
            for (x,y) in self.positions[self.orient]:
                if x<9 and ((x+1,y) in self.positions[self.orient] or tablo.tablo[y][x+1]==0):
                    continue
                else:
                    peutDroite = False
                    break
            if peutDroite:
                posAvant = self.positions[self.orient].copy()
                for cle in self.positions.keys():
                    for i in range(4):
                        (x,y) = self.positions[cle][i] 
                        self.positions[cle][i] = (x+1,y)
                tablo.update(formestr=self.forme, positionsAvant=posAvant, positionsApres=self.positions[self.orient])

        elif direction=='GAUCHE':
            peutGauche = True
            print("Gauche")
            for (x,y) in self.positions[self.orient]:
                if x>1 and ((x-1,y) in self.positions[self.orient] or tablo.tablo[y][x-1]==0):
                    continue
                else:
                    peutGauche = False
                    break
            if peutGauche:
                posAvant = self.positions[self.orient].copy()
                for cle in self.positions.keys():
                    for i in range(4):
                        (x,y) = self.positions[cle][i] 
                        self.positions[cle][i] = (x-1,y)
                tablo.update(formestr=self.forme, positionsAvant=posAvant, positionsApres=self.positions[self.orient])


    def rotation(self, forme, tablo):
        print(self.orient, self.forme)
        # test de possibilité de rotation + update positions
        if self.forme == 'carre':
            return       # si c'est un carre pas besoin de tourner
        elif self.forme == ('elleG' or 'elleD' or 'leThe'):
            print(1)
            t = ['DOWN','RIGHT','UP','LEFT','DOWN']
        else:
            t = ['DOWN', 'UP']
        print(t)
        orientation = t[t.index(self.orient)-1]
        peutTourner = True
        for (x,y) in self.positions[orientation]:
            if 0<x<11 and y>0 and ((x,y) in self.positions[orientation] or tablo.tablo[y][x]==0):
                continue
            else:
                peutTourner = False
                break
        if peutTourner:
            posAvant = self.positions[self.orient].copy()
            self.orient = orientation
            tablo.update(formestr=self.forme, positionsAvant=posAvant, positionsApres=self.positions[self.orient])
        print(self.orient)

def give_position(forme, formestr, tablo):  # forme vient de CONST et tablo est le tablo utilisé
    for (x,y) in forme:
        tablo.tablo[y][x] = formestr # la forme donne la couleur grace au dictionnaire dans CONST
    return(forme)

    
        


