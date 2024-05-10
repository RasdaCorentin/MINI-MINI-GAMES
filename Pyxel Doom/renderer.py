import pyxel

class Renderer:
    def __init__(self, display, object3d, camera):
        self.display = display
        self.object3d = object3d
        self.camera = camera

    def draw_faces(self, projected_vertices):
        for index, face in enumerate(self.object3d.faces):
            vertex_indices = face
            projected_points = [projected_vertices[i] for i in vertex_indices]
            color = 7  # Couleur par défaut

            # Définir la couleur en fonction de l'index de la face
            if index == 1 or index == 3:
                color = 13  # Couleur pour les faces 1 et 3

            if index == 2:
                color = 3  # Couleur pour la face 2

            # Dessiner chaque triangle de la face
            for i in range(len(projected_points) - 2):
                x1, y1 = projected_points[0]
                x2, y2 = projected_points[i + 1]
                x3, y3 = projected_points[i + 2]

                # Dessiner le triangle rempli avec la couleur
                pyxel.tri(x1, y1, x2, y2, x3, y3, color)

    def draw_lines(self, projected_vertices):
        for face in self.object3d.faces:
            for i in range(len(face)):
                vertex_index1 = face[i]
                vertex_index2 = face[(i + 1) % len(face)]

                x1, y1 = projected_vertices[vertex_index1]
                x2, y2 = projected_vertices[vertex_index2]

                # Dessiner la ligne entre les sommets projetés
                pyxel.line(x1, y1, x2, y2, 7)  # Couleur de la ligne
