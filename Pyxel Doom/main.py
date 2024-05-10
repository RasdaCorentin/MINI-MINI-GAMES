#mode d'affichage

DISPLAY_FRAME = "display_frame"
DISPLAY_FACE = "display_face"

import pyxel
import tkinter as tk
import math

class Display:
    def __init__(self):

        self.display_mode = DISPLAY_FRAME
        
        #permet de recuperer les  dimensions de l'écran
        root = tk.Tk()
        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()
        root.destroy()  # Fermer la fenêtre Tkinter après avoir obtenu les dimensions



class Object3D:
    def __init__(self, vertices, faces, position):

        #vertics sont les sommet de  la  figure à représenter
        self.vertices = vertices

        #les face de la figure à representer
        self.faces = faces

        #sa position dans l'espace
        self.position = position

    def __str__(self):
        # Retourne une représentation textuelle de l'objet
        return f"Object3D(vertices={self.vertices}, faces={self.faces}, position={self.position})"
    
    #créer l'image du cube
    def project(self, camera_position):
        projected_vertices = []
        for vertex in self.vertices:

            # Projection perspective simple
            #échelle par rapport à la distance de la caméra
            # caméra_z est le pov divisé par caméra_z
            scale_factor = camera_position[2] / (camera_position[2] - vertex[2])
            projected_x = vertex[0] * scale_factor + camera_position[0]
            projected_y = vertex[1] * scale_factor + camera_position[1]

            #on rentre les coordonée de la figure  selon x et y après projection 
            projected_vertices.append((projected_x, projected_y))
        
        return projected_vertices

    def move(self, dx, dy, dz):

        # Déplacer l'objet en ajoutant les valeurs de déplacement aux coordonnées de sa position
        self.position = (self.position[0] + dx, self.position[1] + dy, self.position[2] + dz)

        # Mettre à jour les coordonnées des sommets en fonction de la nouvelle position
        self.vertices = [[vertex[0] + dx, vertex[1] + dy, vertex[2] + dz] for vertex in self.vertices]

    def rotate(self, angle_x, angle_y, angle_z):

        # Convertit les angles en radians
        angle_x_rad = math.radians(angle_x)
        angle_y_rad = math.radians(angle_y)
        angle_z_rad = math.radians(angle_z)

        # Calcule les valeurs de sin et cos de chaque angle
        sin_x = math.sin(angle_x_rad)
        cos_x = math.cos(angle_x_rad)
        sin_y = math.sin(angle_y_rad)
        cos_y = math.cos(angle_y_rad)
        sin_z = math.sin(angle_z_rad)
        cos_z = math.cos(angle_z_rad)

        # Applique la rotation à chaque sommet autour des axes X, Y et Z
        for i, vertex in enumerate(self.vertices):
            x, y, z = vertex
            # Rotation autour de l'axe X
            new_y = y * cos_x - z * sin_x
            new_z = z * cos_x + y * sin_x
            y, z = new_y, new_z
            # Rotation autour de l'axe Y
            new_x = x * cos_y - z * sin_y
            new_z = z * cos_y + x * sin_y
            x, z = new_x, new_z
            # Rotation autour de l'axe Z
            new_x = x * cos_z - y * sin_z
            new_y = y * cos_z + x * sin_z
            x, y = new_x, new_y
            # Mise à jour des coordonnées du sommet
            self.vertices[i] = [x, y, z]
    
    
    def move_forward(self, distance):
        # Move forward along the z-axis
        self.position = (self.position[0], self.position[1], self.position[2] - distance)

    def move_backward(self, distance):
        # Move backward along the z-axis
        self.position = (self.position[0], self.position[1], self.position[2] + distance)



class Game:
    def __init__(self):

        self.display = Display()

        # Projection de l'objet
        self.camera_position = self.camera_position = [self.display.width / 2, self.display.height / 2, 200]
        #on appelle la classe object avec les information de la figure à représenter
        self.object = Object3D(

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
                [0, 1, 5, 4],  # Côté gauche
                [2, 3, 7, 6],  # Côté droit
                [0, 3, 7, 4],  # Haut
                [1, 2, 6, 5]   # Bas
            ],
            position=(0, 0, 0)  # Position initiale du cube 
        )


        pyxel.init(self.display.width-200, self.display.height-200, title="3D Projection", fps=60)
        pyxel.run(self.update, self.draw)





    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.camera_position[0] -= 10
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.camera_position[0] += 10
        if pyxel.btn(pyxel.KEY_UP):
            self.camera_position[1] -= 10
        if pyxel.btn(pyxel.KEY_DOWN):
            self.camera_position[1] += 10
            
        # Vérifiez les entrées de l'utilisateur ou mettez en œuvre une logique de déplacement prédéfinie
        if pyxel.btn(pyxel.KEY_Q):
            self.object.rotate(0,5,0)     

        if pyxel.btn(pyxel.KEY_D):
            self.object.rotate(0,-5,0)

        if pyxel.btn(pyxel.KEY_Z):
            self.object.rotate(5,0,0)

        if pyxel.btn(pyxel.KEY_S):
            self.object.rotate(-5,0,0)


        if pyxel.btn(pyxel.KEY_A):
            self.object.move_forward(10)
        if pyxel.btn(pyxel.KEY_E):
            self.object.move_backward(10)
            

        if pyxel.btnp(pyxel.KEY_F):
            if self.display.display_mode == DISPLAY_FACE:
                self.display.display_mode = DISPLAY_FRAME
            else:
                self.display.display_mode = DISPLAY_FACE

        #pyxel.mouse(True)
        #if pyxel.frame_count % 30 == 0:
        #    print(pyxel.mouse_x,pyxel.mouse_y)



    def draw(self):
        pyxel.cls(0)

        projected_vertices = self.object.project(self.camera_position)

        if self.display.display_mode == DISPLAY_FACE:
            
            self.draw_faces(projected_vertices)
        
        if self.display.display_mode == DISPLAY_FRAME:
            self.draw_lines(projected_vertices)

    def draw_faces(self, projected_vertices):
        for index, face in enumerate(self.object.faces):
            # Les indices des sommets définissant la face
            vertex_indices = face

            # Coordonnées projetées des sommets de la face
            projected_points = [projected_vertices[i] for i in vertex_indices]

            # Déterminer la couleur en fonction de l'index de la face
            color = 7  # Par défaut, la couleur des murs

            if index == 1 and index == 3:
                color = 13  # Partie haute

            if index == 2:
                color = 3  # Partie haute


            # Dessiner chaque triangle de la face
            for i in range(len(projected_points) - 2):
                # Coordonnées des sommets du triangle
                x1, y1 = projected_points[0]
                x2, y2 = projected_points[i + 1]
                x3, y3 = projected_points[i + 2]

                # Dessiner le triangle rempli avec la couleur
                pyxel.tri(x1, y1, x2, y2, x3, y3, color)
    def draw_lines(self, projected_vertices):
        # Dessin des faces
        for face in self.object.faces:
            for i in range(len(face)):
                # Indice du premier sommet de la face
                vertex_index1 = face[i]
                # Indice du deuxième sommet de la face (boucle circulaire)
                vertex_index2 = face[(i + 1) % len(face)]

                # Coordonnées projetées des sommets
                x1, y1 = projected_vertices[vertex_index1]
                x2, y2 = projected_vertices[vertex_index2]

                # Dessiner la ligne entre les sommets projetés
                pyxel.line(x1, y1, x2, y2, 7)

Game()
