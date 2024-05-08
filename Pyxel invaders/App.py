from Monster import *
from Ball import *
from Player import *
from Bonus import *
from Score import *
from Boss_fight import *
import pyxel
import random
import time

current_time = int(time.time())
random.seed(current_time)

# -------------------------------------------------------------------
#                          INITIALISATION
# -------------------------------------------------------------------

class App:
    def __init__(self, dimx, dimy):
        # Initialisation des variables du jeu
        self.boss_event_cinematic= False
        self.boss_event_fight=False
        self.score = 0     # Score du joueur
        self.player = Player(80,220, self)  # Création de l'objet joueur
        self.balls = []    # Liste des balles
        self.monsters = [] # Liste des monstres
        self.bonus = []    # Liste des bonus
        self.game_speed = 1   # Vitesse du jeu
        self.barre_event = 260   # Barre d'événement
        self.boss_fight=Boss_fight(self)
        self.dimx = dimx   # Dimension du jeu
        self.dimy = dimy   # Dimension du jeu
        self.score_menu = None
        self.game_over = False
        self.game_paused = False 
        # Lancer l'événement du boss si la barre d'événement est vide

            
# -------------------------------------------------------------------
#                          MISE À JOUR
# -------------------------------------------------------------------

    def update(self):
        if not self.game_over:
            if self.score_menu is None:
                if not self.game_paused:
                    self.player.move_player()   # Déplacer le joueur
                    self.move_balls()           # Déplacer les balles
                    self.move_monster()         # Déplacer les monstres
                    self.move_bonus()           # Déplacer les bonus
                    self.cinematic()
                    self.start_boss_fight()
                    self.switch_to_boss_fight()
                        
                    self.player.chargement_barre() # Chargement de la barre du joueur
                    self.score += 1   # Incrémenter le score

        if pyxel.btnp(pyxel.KEY_Q):
            self.game_paused = True
        if pyxel.btnr(pyxel.KEY_Q):
            self.game_paused = False
        # Ajouter une balle si la barre est chargée
            

# -------------------------------------------------------------------
#                          DESSIN
# -------------------------------------------------------------------

    def draw(self):
        # Dessiner les éléments du jeu
        if self.score_menu is None:
            pyxel.cls(0)   # Effacer l'écran
            self.player.draw()    # Dessiner le joueur
            for monster in self.monsters:
                    monster.draw()    # Dessiner les monstres
            for ball in self.balls:
                if self.player.type_ball == 1:
                    ball.draw(48)
                elif self.player.type_ball == 2:
                    ball.draw(56) # Dessiner les balles
            for bonus in self.bonus:
                if self.player.type_ball != 2:
                    bonus.draw()      # Dessiner les bonus
            if self.barre_event <= 0:
                self.boss_fight.draw()

            pyxel.rect(138, 0, 2, self.barre_event, 2)   # Dessiner la barre d'événement
        else:
            self.score_menu.draw()
# -------------------------------------------------------------------
#                    AJOUT OU RETRAIT D'ÉLÉMENTS
# -------------------------------------------------------------------

    def ajouter_monster(self):
        # Ajouter des monstres au jeu
        self.monsters.append(Monster(random.randint(10, 120), random.randint(-70, -10), (random.randint(10,30) / 20), self))
        self.monsters.append(Monster(random.randint(10, 120), random.randint(-50, -10), (random.randint(10,30) / 20), self))
        self.monsters.append(Monster(random.randint(10, 120), random.randint(-50, -10), (random.randint(10,30) / 20), self))
        

    def ajouter_bonus(self):
        # Ajouter des bonus au jeu
        self.bonus.append(Bonus(random.randint(10, 120), random.randint(-50, -10),self.player))

    def ajouter_ball(self, x, y, dirx, diry):
        # Ajouter une balle au jeu
        self.balls.append(Ball(x, y, dirx, diry,self))

    def ball_update(self):
        if self.player.barre_chargement == 0 and self.player.type_ball == 1:  
            self.ajouter_ball(self.player.x, self.player.y, 0, -1)  
        if self.player.barre_chargement == 0 and self.player.type_ball == 2:
            self.ajouter_ball(self.player.x, self.player.y, random.randint(-1,1), -1)
            
    def spawn(self):
        if (pyxel.frame_count % 50 == 0 ):  
            self.ajouter_monster()    
        if (pyxel.frame_count % 75 == 0 ):
            self.ajouter_bonus()

    def spawn_monsters(self):
        if (pyxel.frame_count % 75 == 0 ):  
            self.ajouter_monster()    

    def supprimer_monster(self, monster):
        # Supprimer un monstre du jeu
        self.monsters.remove(monster)


# -------------------------------------------------------------------
#                          DÉPLACEMENT
# -------------------------------------------------------------------

    def move_monster(self):
        # Déplacer les monstres
        for monster in self.monsters:
            monster.move_monster()
            monster.check_collisions_monster_wall()

    def move_balls(self):
        # Déplacer les balles
        for ball in self.balls:
            ball.move_ball()
        if self.player.type_ball == 2:
            for ball in self.balls: 
                ball.check_collisions_ball_wall()

    def move_bonus(self):
        # Déplacer les bonus
        for bonus in self.bonus:
            bonus.move_bonus()
            bonus.check_collision_bonus_player()

# -------------------------------------------------------------------
#                        VÉRIFICATION DES COLLISIONS
# -------------------------------------------------------------------

    def check_collisions_ball_monster(self):
        # Vérifier les collisions entre les balles et les monstres
        for monster in self.monsters:
            for ball in self.balls:
                if( ball.x < monster.x + monster.w and ball.x + ball.w > monster.x and
                    ball.y < monster.y + monster.h and ball.y + ball.h > monster.y
                  ):
                     self.monsters.remove(monster)
                     self.balls.remove(ball)

    def check_collisions_player_monster(self):
        # Vérifier les collisions entre le joueur et les monstres
        for monster in self.monsters:
                if( self.player.x < monster.x + monster.w and self.player.x + self.player.w > monster.x and
                    self.player.y < monster.y + monster.h and self.player.y + self.player.h > monster.y
                  ): 
                        self.score_menu = ScoreMenu(self.score, self.dimx, self.dimy)
                        self.game_over = True
                        self.game_paused = True 
                        self.balls = []  

    def check_collision_bonus_player(self):
        # Vérifier la collision entre le joueur et le bonus
        for bonus in self.bonus:
            if( self.player.x < bonus.x + bonus.w and self.player.x + self.player.w > bonus.x and
                self.player.y < bonus.y + bonus.h and self.player.y + self.player.h > bonus.y
            ):
                self.bonus.remove(bonus)   # Supprimer le bonus
                self.player.type_ball=2    # Définir le type de balle du joueur

# -------------------------------------------------------------------
#                    MISE À JOUR DES PARAMÈTRES
# -------------------------------------------------------------------

    def chargement_barre_event(self):
        # Mettre à jour la barre de chargement de l'événement
        self.barre_event -= self.game_speed 

    def cinematic(self):
        if not self.boss_event_cinematic:
            self.check_collisions_ball_monster()       # Vérifier les collisions balle-monstre
            self.check_collisions_player_monster()
            self.ball_update()
            self.spawn()

    def start_boss_fight(self):
        if self.boss_event_fight:
            self.boss_fight.update()
            self.check_collisions_ball_monster()       # Vérifier les collisions balle-monstre
            self.check_collisions_player_monster()
            self.ball_update()
            self.spawn_monsters()
            if (pyxel.frame_count % 75 == 0 ):
                self.monsters.append(Monster((random.randint(100, 1200)/10), random.randint(-50, -10), (random.randint(10,30) / 15), self))

    def switch_to_boss_fight(self):
                # Vérifier les collisions joueur-monstre
        if self.barre_event >= 0:
            self.chargement_barre_event()  # Chargement de l'
        else:
            self.boss_fight.move_boss()
            self.boss_event_cinematic=True