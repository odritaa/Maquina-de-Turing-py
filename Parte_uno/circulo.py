import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random 

class Circulo:
    def __init__(self):
        """
        Inicializa la maquina de estados para reconocer la palabra 'circle'.
        Define los estados y transiciones necesarios.
        """
        self.states = {
            0: {'c': (1, 'R')},
            1: {'i': (2, 'R')},
            2: {'r': (3, 'R')},
            3: {'c': (4, 'R')},
            4: {'l': (5, 'R')},
            5: {'e': (6, 'R')}
        }
        self.state = 0

    def process_word(self, word):
        """
        Procesa una palabra ingresada por el usuario.

        Args:
            -->word (str): Palabra ingresada.

        Returns:
            -->bool: True si la palabra es correcta y se pudo crear el círculo, False si no.
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

        if self.state == 6:  #Si se llego al estado final, es porque se completo la palabra 'circle'
            return True
        else:
            return False

    def show_circles(self, circles):
        """
        Muestra todos los circulos en una misma gráfica con diferentes colores.

        Args:
            -->circles (list): Lista de circulos, cada uno representado como un diccionario {'radius': r, 'name': nombre, 'position': (x, y)}.
        """
        fig, ax = plt.subplots()

        colors = [plt.cm.viridis(i) for i in np.linspace(0, 1, len(circles))]

        for idx, circle in enumerate(circles):
            r = circle['radius']
            name = circle['name']
            pos = circle['position']
            color = colors[idx]
            circle = patches.Circle(pos, r, edgecolor=color, facecolor='none')
            ax.add_patch(circle)
            ax.text(pos[0], pos[1], name, ha='center', va='center', fontsize=10, color=color)

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
        plt.title('( ^ω^) TODOS TUS CIRCULOS ( ^ω^)')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()

def main():
    circles = []
    c = Circulo()

    while True:
        print("\n♥━━━ M E N U ━━━♥")
        print("♥1. Agregar un circulo")
        print("♥2. Mover un circulo")
        print("♥3. Mostrar todos los circulos")
        print("♥4. Salir")
        choice = input("♥Selecciona una opcion ﾉﾉ1-2-3-4ﾉﾉ: ")

        if choice == '1':
            input_word = input("（っ◜◡◝）っ Ingresa la palabra ('circle' para dibujar un circulo): ").lower()

            if input_word == 'circle':
                r = float(input("♥Ingresa el radio del circulo: "))
                name = input("♥Ingresa el nombre del circulo: ")

                if c.process_word(input_word):
                    color=random.choice(['blue', 'orange', 'green', 'red', 'purple', 'teal', 'magenta', 'yellow'])
                    circles.append({'radius': r, 'name': name, 'position': (0, 0), 'color': color})
                    print(f"¡Has creado un circulo con radio {r} y nombre '{name}'!＼(>o<)／")
                    c.show_circles(circles)
                else:
                    print("(〒＿〒)Error: La palabra ingresada no es valida para crear un circulo.")

        elif choice == '2':
            if not circles:
                print("(〒＿〒)No hay circulos para mover.")
                continue

            print("☆Circulos disponibles para mover:")
            for idx, circle in enumerate(circles):
                print(f"{idx + 1}. {circle['name']}")

            try:
                idx_move = int(input("☆Selecciona el numero del circulo que deseas mover: ")) - 1
                if 0 <= idx_move < len(circles):
                    new_x = float(input(f"☆Ingrese la nueva posicion X para '{circles[idx_move]['name']}': "))
                    new_y = float(input(f"☆Ingrese la nueva posicion Y para '{circles[idx_move]['name']}': "))
                    print(f"☆☆☆¡Moviendo el circulo '{circles[idx_move]['name']}' a la posicion ({new_x}, {new_y})!☆☆☆")

                    #Actualizar posicion en la lista de circulos
                    circles[idx_move]['position'] = (new_x, new_y)

                else:
                    print("(〒＿〒)Numero de circulo fuera de rango.")
            except ValueError:
                print("(〒＿〒)Entrada no valida. Debe ser un numero.")

        elif choice == '3':
            if not circles:
                print("(〒＿〒)No hay circulos para mostrar.")
                continue
            c.show_circles(circles)

        elif choice == '4':
            print("ヘ(^_^ヘ)CHAUUU...")
            break

        else:
            print("(〒＿〒)Opcion no valida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
