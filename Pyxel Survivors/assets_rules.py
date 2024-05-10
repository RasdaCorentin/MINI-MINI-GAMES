GAME = 3
IN_GAME_WIN = 1
IN_GAME_OVER = 2

COLLISION_THRESHOLD = 20  # Adjust as needed

import pyxel
import random
import math


#------------------------------------------------------WORLD-------------------------------------------------------

class World:
    def __init__(self,game, width=1000,height=1000):


        self.world_game_mode = GAME
        self.game = game
        self.map_position_x=-435
        self.map_position_y=-435
        
        self.width = width
        self.height = height

        self.bullet_list = []        
        
        self.character = Character(self)
        self.mob = Mob(self.character)

        self.in_game_minute = 1
        self.in_game_second = 0


    def character_mouvment(self):
        
        #direction ves la droite
            if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
                self.map_position_x -= self.character.character_speed
                self.character.direction_character_x = -1

            #direction vers la gauche
            if pyxel.btn(pyxel.KEY_Q) or pyxel.btn(pyxel.KEY_LEFT):
                self.map_position_x += self.character.character_speed
                self.character.direction_character_x = 1

            #direction vers le haut
            if pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN):
                self.map_position_y -= self.character.character_speed

            #direction vers le bas
            if pyxel.btn(pyxel.KEY_Z) or pyxel.btn(pyxel.KEY_UP):
                self.map_position_y += self.character.character_speed


    def map_border(self):
        if self.map_position_x > -10:
            self.map_position_x -= 768
        
        if self.map_position_x < -800:
            self.map_position_x += 768

        if self.map_position_y > -10:
            self.map_position_y -= 768

        if self.map_position_y < -800:
            self.map_position_y += 768


    def timer(self):
        if pyxel.frame_count % 60 == 0:
            self.in_game_second -= 1
            if self.in_game_second < 0 and self.in_game_minute != 0:
                self.in_game_second = 59
                self.in_game_minute -= 1
            elif self.in_game_second <= 0 and self.in_game_minute == 0:
                self.world_game_mode = IN_GAME_WIN
        
        second = str(self.in_game_second)
        minute = str(self.in_game_minute)
        
        return f"{minute:0>2}:{second:0>2}"
    
    def character_health(self):

        for mob in self.mob.mobs_liste:
            if 95 < mob[0] < 102 and 93 < mob[1] < 107:
                self.character.health -= 1
            
            if self.character.health <= 0:
                self.world_game_mode = IN_GAME_OVER


    # ===============================================================
    # ==                         UPDATE                            ==
    # ===============================================================
    def update(self):

        if self.world_game_mode == GAME:

            self.character_mouvment()
            self.map_border()
            self.mob.update()
            self.character_health()


    # ===============================================================
    # ==                         DRAW                              ==
    # ===============================================================
    def draw(self):

        if self.world_game_mode == GAME:

            # Dessiner le monde en fonction de l'offset
            pyxel.bltm(self.map_position_x, self.map_position_y, 0, 0, 0, self.width, self.height, 0)

            self.mob.draw()
            self.character.draw()

            timer_str = self.timer()
            pyxel.rect(87, 8, 25, 9, 0)
            pyxel.text(90, 10, timer_str, 7)

#------------------------------------------------------CHARACTER-------------------------------------------------------

class Character:
    def __init__(self,world_instance, x=0, y=0, speed=2):

        # definit la position initiale du character (origine des positions : coin haut gauche)

        self.world = world_instance
        
        self.health = 100

        self.position_character_x = 435
        self.position_character_y = 435


        self.direction_character_x = 1
        

        #definit la vitesse du character
        self.character_speed = speed


    def health_bar(self):
        pyxel.rectb(49, 184, 102, 5, 10)
        pyxel.rect(50, 185, 100, 3, 0)
        pyxel.rect(50, 185, self.health, 3, 8)
    


    def draw(self):

        # Dessiner le personnage
        center_x = pyxel.width // 2 - 8  # 8 est la moitié de la largeur du personnage
        center_y = pyxel.height // 2 - 8  # 8 est la moitié de la hauteur du personnage
        if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
            self.direction_character_x = -1
        elif pyxel.btn(pyxel.KEY_Q) or pyxel.btn(pyxel.KEY_LEFT):
            self.direction_character_x = 1

        pyxel.blt(center_x, center_y, 1, 0, 0, 16*self.direction_character_x, 16, 11)

        #dessine la barre de vie
        self.health_bar()

         
#------------------------------------------------------MOB-------------------------------------------------------

class Mob:
    def __init__(self, character, speed=1):

        #definit la vitesse des mobs
        self.mob_speed = speed
        self.direction_mob = 1
              
        #initialisation des mobs
        self.mobs_liste = []
        self.mobs_proche = []
        self.character = character
    



    def mobs_creation(self):
        """création aléatoire des mobs"""

        # un mob par seconde
        if (pyxel.frame_count % 10 == 0):
            bord = random.randint(0, 3)  # Sélection aléatoire d'un bord (0: haut, 1: droite, 2: bas, 3: gauche)
            if bord == 0:
        # Bord supérieur
                self.mobs_liste.append([random.randint(-8, 208), 0])
            elif bord == 1:
        # Bord droit
                self.mobs_liste.append([208, random.randint(-8, 208)])
            elif bord == 2:
        # Bord inférieur
                self.mobs_liste.append([random.randint(-8, 208), 200])
            else:
        # Bord gauche
                self.mobs_liste.append([0, random.randint(-8, 208)])




    def avoid_collision(self, mob1, mob2):
            dx = mob2[0] - mob1[0]
            dy = mob2[1] - mob1[1]
            if distance == 0:
                distance = 1
            dx /= distance
            dy /= distance
            dist_factor = COLLISION_THRESHOLD - distance
            mob1[0] -= dx * dist_factor
            mob1[1] -= dy * dist_factor
            mob2[0] += dx * dist_factor
            mob2[1] += dy * dist_factor

    def mobs_deplacement(self):
        """déplacement des mobs vers le haut et suppression s'ils sortent du cadre"""              
        #fait se déplacer les mobs en fonction des coo du joueur
        self.mobs_proche = None  # Réinitialiser l'mob le plus proche

        for i in range(len(self.mobs_liste)):
            for j in range(i + 1, len(self.mobs_liste)):
                self.avoid_collision(self.mobs_liste[i], self.mobs_liste[j])
        
        
        for mob in self.mobs_liste:

            #direction ves la droite
            if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
                mob[0] -= self.character.character_speed
                self.direction_mob = -1
            if mob[0] < 98:
                mob[0] += 0.5

            #direction vers la gauche
            if pyxel.btn(pyxel.KEY_Q) or pyxel.btn(pyxel.KEY_LEFT):
                mob[0] += self.character.character_speed
                self.direction_mob = 1
            if mob[0] > 98:
                mob[0] -= 0.5

            #direction vers le haut
            if pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN):
                mob[1] -= self.character.character_speed
            if mob[1] < 100:
                mob[1] += 0.5

            #direction vers le bas
            if pyxel.btn(pyxel.KEY_Z) or pyxel.btn(pyxel.KEY_UP):
                mob[1] += self.character.character_speed
            if mob[1] > 100:
                mob[1] -= 0.5

    def mob_colision(self):
        pass



    # ===============================================================
    # ==                         UPDATE                            ==
    # ===============================================================
    def update(self):
        """mise à jour des variables (30 fois par seconde)"""
        self.mobs_creation()
        self.mobs_deplacement()
        self.mob_colision()



    # ===============================================================
    # ==                         DRAW                              ==
    # ===============================================================
    def draw(self):
        for mob in self.mobs_liste:
            pyxel.blt(mob[0],mob[1], 1, 16, 0, 16*self.direction_mob, 16, 11)
