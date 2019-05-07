import pygame
import CONST


def give_position(forme, formestr, tablo):  # forme vient de CONST et tablo est le tablo utilisé
    for (x,y) in forme:
        tablo.tablo[y][x] = formestr # la forme donne la couleur grace au dictionnaire dans CONST
    return(forme)

def give_couleur(forme):
    if forme=='carre':
        return('Jaune')
    elif forme=='laBarre':
        return('Bleu')
    elif forme=='leThe':
        return('Bleu')  #Violet apres
    elif forme=='eclaireD':
        return('Vert')
    elif forme=='eclaireG':
        return('Orange')
    elif forme=='elleD':
        return('Rouge')
    elif forme=='elleG':
        return('Rose')

def test_rotation_coromp(les_positions):
        for (x,y) in les_positions:
            if 0>x or x>9 or y<0 or y>19:
                return(True)     




class tablo:

    def __init__(self):
        self.tablo = [[0,0,0,0,0,0,0,0,0,0] for i in range(20)] # Indique presence des blocs
        self.score = 0
        self.isvide = True
        
    
    # Actualise le tablo, les scores/combos
    def test(self):
        combo = 0
        for i in range(20): 
            if not 0 in self.tablo[i]:
                for j in range(i,20):
                    if self.tablo[j]!=[0,0,0,0,0,0,0,0,0,0]:
                        tempLigne = self.tablo[j+1].copy()
                        self.tablo[j] = tempLigne
                    else:
                        break
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
                self.tablo[yApres][xApres] = formestr 
            self.isvide = False
        else:
            for (x,y) in positionsAvant:
                self.tablo[y][x] = give_couleur(formestr)
            self.isvide = True




class newBlock:

    def __init__(self, laForme, forme, tablo):
        '''
            Le bloc qui bouge

            :param laForme str, c'est la forme du bloc qu'on appel et sert a initialiser la position et a la rotation. Sert aussi à donner la couleur (ref)
            :param forme  dict, les positions du bloc pour chaque rotation sert pour initialiser la position et pour reperer le bloc lors de deplacement et de rotation
            :param tablo un objet de la classe tablo (au dessus) dont on utilise le tablo pour tester les positions.
        '''
        #donne une position de chaque bloc dans le tablo sous forme d'une liste de tuple = (x,y)
        # commence en (6,19)
        self.orient = 'DOWN'
        self.forme = laForme
        self.jsp = give_position(forme[self.orient], self.forme, tablo)
        self.positions = forme
        self.rotationCorompue = []

        
    def deplacement(self,direction,tablo):

        if direction == 'BAS':
            peutDescendre = True
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
                    cleCorompue =  test_rotation_coromp(self.positions[cle])
                    if not cle in self.rotationCorompue:
                        if cleCorompue:
                            self.rotationCorompue.append(cle)
                    elif cle in self.rotationCorompue:
                        if not cleCorompue:
                            self.rotationCorompue.remove(cle)
                tablo.update(formestr=self.forme, positionsAvant=posAvant, positionsApres=self.positions[self.orient]) 
            else:
                tablo.update(estArrive=True, formestr=self.forme, positionsAvant=self.positions[self.orient])
            
        elif direction == 'DROITE':
            peutDroite = True
            for (x,y) in self.positions[self.orient]:
                if 0<=x<9 and ((x+1,y) in self.positions[self.orient] or tablo.tablo[y][x+1]==0):
                    continue
                elif not (x+1,y) in self.positions[self.orient]:
                    peutDroite = False
                    break
            if peutDroite:
                posAvant = self.positions[self.orient].copy()
                for cle in self.positions.keys():
                    for i in range(4):
                        (x,y) = self.positions[cle][i] 
                        self.positions[cle][i] = (x+1,y)
                    cleCorompue =  test_rotation_coromp(self.positions[cle])
                    if not cle in self.rotationCorompue:
                        if cleCorompue:
                            self.rotationCorompue.append(cle)
                    elif cle in self.rotationCorompue:
                        if not cleCorompue:
                            self.rotationCorompue.remove(cle)
                tablo.update(formestr=self.forme, positionsAvant=posAvant, positionsApres=self.positions[self.orient])

        elif direction=='GAUCHE':
            peutGauche = True
            for (x,y) in self.positions[self.orient]:
                if x>0 and ((x-1,y) in self.positions[self.orient] or tablo.tablo[y][x-1]==0):
                    continue
                elif not (x+1,y) in self.positions[self.orient]:
                    peutGauche = False
                    break
            if peutGauche:
                posAvant = self.positions[self.orient].copy()
                for cle in self.positions.keys():
                    for i in range(4):
                        (x,y) = self.positions[cle][i] 
                        self.positions[cle][i] = (x-1,y)
                    cleCorompue =  test_rotation_coromp(self.positions[cle])
                    if not cle in self.rotationCorompue:
                        if cleCorompue:
                            self.rotationCorompue.append(cle)
                    elif cle in self.rotationCorompue:
                        if not cleCorompue:
                            self.rotationCorompue.remove(cle)
                tablo.update(formestr=self.forme, positionsAvant=posAvant, positionsApres=self.positions[self.orient])


    def rotation(self, forme, tablo):
        # test de possibilité de rotation + update positions
        if self.forme == 'carre':
            return       # si c'est un carre pas besoin de tourner
        elif self.forme=='elleG' or self.forme=='elleD' or self.forme=='leThe':
            t = ['DOWN','RIGHT','UP','LEFT']
        else:
            t = ['DOWN', 'UP']
        for i in range(len(t)):
            orientation = t[t.index(self.orient)-(1+i)]
            if not orientation in self.rotationCorompue:
                break
        peutTourner = False
        if not orientation in self.rotationCorompue:
            peutTourner = True
            for (x,y) in self.positions[orientation]:
                if 0<x<10 and 20>y>0 and ((x,y) in self.positions[orientation] or tablo.tablo[y][x]==0):
                    continue
                else:
                    peutTourner = False
                    break
        if peutTourner:
            posAvant = self.positions[self.orient].copy()
            self.orient = orientation
            tablo.update(formestr=self.forme, positionsAvant=posAvant, positionsApres=self.positions[self.orient])

        


