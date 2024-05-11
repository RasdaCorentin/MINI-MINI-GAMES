import pyxel
import math

maplist= [[1,1,1,1,1,1,1,1,1,1],
          [1,0,0,0,0,0,0,0,0,1],
          [1,0,1,0,1,0,1,1,0,1],
          [1,0,0,0,1,0,1,1,0,1],
          [1,0,0,0,0,0,0,0,0,1],
          [1,1,1,1,1,1,1,1,1,1]]
EXIT =(8,2)
PI = 3.14159265359

class Map:
    def __init__(self, maplist, EXIT):
        self.w = 1000
        self.h = 800
        self.pos_x, self.pos_y = (1,1)
        self.rot = PI / 4
        self.EXIT = EXIT
        self.maplist = maplist
        pyxel.init(self.w, self.h, title="Name", fps=60)
        pyxel.run( self.update , self.draw )

    def update(self):
        self.move()
        pyxel.cls(0)
        self.mapping(self.pos_x, self.pos_y)
    def draw(self):
        pass

    def mapping(self, player_x, player_y):
        for i in range(60):
            rot_i = self.rot + (i - 30) * PI / 180
            x, y = player_x, player_y
            sin, cos = 0.017 * math.sin(rot_i), 0.017 * math.cos(rot_i)
            distance = 0
            while True:
                x, y = x + cos, y + sin
                distance += 1
                if self.maplist[int(x)][int(y)] != 0:
                    height = min(12000 / distance, self.h / 2)  
                    break

            x_column = int(i * (self.w / 60)) 
            pyxel.rect(x_column, self.h / 3 - height, 10, height * 2.5, 3)
            

    def move(self):
        speed = 0.015  
        if pyxel.btn(pyxel.KEY_Z):
            self.pos_x += speed * math.cos(self.rot)  
            self.pos_y += speed * math.sin(self.rot) 
        if pyxel.btn(pyxel.KEY_S):
            self.pos_x -= speed * math.cos(self.rot) 
            self.pos_y -= speed * math.sin(self.rot) 
        if pyxel.btn(pyxel.KEY_Q):
            self.pos_x += speed * math.sin(self.rot)  
            self.pos_y -= speed * math.cos(self.rot)  
        if pyxel.btn(pyxel.KEY_D):
            self.pos_x -= speed * math.sin(self.rot)  
            self.pos_y += speed * math.cos(self.rot)

        if pyxel.btn(pyxel.KEY_LEFT):
            self.rot -= 0.03
            if self.rot <= -2 * PI:
                self.rot = 0
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.rot += 0.03
            if self.rot >= 2 * PI:
                self.rot = 0

Map(maplist, EXIT)

        