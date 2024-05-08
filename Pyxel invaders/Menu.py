import pyxel
from App import *
from Credits import *
from Option import *

class Menu:
    def __init__(self):
        self.x = 140
        self.y = 260 
        self.selected_option = 0
        self.game_menu_exist = True
        self.menu_options_exist = False
        self.options_menu = None       
        self.credits_menu = None
        self.menu_credits_exist = False


        pyxel.init(self.x, self.y, title="Space Invaders", fps=60)
        pyxel.load("assets/sprites.pyxres")

        self.options = [
            "Start Game",
            "Options",
            "Credits",
            "Quit"
        ]

        pyxel.run(self.update, self.draw)

    def update(self):
        if self.game_menu_exist:
            self.make_choice_menu()
        
        if self.menu_options_exist:
            self.options_menu.update()  
        elif self.menu_credits_exist:
            self.credits_menu.update()
            

    def draw(self):
        pyxel.cls(0)
        pyxel.text(50, 100, "Space Invaders", pyxel.COLOR_LIGHT_BLUE)
        self.draw_menu_options()
        if self.menu_options_exist:
            self.options_menu.draw()
        elif self.menu_credits_exist:
            self.credits_menu.draw()    
    
    def draw_menu_options(self):
        for i, option in enumerate(self.options):
            color = pyxel.COLOR_YELLOW if i == self.selected_option else pyxel.COLOR_WHITE
            pyxel.text(50, 120 + i * 20, option, color)

    def start_game(self):
        self.app = App(self.x, self.y)
        pyxel.run(self.app.update, self.app.draw)

    def open_options(self):
        self.menu_options_exist = True  
        self.game_menu_exist = False
        self.options_menu = Option(self)

    def open_credits(self):
        self.menu_credits_exist = True
        self.game_menu_exist = False
        self.credits_menu = Credits(self)

    def make_choice_menu(self):
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.selected_option = (self.selected_option + 1) % len(self.options)
        elif pyxel.btnp(pyxel.KEY_UP):
            self.selected_option = (self.selected_option - 1) % len(self.options)
        if pyxel.btnp(pyxel.KEY_SPACE):
            if self.selected_option == 0:
                self.start_game()
            elif self.selected_option == 1:
                self.open_options()
            elif self.selected_option == 2:
                self.open_credits()
            elif self.selected_option == 3:
                pyxel.quit()

Menu()
