import pyxel
import random

class Bonus:
    def __init__(self, x, y, player):
        self.player = player
        self.x = x
        self.y = y
        self.w =7
        self.h =7
        self.speed = 0.5
        #Donne la vitesse de la direction de la balle (x = longueur; y = hauteur)
        self.dx = self.speed
        self.dy =  self.speed

    def move_bonus(self):
        self.y += self.dy

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 32, 0, self.w, self.h, 0)

    
    def check_collision_bonus_player(self):
                if( self.x < self.player.x + self.player.w and self.x + self.w > self.player.x and
                    self.y < self.player.y + self.player.h and self.y + self.h > self.player.y
                  ):
                      self.player.type_ball=2