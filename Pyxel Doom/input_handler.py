import pyxel

DISPLAY_FRAME = "display_frame"
DISPLAY_FACE = "display_face"

class InputHandler:
    def __init__(self, scene):
        
        self.scene = scene
        self.object3d = scene.object3d

    def handle_input(self):


        #Controle pour le  déplacement
        if pyxel.btn(pyxel.KEY_D):
            self.scene.move_object(-10, 0, 0)

        if pyxel.btn(pyxel.KEY_Q):
            self.scene.move_object(10, 0, 0)

        if pyxel.btn(pyxel.KEY_S):
            self.scene.move_object(0, 0, -10)

        if pyxel.btn(pyxel.KEY_Z):
            self.scene.move_object(0, 0, 10)


        #Controle pour le  déplacement verticale
        if pyxel.btn(pyxel.KEY_A):
            self.scene.move_object(0, -10, 0)

        if pyxel.btn(pyxel.KEY_E):
            self.scene.move_object(0, 10, 0)


        #Controle pour les rotation
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.object3d.rotate(0, 5, 0)

        if pyxel.btn(pyxel.KEY_LEFT):
            self.object3d.rotate(0, -5, 0)

        if pyxel.btn(pyxel.KEY_DOWN):
            self.object3d.rotate(5, 0, 0)

        if pyxel.btn(pyxel.KEY_UP):
            self.object3d.rotate(-5, 0, 0)


        #Controle pour afficher ou non les faces
        if pyxel.btnp(pyxel.KEY_F):
            if self.scene.display.display_mode == DISPLAY_FACE:
                self.scene.display.display_mode = DISPLAY_FRAME
            else:
                self.scene.display.display_mode = DISPLAY_FACE