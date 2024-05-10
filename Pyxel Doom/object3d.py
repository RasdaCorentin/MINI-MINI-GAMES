import math

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

    def set_position(self, x, y, z):
        self.position = (x, y, z)

    #créer l'image du cube
    def project(self, camera_position):
        projected_vertices = []
        for vertex in self.vertices:
            # Calculer les coordonnées relatives du sommet par rapport à la position de l'objet
            relative_x = vertex[0] + self.position[0]
            relative_y = vertex[1] + self.position[1]
            relative_z = vertex[2] + self.position[2]

            # Calculer la distance entre le sommet relatif et la caméra
            dx = relative_x - camera_position[0]
            dy = relative_y - camera_position[1]
            dz = relative_z - camera_position[2]

            # Projection perspective
            if dz != 0:
                scale_factor = camera_position[2] / dz
                projected_x = dx * scale_factor + camera_position[0]
                projected_y = dy * scale_factor + camera_position[1]
            else:
                projected_x = relative_x
                projected_y = relative_y

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
        """
        Rapproche l'objet de la caméra en déplaçant sa position le long de l'axe Z.
        """
        self.position = (self.position[0], self.position[1], self.position[2] + distance)

    def move_backward(self, distance):
        """
        Éloigne l'objet de la caméra en déplaçant sa position le long de l'axe Z.
        """
        self.position = (self.position[0], self.position[1], self.position[2] - distance)