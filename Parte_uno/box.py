import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random 

class Box:
    def __init__(self):
        """
        Inicializa la maquina Turing con los estados para reconocer de la palabra 'box'.
        Define los estados y transiciones necesarios.
        """
        self.states = {
            0: {'b': (1, 'R')},
            1: {'o': (2, 'R')},
            2: {'x': (3, 'R')},
        }
        self.state = 0

    def process_word(self, word):
        """
        Realiza una transicion de estado basada en el caracter de entrada.

        Args:
            -->word (str):Palabra ingresada.

        Returns:
            -->bool:"True" si la transicion es valida, "False" si no lo es.
        """
        self.state = 0  #Reinicia el estado al inicio de procesar una nueva palabra

        for char in word:
            if self.state in self.states and char in self.states[self.state]:
                next_state, direction = self.states[self.state][char]
                print(f"Transicion: estado {self.state} -> {next_state} con '{char}'")
                self.state = next_state
            else:
                print(f"Error: '{char}' no es valido en el estado {self.state}")
                return False
            
        if self.state == 3:  #Si se llego al estado final, es porque se completo la palabra 'box'
            return True
        else:
            return False
    
    def show_boxes(self, boxes):
        """
        Muestra todos los rectángulos en una misma grafica con diferentes colores.

        Args:
            -->boxes (list):Lista de rectangulos, cada uno representado como un diccionario.
        """
        fig, ax = plt.subplots()

        colors = [plt.cm.viridis(i) for i in np.linspace(0, 1, len(boxes))]

        for idx, box in enumerate(boxes):
            w = box['width']
            l = box['length']
            name = box['name']
            pos = box['position']
            color = colors[idx]
            r = patches.Rectangle((pos[0], pos[1]), w, l, edgecolor=color, facecolor='none')
            ax.add_patch(r)
            ax.text(pos[0] + w / 2, pos[1] + l / 2, name, ha='center', va='center', fontsize=10, color=color)

        #Configura el grafico
        ax.set_xlim(-50, 50)
        ax.set_ylim(-50, 50)
        ax.set_aspect('equal', 'box')

        #Agregamos las lineas de los ejes
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)

        #Tambien incorporamos una cuadricula
        ax.grid(color='gray', linestyle='--', linewidth=0.5)

        #Muestra el grafico
        plt.title('( ^ω^) TODOS LOS RECTANGULOS ( ^ω^)')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()

def main():
    boxes = []
    b = Box()

    while True:
        print("\n♥━━━ M E N U ━━━♥")
        print("♥1. Agregar un rectangulo")
        print("♥2. Mover un rectangulo")
        print("♥3. Mostrar todos los rectangulos")
        print("♥4. Salir")
        choice = input("♥Selecciona una opcion ﾉﾉ1-2-3-4ﾉﾉ: ")

        if choice == '1':
            input_word = input("（っ◜◡◝）っ Ingresa la palabra ('box' para dibujar un rectangulo): ").lower()

            if input_word == 'box':
                w = float(input("♥Ingresa el ancho del rectangulo: "))
                l = float(input("♥Ingresa el largo del rectangulo: "))
                name = input("♥Ingresa el nombre del rectangulo: ")

                if b.process_word(input_word):
                    color=random.choice(['blue', 'orange', 'green', 'red', 'purple', 'teal', 'magenta', 'yellow'])
                    boxes.append({'width': w, 'length': l, 'name': name, 'position': (0, 0), 'color': color})
                    print(f"¡Has creado un rectangulo con ancho de {w}, un largo de {l} y nombre '{name}'!＼(>o<)／")
                    b.show_boxes(boxes)
                else:
                    print("(〒＿〒)Error: La palabra ingresada no es valida para crear un rectangulo.")

        elif choice == '2':
            if not boxes:
                print("(〒＿〒)No hay rectangulos para mover.")
                continue

            print("☆Rectangulos disponibles para mover:")
            for idx, box in enumerate(boxes):
                print(f"{idx + 1}. {box['name']}")

            try:
                idx_move = int(input("☆Selecciona el numero del rectangulo que deseas mover: ")) - 1
                if 0 <= idx_move < len(boxes):
                    new_x = float(input(f"☆Ingrese la nueva posicion X para '{boxes[idx_move]['name']}': "))
                    new_y = float(input(f"☆Ingrese la nueva posicion Y para '{boxes[idx_move]['name']}': "))
                    print(f"☆☆☆¡Moviendo el rectangulo '{boxes[idx_move]['name']}' a la posicion ({new_x}, {new_y})!☆☆☆")

                    #Actualizar posicion en la lista de rectangulos
                    boxes[idx_move]['position'] = (new_x, new_y)

                else:
                    print("(〒＿〒)Numero de rectangulo fuera de rango.")
            except ValueError:
                print("(〒＿〒)Entrada no valida. Debe ser un numero.")

        elif choice == '3':
            if not boxes:
                print("(〒＿〒)No hay rectangulos para mostrar.")
                continue
            b.show_boxes(boxes)

        elif choice == '4':
            print("ヘ(^_^ヘ)CHAUUU...")
            break

        else:
            print("(〒＿〒)Opcion no valida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
