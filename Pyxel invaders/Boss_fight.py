from Boss import *
from Ball import *
from Player import *
from Monster import *
import random
import time

current_time = int(time.time())
random.seed(current_time)

# Set the seed based on the current time
random.seed(current_time)
#Frame count 
class Boss_fight:
    def __init__(self, app):
        self.app = app
        self.boss= { "X_gauche" : Boss_tiny_left_side( 20, -25 ), 
                     "Gauche" :   Boss_left_side( 27, -13 ), 
                     "Centre" :   Boss_center( 47, -25 ),
                     "Droite" :   Boss_right_side( 103, -13 ),
                     "X_droite" : Boss_tiny_right_side( 123, -25 )
                   }
        self.boss_center= self.boss["Centre"]
        self.boss_stop= [25,13,20,13,25]

    def update(self):
        if self.app.player.barre_chargement == 0 and self.app.player.type_ball == 2:
            self.app.ajouter_ball(self.app.player.x, self.app.player.y, random.randint(-1,1), -1)
        self.check_collisions_ball_boss()
        
    def draw(self):
        for boss_part in self.boss.values():
            if boss_part != 0 :
                boss_part.draw()
            
    def check_collisions_ball_boss(self):
        for ball in self.app.balls:
            for part_name, boss_part in list(self.boss.items()):  # Utilisation de list() pour éviter RuntimeError: dictionary changed size during iteration
                if (
                    ball.x < boss_part.x + boss_part.w + 5
                    and ball.x + ball.w > boss_part.x
                    and ball.y < boss_part.y + boss_part.h 
                    and ball.y + ball.h > boss_part.y
                ):
                    if not isinstance(boss_part, Boss_center):  # Vérifie si la partie du boss est le "Centre"
                        if boss_part.life <= 0:
                            self.boss.pop(part_name)  # Supprime la partie du boss si elle n'a plus de vie
                        else:
                            boss_part.life -= 34  # Réduit la vie de la partie centrale du boss

                    if isinstance(boss_part, Boss_center):
                        if len(list(self.boss.items())) == 1:
                            self.boss.pop(part_name)
            
                    self.app.balls.remove(ball)
                        
    def move_boss(self):
        for i, boss_part in enumerate(self.boss.values()):
            boss_part.move(self.boss_stop[i])
        if self.boss_center.y >= self.boss_stop[2]:
            self.app.boss_event_fight = True
