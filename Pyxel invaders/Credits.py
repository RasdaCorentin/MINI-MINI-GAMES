import pyxel

class Credits:
    def __init__(self, menu):
        self.menu = menu 
        self.selected_option = 0 
        self.options = ["WeeBoss",
                        "- Corentin",
                        "- Nolan",
                        "- Alexandre",
                        "- Jordan",
                        "Q to return to menu"
                        ]

    def update(self):
        # Logique de mise à jour du menu des crédits
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.selected_option = (self.selected_option + 1) % (len(self.options)-1)
        elif pyxel.btnp(pyxel.KEY_UP):
            self.selected_option = (self.selected_option - 1) % (len(self.options)-1)
        if pyxel.btnp(pyxel.KEY_Q):
            self.quit_to_menu()
                
    def draw(self):
        pyxel.cls(0)
        pyxel.text(50, 100, "Credits", pyxel.COLOR_LIGHT_BLUE)

        for i, option in enumerate(self.options):
                    color = pyxel.COLOR_YELLOW if i == self.selected_option else pyxel.COLOR_WHITE
                    pyxel.text(40, 120 + i * 20, option, color)
        
    def quit_to_menu(self):  
        if self.menu.menu_credits_exist:
            self.menu.game_menu_exist = True
            self.menu.menu_credits_exist = False