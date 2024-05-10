import pyxel
from assets_rules import World

# --- Les différents modes
# ---

WELCOME_SCREEN = 0
MAIN_MENU = 1
OPTION = 2
GAME = 3
GAME_PAUSE = 4
END_GAME = 5
WIN_SCREEN = 6
LOSE_SCREEN = 7

# --- Les directions de déplacement
# ---
NORD = 0, -1
EST = 1, 0
SUD = 0, 1 
OUEST = -1, 0

KEY_TO_DIR = {pyxel.KEY_UP: NORD, pyxel.KEY_RIGHT: EST, pyxel.KEY_DOWN: SUD, pyxel.KEY_LEFT: OUEST}
FLECHES = KEY_TO_DIR.keys()
DIRECTIONS = KEY_TO_DIR.values()

class Bouton:

    def __init__(self, rectangle, couleurs, texte, mode):
        
        self.rect = rectangle
        self.couleurs = couleurs
        self.actif = False
        self.texte = texte  # (x, y, contenu texte)
        self.mode = mode

    def on(self):
        self.actif = True

    def off(self):
        self.actif = False

    def validate(self, last_game_mode):
        if self.mode is not None:
            return self.mode
        else:
            return last_game_mode

    def draw(self):
        x, y, w, h = self.rect
        couleur = self.couleurs[int(self.actif)]
        #pyxel.rectb(x, y, w, h, couleur)
        pyxel.text(x+13, y+5, self.texte, couleur)
        pyxel.rectb(x+10,y+1, 55, 12 , couleur)




class Menu:
    """Gestion des différents mode du jeu avec les écrans associés"""

    def __init__(self, game_instance,boutons,background_color = 1):        
        self.game = game_instance
        self.boutons = boutons
        self.background_color = background_color
        self.selected = 0

        self.reset = False
        self.bouton_actif().on()

    def bouton_actif(self):
        return self.boutons[self.selected]
    

    def update(self):
        if pyxel.btnr(pyxel.KEY_UP):
            self.bouton_actif().off()
            self.selected = (self.selected - 1) % len(self.boutons)
            self.bouton_actif().on()
        elif pyxel.btnr(pyxel.KEY_DOWN):
            self.bouton_actif().off()
            self.selected = (self.selected + 1) % len(self.boutons)
            self.bouton_actif().on()
        elif pyxel.btnr(pyxel.KEY_RETURN) or pyxel.btnr(pyxel.KEY_SPACE):
            self.game.change_mode(self.bouton_actif().validate(self.game.last_game_mode))

    def draw(self):
        pyxel.cls(self.background_color)
        for bouton in self.boutons:
            bouton.draw()




#===========================================================GAME============================================================

class Game:

    def __init__(self,w=200,h=200):
        self.w = w
        self.h = h
        pyxel.init(width=w,height=h,fps=60, title="Projet python", display_scale=3)

        self.world = World(self)
        
        self.menus = {
            WELCOME_SCREEN:     Menu(self, [Bouton((65, 130, 100, 20), (7, 0), "PRESS ESPACE", MAIN_MENU)],1),
            
            MAIN_MENU:          Menu(self, [Bouton((15, 120, 150, 144), (7, 0), "PLAY", GAME),  
                                            Bouton((15, 140, 150, 164), (7, 0), "OPTION", OPTION), 
                                            Bouton((15, 160, 168, 182), (7, 0), "QUIT", END_GAME),],3),
            
            OPTION:             Menu(self, [Bouton((72, 168, 50, 15), (7, 0), "RETURN", None)],2),
            
            GAME_PAUSE:         Menu(self, [Bouton((72, 100, 150, 144), (7, 0), "PLAY", GAME), 
                                            Bouton((72, 120, 150, 164), (7, 0), "OPTION", OPTION), 
                                            Bouton((72, 140, 168, 182), (7, 0), "MAIN MENU", MAIN_MENU)],5),
            
            LOSE_SCREEN:        Menu(self, [Bouton((72, 168, 50, 15), (7, 0), "RETURN", MAIN_MENU)],8),

            WIN_SCREEN:         Menu(self, [Bouton((72, 168, 50, 15), (7, 0), "RETURN", MAIN_MENU)],7),
        }

        self.game_mode = WELCOME_SCREEN
        self.last_game_mode = WELCOME_SCREEN

        pyxel.load("my_resource.pyxres")

    def start(self):
        pyxel.run(self.update, self.draw)
    
    def quit_game(self):
        pyxel.quit()

    def pause(self):
        self.game_mode = GAME_PAUSE
    
    def change_mode(self, mode):
        self.last_game_mode = self.game_mode
        self.game_mode = mode

    def update(self):
        # juste pour afficher sur la console dans quel mode on est :
        if pyxel.frame_count % 50 == 0:
            print (self.game_mode, self.last_game_mode,self.world.world_game_mode, flush=True)

        if self.game_mode == END_GAME:
            self.quit_game()
        elif self.game_mode == GAME:
            if self.world.world_game_mode == 1:
                self.change_mode(WIN_SCREEN)
            elif self.world.world_game_mode == 2:
                self.change_mode(LOSE_SCREEN)
            else:
                pass
            self.world.update()
            if pyxel.btn(pyxel.KEY_P):
                self.pause()
        else:
            if self.menus[MAIN_MENU]:
                self.world.__init__(self)
            self.menus[self.game_mode].update()        

    def draw(self):
        pyxel.cls(1)
        if self.game_mode == GAME:
            self.world.draw()
        elif self.game_mode in self.menus:
            self.menus[self.game_mode].draw()

Game().start()
#===========================================================GAME============================================================
