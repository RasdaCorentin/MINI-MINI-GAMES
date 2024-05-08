import pyxel 

#Classe pour le Joueur (Vaisseau)
class Player:
    def __init__(self, x, y, app):
        self.app = app
        self.x = x #ça c'est la position du joueur en largeur 
        self.y = y#ça c'est la position du joueur en hauteur
        self.w = 16
        self.h = 15
        self.speed = 1.4
        self.speed_bar = 1
        #type de la balle doit appartenir à la balle sinon toutes les balles change de type 
        self.type_ball = 1
        self.barre_chargement=0 #La barre commence à 0 donc il y a une barre plein

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 32, self.w, self.h, 0)
        pyxel.rect(self.x, self.y + 17 , self.w, 2, 7) # Celle là elle est ? 
        pyxel.rect(self.x, self.y + 17 , self.barre_chargement, 2, 2) # oui rouge ou violet mais ou lé daltonien
        

    def chargement_barre(self): 
        self.barre_chargement += self.speed_bar /2
        if self.barre_chargement > 16 :
            self.barre_chargement = 0

    def move_player(self):
        if pyxel.btn(pyxel.KEY_RIGHT) and self.x < self.app.dimx - 2 - self.w:
            self.x += self.speed

        if pyxel.btn(pyxel.KEY_LEFT) and self.x > 2:
            self.x -= self.speed