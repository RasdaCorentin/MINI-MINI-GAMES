import pyxel

class Boss:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.bar_speed = 2
        self.boss_speed = 2
        self.life = 110
        self.barre_chargement = 0

    def draw(self):
        # Barre de vie du boss
        pyxel.rect(self.x -10, self.y + 35, self.life, 2, 2)
        
    def chargement_barre(self): 
        self.barre_chargement += self.bar_speed / 7
        if self.barre_chargement > 16 :
            self.barre_chargement = 0

class Boss_right_side(Boss):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.w = 20
        self.h = 33

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 156, 23, self.w, self.h, 0)

    def move(self, pos_final):
        if self.y < pos_final:
            self.y += self.boss_speed / 7
    
class Boss_left_side(Boss):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.w = 20
        self.h = 33
        
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 80, 23, self.w, self.h, 0)

    def move(self, pos_final):
        if self.y < pos_final:
            self.y += self.boss_speed / 7


class Boss_tiny_left_side(Boss):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.w = 7
        self.h = 9

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 72, 35, self.w, self.h, 0)

    def move(self, pos_final):
        if self.y < pos_final:
            self.y += self.boss_speed /2


class Boss_tiny_right_side(Boss):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.w = 7
        self.h = 9
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 177, 35, self.w, self.h, 0)

    def move(self, pos_final):
        if self.y < pos_final:
            self.y += self.boss_speed /2

class Boss_center(Boss):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.w = 56
        self.h = 19
        self.boss_speed = 1 
        
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 101, 30, self.w, self.h, 0)
        super().draw()
    
    def move(self, pos_final):
        if self.y < pos_final:
            self.y += self.boss_speed / 8

