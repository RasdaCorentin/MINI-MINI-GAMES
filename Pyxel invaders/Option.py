import pyxel 

class Option:
    def __init__(self, menu):
        self.menu = menu
        self.selected_option = 0
        self.options = [
            "Change Difficulty",
            "Press Q to return to menu"
        ]

    def update(self):
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.selected_option = (self.selected_option + 1) % len(self.options)
        elif pyxel.btnp(pyxel.KEY_UP):
            self.selected_option = (self.selected_option - 1) % len(self.options)

        if pyxel.btnp(pyxel.KEY_SPACE):
            if self.selected_option == 0:
                pass
        if pyxel.btnp(pyxel.KEY_Q):
            self.quit_to_menu()

    def quit_to_menu(self):  
        if self.menu.menu_options_exist:
            self.menu.game_menu_exist = True
            self.menu.menu_options_exist = False
    
    def draw(self):
        pyxel.cls(0)
        pyxel.text(50, 100, "Options", pyxel.COLOR_LIGHT_BLUE)
        for i, option in enumerate(self.options):
            color = pyxel.COLOR_YELLOW if i == self.selected_option else pyxel.COLOR_WHITE
            pyxel.text(40, 120 + i * 20, option, color)
