import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random

class shapes():
    def __init__(self):
        self.radio = 0
        self.ancho = 0
        self.alto = 0
        self.nombre = ""
        self.state = 0
        self.pos = 0,0
        self.angulo = 0

    def automata(self,word):
        salto = True
        word_sep = word.split()
        self.nombre = word_sep[-1]
        for part in word_sep:
            for char in part:
                if self.state == 0:
                    if char == 'c':
                        self.state += 1
                    if char == 'b':
                        self.state = 8
                    if char == 'm':
                        self.state = 13
                    if char == 's':
                        self.state = 19
                    if char == 'r':
                        self.state = 25
                if self.state == 1:
                    if char == 'i':
                        self.state += 1
                if self.state == 2:
                    if char == 'r':
                        self.state += 1
                if self.state == 3:
                    if char == 'c':
                        self.state += 1
                if self.state == 4:
                    if char == 'l':
                        self.state += 1
                if self.state == 5:
                    if char == 'e':
                        self.state += 1
                if self.state == 6:
                    if char.isnumeric():
                        if len(part) == 2:
                            self.radio = char  + part[part.index(char) +1]
                        else:
                            self.radio = char
                        self.state += 1
                if self.state == 8:
                    if char == 'o':
                        self.state += 1
                if self.state == 9:
                    if char == 'x':
                        self.state += 1
                if self.state == 10:
                    if char.isnumeric():
                        if len(part) == 2:
                            self.ancho = char + part[part.index(char) + 1]
                            self.state += 1
                            continue
                        else:
                            self.ancho = char
                            self.state += 1
                            continue
                if self.state == 11:
                    if char.isnumeric():
                        if len(self.ancho) == 2 and salto:
                            salto = False
                            continue
                        if len(part) == 2:
                            self.alto = char + part[part.index(char) + 1]
                            self.state += 1
                            continue
                        else:
                            self.alto = char
                            self.state += 1
                            continue
                if self.state == 13:
                    if char == 'o':
                        self.state += 1
                if self.state == 14:
                    if char == 'v':
                        self.state += 1
                if self.state == 15:
                    if char == 'e':
                        self.state += 1
                if self.state == 16:
                    if char.isnumeric():
                        if len(part) == 2:
                            self.x = char + part[part.index(char) + 1]
                            self.state += 1
                            continue
                        else:
                            self.x = char
                            self.state += 1
                            continue
                if self.state == 17:
                    if len(self.x) == 2 and salto:
                        salto = False
                        continue
                    if char.isnumeric():
                        if len(part) == 2:
                            self.y = char + part[part.index(char) + 1]
                            self.state += 1
                            continue
                        else:
                            self.y = char
                            self.state += 1
                            continue
                if self.state == 19:
                    if char == 'c':
                        self.state += 1
                if self.state == 20:
                    if char == 'a':
                        self.state += 1
                if self.state == 21:
                    if char == 'l':
                        self.state += 1
                if self.state == 22:
                    if char == 'e':
                        self.state += 1
                if self.state == 23:
                    if char.isnumeric():
                        if len(part) == 2:
                            self.x = char + part[part.index(char) + 1]
                            self.state += 1
                            continue
                        else:
                            self.x = char
                            self.state += 1
                            continue
                if self.state == 24:
                    if len(self.x) == 2 and salto:
                        salto = False
                        continue
                    if char.isnumeric():
                        if len(part) == 2:
                            self.y = char + part[part.index(char) + 1]
                            self.state += 1
                            continue
                        else:
                            self.y = char
                            self.state += 1
                            continue
                if self.state == 25:
                    if char == 'o':
                        self.state += 1
                if self.state == 26:
                    if char == 't':
                        self.state += 1
                if self.state == 27:
                    if char == 'a':
                        self.state += 1
                if self.state == 28:
                    if char == 't':
                        self.state += 1
                if self.state == 29:
                    if char == 'e':
                        self.state += 1
                if self.state == 30:
                    if char.isnumeric():
                        if len(part) == 2:
                            self.a = char  + part[part.index(char) +1] + '0'
                        else:
                            self.a = char + '0'
                        self.state += 1



        if self.state == 7 and int(self.radio) > 0 and self.nombre != "":
            return 7
        elif self.state == 12 and int(self.ancho) > 0 and int(self.alto) > 0 and self.nombre != "":
            return 12
        elif self.state == 18 and int(self.x) > 0 and int(self.y) > 0 and self.nombre != "":
            return 18
        elif self.state == 25 and int(self.x) > 0 and int(self.y) > 0 and self.nombre != "":
            return 25
        if self.state == 31 and int(self.a) > 0 and self.nombre != "":
            return 31
        else:
            return False

    def draw(self, shapes):
        fig, ax = plt.subplots()

        colors = [plt.cm.viridis(i) for i in np.linspace(0, 1, len(shapes))]
        idx = 0
        for shape in shapes:
            if int(shape.radio) > 0:
                r = int(shape.radio)
                name = shape.nombre
                color = colors[idx]
                pos = shape.pos
                circle = patches.Circle(pos, r, edgecolor=color, facecolor='none')
                ax.add_patch(circle)
                ax.text(pos[0], pos[1], name, ha='center', va='center', fontsize=10, color=color)
                idx += 1
            else:
                w = int(shape.ancho)
                l = int(shape.alto)
                name = shape.nombre
                pos = shape.pos
                color = colors[idx]
                r = patches.Rectangle((pos[0], pos[1]), w, l, edgecolor=color, facecolor='none', angle=int(self.angulo))
                ax.add_patch(r)
                ax.text(pos[0] + w / 2, pos[1] + l / 2, name, ha='center', va='center', fontsize=10, color=color)
                idx += 1

        # Configura el grafico
        ax.set_xlim(-50, 50)
        ax.set_ylim(-50, 50)
        ax.set_aspect('equal', 'box')

        # Agregamos las lineas de los ejes
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)

        # Tambien incorporamos una cuadricula
        ax.grid(color='gray', linestyle='--', linewidth=0.5)

        # Muestra el grafico
        plt.title('( ^ω^) TODAS TUS FORMAS ( ^ω^)')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()
    def rotate(self,a):
        self.angulo = a
    def move(self,x,y):
        self.pos = x,y
    def scale(self,x,y):
        self.ancho = int(self.ancho) * x
        self.alto = int(self.alto) * y
        if int(self.radio) > 0:
            self.radio = int(self.radio) * x









def main():
    while True:
        word = "box 10 10 nashe"
        formitas = []
        c = shapes()
        if (c.automata(word) == 12):
            formitas.append(c)
        c.scale(2,2)
        c.draw(formitas)






if __name__ == "__main__":
    main()
