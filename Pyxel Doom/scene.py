
import pyxel
from display import Display
from input_handler import InputHandler
from object3d import Object3D
from renderer import Renderer
from camera import Camera

class Scene:
    def __init__(self):
        self.display = Display()
        self.camera = Camera(self.display)
        self.object3d = Object3D(
            vertices=[
        [-50, -50, -50],  # Sommet 1
        [50, -50, -50],   # Sommet 2
        [50, 50, -50],    # Sommet 3
        [-50, 50, -50],   # Sommet 4
        [-50, -50, 50],   # Sommet 5
        [50, -50, 50],    # Sommet 6
        [50, 50, 50],     # Sommet 7
        [-50, 50, 50]     # Sommet 8
    ],
    faces=[
        ([0, 1, 2, 3],2),  # Face avant
        ([4, 5, 6, 7],3),  # Face arrière
        ([0, 1, 5, 4],4),  # Côté gauche
        ([2, 3, 7, 6],5),  # Côté droit
        ([0, 3, 7, 4],8),  # Haut
        ([1, 2, 6, 5],9),   # Bas
    ],
    position=(self.display.width/2, self.display.height/2, -100),

    
        )
        
        self.renderer = Renderer(self.display, self.object3d, self.camera)
        self.input_handler = InputHandler(self)

        pyxel.init(self.display.width - 200, self.display.height - 200, title="3D Projection", fps=60)

    def change_face_color(self, face_index, color_tuple):
        self.object3d.face_colors[face_index] = color_tuple

    def run(self):
        pyxel.run(self.update, self.draw)

    def update(self):
        self.input_handler.handle_input()

    def draw(self):
        pyxel.cls(0)
        projected_vertices = self.object3d.project(self.camera.position)

        if self.display.display_mode == "display_face":
            self.renderer.draw_faces(projected_vertices)
        else:
            self.renderer.draw_lines(projected_vertices)

    
    def move_object(self, dx, dy, dz):

        self.object3d.set_position(self.object3d.position[0] + dx,
                                   self.object3d.position[1] + dy,
                                   self.object3d.position[2] + dz)
