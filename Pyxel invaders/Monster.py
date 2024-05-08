import pyxel 

class Monster:
    def __init__(self, x, y, speed, app):
        self.app= app
        self.x = x
        self.y = y
        self.w = 16
        self.h = 15
        self.speed = speed
        #Donne la vitesse de la direction du monstre (x = longueur; y = hauteur)
        self.dx = self.speed 
        self.dy = self.speed 

    def move_monster(self):
        self.x+= self.dx 
        self.y+= self.dy
        
    def check_collisions_monster_wall(self):
        if self.x + self.w > self.app.dimx or self.x < 0:
            self.dx *= -1

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 16, 0, self.w, self.h, 0)
