import pygame
import CONST

'''
    Ce module contient les définitions des calsses tablo et newBloc qui permettent de jouer.
'''


def give_position(forme, formestr, tablo):  # forme vient de CONST et tablo est le tablo utilisé
    '''
        La fonction qui initialise la position du bloc dans le tablo 
        N'est appelé qu'a la création du newBloc

        :param forme: la position initiale du bloc 
        :param formestr: la forme du bloc (ref commentcamarche)
        :param tablo: le tablo jeu utilisé
        :type forme: list
        :type formestr: str
        :type tablo: tablo
    '''
    for (x,y) in forme:
        if tablo.tablo[y][x] == 0:
            tablo.tablo[y][x] = formestr # la forme donne la couleur grace au dictionnaire dans CONST
        else:
            tablo.gameOver = True


def give_couleur(forme):
    '''
        Cetete fonction donne un code différents en fonction de la forme du bloc 
        Un code couleur différent est utilisé pour les bloc tombé et pour le bloc en mouvement (ref commentcamarche)
        Est utilisée quand le bloc a finit de tomber

        :param forme: la forme du bloc qui est arrivé
        :type forme: str
        :return: la couleur du bloc
        :rtype: str
    '''
    if forme=='carre':
        return('Jaune')
    elif forme=='laBarre':
        return('Bleu')
    elif forme=='leThe':
        return('Violet') 
    elif forme=='eclaireD':
        return('Vert')
    elif forme=='eclaireG':
        return('Orange')
    elif forme=='elleD':
        return('Rouge')
    elif forme=='elleG':
        return('Rose')


def test_rotation_coromp(les_positions):
    '''
        Test de rotation corompue
        Si un des carrés compposant le bloc est en dehors du tablo alors la rotaion est marquée comme corompue (ref rotation)

        .. warning:: Cette fonction a été développée en urgence car certain carrés avait des position négatives
                        dans le tablo pour une raison inconue
    '''
    for (x,y) in les_positions:
        if 0>x or x>9 or y<0 or y>19:
            return(True)     




class tablo:
    '''
        Cette classe est le tableau du jeu. C'est à dire le moyen de gérer les bloc de manière logique.

        Cette classe tablo contient le tableau (oui) ainsi que plusieurs variables nessessaires au fonctionnement du jeu.
    '''

    def __init__(self):
        '''
            Initialisation de l'objet.

            Création d'une liste de liste (simulation d'un tableau de 10 par 20) (voir exemple)
            Quelques autres varaiables qui servent à indiquer l'état du jeu:
                score est le score du joueur (oui oui c'est vrai)
                isvide indique si il y a un bloc en mouvement dans le tableau (False dans ce cas)
                gameOver indique quand le joueur a perdu
        '''
        self.tablo = [[0,0,0,0,0,0,0,0,0,0] for i in range(20)] # Indique presence des blocs
        self.score = 0
        self.lignes = 0
        self.isvide = True
        self.gameOver = False
        
    
    # Actualise le tablo, les scores/combos
    def test(self):
        '''
            Cette fonction teste si il y a des lignes horizontales complètes,
            Dans ce cas la fonction supprime ces lignes et augmente le score du joueur.
            Le combo sert a détécter un "Tetris" (4 lignes d'un coup) ce qui augmente le score.
        '''
        combo = 0
        for i in range(20): 
            if not 0 in self.tablo[i]:
                for j in range(i,20):
                    if self.tablo[j]!=[0,0,0,0,0,0,0,0,0,0]:
                        tempLigne = self.tablo[j+1].copy()
                        self.tablo[j] = tempLigne.copy()
                    else:
                        break
                combo += 1
                i -= 1

                self.lignes += combo
                if combo >= 4:  # le gain de score est totalement arbitraire meme si basé sur le Tetris original
                    self.score += 800 + combo*100
                else:
                    self.score += combo*100
    

    def update(self, estArrive=False, formestr="",positionsAvant=[], positionsApres=[]): # update position du bloc + test si le bloc a fini de tomber      
        '''
            Cette fonction permet de changer la position du bloc dans le tablo 
            Elle demande une position avant le déplacement qui sera supprimée ainsi
            qu'une position après le déplacment (ou rotation) qui sera écrite dans le tablo au bon endroit.

            :param estArrive: par défaut = False. Indique si le bloque à fini de tomber
            :param formestr: par défaut = "". La forme du bloc qui sera écrite dans le tablo.
            :param positionAvant: par défaut = []. La position que le bloc occupait avant le déplacement.
            :param positionApres: par défaut = []. La position que le bloc occupe après le déplacement.
        '''
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
            self.test()




class newBlock:
    '''
        Le bloc qui et en train de tomber et que l'on dirige

        Dans cette classe on peut trouver toute les valeures temporaire du bloc 
        ainsi que les fonctions qui permettent de le déplacer et de le faire tourner
    '''

    def __init__(self, laForme, positions_init, tablo):
        '''
            Initialisation du nouveau bloc

            Donne au nouveau bloc ses valeurs initiales:
            son orientation initiale, sa forme, initialisation de sa position initiale dans le tablo (ref give_position),
            ses position en fontion de son orientaiton, ses 'rotations corompues' (ref un paragrafe)
             

            :param laForme: str, c'est la forme du bloc qu'on appel et sert a initialiser la position et a la rotation. Sert aussi à donner la couleur (ref)
            :param forme:  dict, les positions du bloc pour chaque rotation sert pour initialiser la position et pour reperer le bloc lors de deplacement et de rotation
            :param tablo: un objet de la classe tablo (au dessus) dont on utilise le tablo pour tester les positions.
            :type laForme: str
            :type forme: dict
            :type tablo: tablo
        '''
        self.orient = 'DOWN'
        self.forme = laForme
        give_position(positions_init[self.orient], self.forme, tablo)
        self.positions = positions_init
        self.rotationCorompue = []

        
    def deplacement(self,direction,tablo):
        '''
            La fonction déplacement est appelée lorsqu'on le demande (les flêches) ou autaumatiquement pour BAS (ref gravité) (ref explication détaillée)

            Cette fonction est appelée quelle que soit la direction voulue:
                si la direction voulue est GAUCHE ou DROITE la fonction teste si le bloc est restera dans le tablo principal (ref explication détaillée)
                si la direction voulue est BAS la fonction fait la même chose mais si le bloc à atteint le bas la fontion renvoi l'information (ref tablo.update)


            :param direction: la direction voulue lorsqu'on appelle la fonction
            :param tablo: le tablo dans lequel se trouve le jeu (ref tablo)
            :type direction: str
            :type tablo: tablo   
        '''

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
                elif not (x-1,y) in self.positions[self.orient]:
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


    def rotation(self, tablo):
        '''
            La fonction rotation est appelée lorqu'on appuie sur la fleche du haut et teste si la rotation du bloc vers la gauche est possible.
            (ref rotation détail)

            D'abord la fonction trouve les rotations possible en fonction de la forme. (la liste t)
            Esuite, une fois que la prochaine rotation "disponible" est trouvée, la fonction teste s'il n'y a aucun obstacle ou si le bloc ne sort pas du jeu.
            Si tout est vérifié l'orientation du bloc est changée et les positions sont actualisées dans le tablo

            :param tablo: le tablo utilisé = le jeu
            :type tablo: tablo
        '''
        # test de possibilité de rotation + update positions
        if self.forme == 'carre':
            return       # si c'est un carre pas besoin de tourner
        elif self.forme=='elleG' or self.forme=='elleD' or self.forme=='leThe':
            t = ['DOWN','RIGHT','UP','LEFT']
        else:
            t = ['DOWN', 'UP']
        for i in range(len(t)): # Ca a merdé une fois à revoir
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

        


