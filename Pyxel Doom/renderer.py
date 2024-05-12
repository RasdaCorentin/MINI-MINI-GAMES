import pyxel

PALETTE_COULEURS = [
    (0, 0, 0),       # Noir  =  (indice 0)
    (43, 51, 95),     # Bleu foncé -  (indice 1)
    (126, 32, 144),     # Violet  =  (indice 2)
    (25, 149, 156),     # Vert foncé  -  (indice 3)
    (139, 72, 82),   # Marron =  (indice 4)
    (57, 92, 152),       # Bleu  -  (indice 5)
    (169, 193, 255),     # Bleu très claire =  (indice 6)
    (238, 238, 238),     # Blanc  -  (indice 7)
    (212, 24, 108),     # Rouge  =  (indice 8)
    (211, 132, 65),   # Orange -  (indice 9)
    (233, 195, 91),       # Jaune  =  (indice 10)
    (112, 198, 169),     # Vert clair -  (indice 11)
    (118, 150, 222),     # Bleu clair  =  (indice 12)
    (163, 163, 163),     # Gris  -  (indice 13)
    (255, 151, 152),   # Orange clair =  (indice 14)
    (237, 199, 176),   # Orange très claire -  (indice 15)
]


class Renderer:
    def __init__(self, display, object3d, camera):
        self.display = display
        self.object3d = object3d
        self.camera = camera

    def draw_faces(self, projected_vertices):
        for face_data in self.object3d.faces:
            vertex_indices, color_index = face_data[:2]
            projected_points = [projected_vertices[i] for i in vertex_indices]

            # Utiliser directement l'indice de couleur comme valeur de couleur pour Pyxel
            color = color_index

            # Dessiner chaque triangle de la face
            for i in range(len(projected_points) - 2):
                x1, y1 = projected_points[0]
                x2, y2 = projected_points[i + 1]
                x3, y3 = projected_points[i + 2]

                # Dessiner le triangle rempli avec la couleur
                pyxel.tri(x1, y1, x2, y2, x3, y3, color)

    def draw_lines(self, projected_vertices):
        for face in self.object3d.faces:
            vertex_indices, color_index, *_ = face  # Ignorer les autres données éventuelles
            for i in range(len(vertex_indices)):
                vertex_index1 = vertex_indices[i]
                vertex_index2 = vertex_indices[(i + 1) % len(vertex_indices)]

                x1, y1 = projected_vertices[vertex_index1]
                x2, y2 = projected_vertices[vertex_index2]

                # Dessiner la ligne entre les sommets projetés
                pyxel.line(x1, y1, x2, y2, 7)  # Couleur de la ligne