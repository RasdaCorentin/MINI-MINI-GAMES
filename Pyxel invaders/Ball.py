import pyxel 

#Classe pour le Joueur (Barre) même régles que la brique
class Ball:

    def __init__(self, x, y, directionx, directiony, app):
        self.app = app
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8
        self.speed = 1.5
        self.damage = 5
        #Donne la vitesse de la direction de la balle (x = longueur; y = hauteur)
        self.dx =  directionx * self.speed
        self.dy =  directiony * self.speed

    def draw(self, pos_ball):
        pyxel.blt(self.x, self.y, 0, 0, pos_ball, self.w, self.h, 0)

    def move_ball(self):
        self.x += self.dx 
        self.y += self.dy

    def check_collisions_ball_wall(self):
        if self.x + self.w > self.app.dimx or self.x < 0:
            self.dx *= -1
        if self.y + self.h > self.app.dimy or self.y < 0:
            self.dy *= -1

