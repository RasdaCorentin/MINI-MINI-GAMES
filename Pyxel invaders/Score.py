import pyxel

class ScoreMenu:
    def __init__(self, score, dimx, dimy):
        self.score = score
        self.dimx = dimx
        self.dimy = dimy
        self.selected_option = 0
        self.options = ["OK"]

    def handle_input(self):
        if pyxel.btnp(pyxel.KEY_SPACE) and self.selected_option == len(self.options) - 1:
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)  # Efface l'écran avec la couleur noire
        text_x = self.dimx // 2 - 20  # Centre horizontalement le texte
        text_y = self.dimy // 2 - 20  # Centre verticalement le texte
        pyxel.text(text_x, text_y, "Score :", pyxel.COLOR_WHITE)  # Affiche le texte "Score :"
        pyxel.text(text_x, text_y + 20, str(self.score), pyxel.COLOR_WHITE)  # Affiche le score
        option_y = text_y + 60
        pyxel.text(text_x, option_y, self.options[0], pyxel.COLOR_YELLOW if self.selected_option == 0 else pyxel.COLOR_WHITE)
