import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Circulo:
    def __init__(self):
        """
        Inicializa la maquina de Turing para reconocer la palabra 'circle'.
        Define los estados y transiciones necesarios.
        """
        self.states = {
            0: {'c': (1, 'R')},
            1: {'i': (2, 'R')},
            2: {'r': (3, 'R')},
            3: {'c': (4, 'R')},
            4: {'l': (5, 'R')},
            5: {'e': (6, 'R')},
        }
        self.head_position = 0
        self.state = 0

    def step(self, input_char):
        """
        Realiza una transicion de estado basada en el caracter de entrada.

        Args:
            input_char (str):Caracter ingresado por el usuario.

        Returns:
            bool:True si la transicion es valida, False si no lo es.
        """
        #Se simula el comportamiento de una maquina de Turing, evalua cada caracter de entrada en self.states
        if input_char in self.states[self.state]:
            next_state, direction = self.states[self.state][input_char]
            if direction == 'R':
                self.head_position += 1
            elif direction == 'L':
                self.head_position -= 1
            self.state = next_state
            return True
        else:
            return False

    def draw_circle(self, progress, r):
        """
        Se dibuja un arco de circulo en funcion del progreso.

        Args:
            progress (int):Numero de letras correctas ingresadas.
            r (float):Radio del circulo.
        """
        #Creamos la figura y un eje
        fig, ax = plt.subplots()

        if progress > 0:
            theta1 = 0 #Es el angulo medido en grados o radianes.
            theta2 = (progress / 6) * 360 
            #Se muestra el proceso del mismo, en donde los 360 grados corresponden a 6 letras
        
            #Se crea un arco que representa el progreso del circulo con patches.Arc
            arc = patches.Arc((0, 0), 2*r, 2*r, angle=0, theta1=theta1, theta2=theta2, edgecolor='magenta')
            ax.add_patch(arc)

        #Establecemos los limites
        ax.set_xlim(-r-1, r+1)
        ax.set_ylim(-r-1, r+1)
        ax.set_aspect('equal', 'box')

        #Agregamos las lineas de los ejes
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)

        #Tambien incorporamos una cuadricula
        ax.grid(color='gray', linestyle='--', linewidth=0.5)

        #Mostramos el grafico
        plt.title(f'El circulo cuenta con radio de {r}. Completa el proceso {progress}/6')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()

def main():
    c = Circulo()
    r = 5  #Radio del circulo
    progress = 0  #Inicializamos el progreso 

    while c.state != 6:
        input_char = input(f"Ingresa la letra numero {progress + 1}: ").lower()

        #Se actualiza visualmente el avance del crculo y se gestiona la deteccion de errores durante el proceso.
        if c.step(input_char): 
            progress += 1
            if c.state ==6:
                c.draw_circle(progress, r)
        else:
            print("LO SIENTO, la letra es incorrecta :c")
            break

    if c.state == 6:
        print("¡HAZ COMPLETADO EL CIRCULO, FELICITACIONES!")
    else:
        print("El circulo no se pudo completar. ¡Volve a intentarlo!")
        

if __name__ == "__main__":
    main()
