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

    def automata(self,word):
        x = 0
        y = 0
        a = 0
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
                            x = char + part[part.index(char) + 1]
                            self.state += 1
                            continue
                        else:
                            x = char
                            self.state += 1
                            continue
                if self.state == 17:
                    if char.isnumeric():
                        if len(part) == 2:
                            y = char + part[part.index(char) + 1]
                            self.state += 1
                            continue
                        else:
                            y = char
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
                            x = char + part[part.index(char) + 1]
                            self.state += 1
                            continue
                        else:
                            x = char
                            self.state += 1
                            continue
                if self.state == 24:
                    if char.isnumeric():
                        if len(part) == 2:
                            y = char + part[part.index(char) + 1]
                            self.state += 1
                            continue
                        else:
                            y = char
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
                            a = char  + part[part.index(char) +1] + '0'
                        else:
                            a = char + '0'
                        self.state += 1

        print(self.state)


        if self.state == 7 and int(self.radio) > 0 and self.nombre != "":
            return True
        elif self.state == 12 and int(self.ancho) > 0 and int(self.alto) > 0 and self.nombre != "":
            return True
        elif self.state == 18 and int(x) > 0 and int(y) > 0 and self.nombre != "":
            return x,y,True
        elif self.state == 25 and int(x) > 0 and int(y) > 0 and self.nombre != "":
            return x,y,True
        if self.state == 31 and int(a) > 0 and self.nombre != "":
            return a,True
        else:
            return False





def main():
    word = "move 9 8 nashe"
    fprmitas = []
    c = shapes()
    print(c.automata(word))
    # circle3 = plt.Circle((0, 0), int(c.radio))
    #
    # fig, ax = plt.subplots()  # note we must use plt.subplots, not plt.subplot
    # # (or if you have an existing figure)
    # # fig = plt.gcf()
    # # ax = fig.gca()
    # ax.set_xlim(-50, 50)
    # ax.set_ylim(-50, 50)
    # ax.set_aspect('equal', 'box')
    #
    # ax.add_patch(circle3)
    # plt.show()


if __name__ == "__main__":
    main()