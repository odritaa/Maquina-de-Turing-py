import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Circulo:
    def __init__(self):
        """
        Inicializa la maquina Turing con los estados para reconocer de la palabra 'circle'.
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
            word (str):Palabra ingresada.

        Returns:
            bool: "True" si la palabra es correcta, "False" si no lo es.
        """
        for char in word:
            if self.state in self.states and char in self.states[self.state]:
                next_state, direction = self.states[self.state][char]
                print(f"Transicion: estado {self.state} -> {next_state} con '{char}'")
                self.state = next_state
            else:
                print(f"Error: '{char}' no es valido en el estado {self.state}")
                return False
        return self.state == 6

    def draw_circle(self, r):
        """
        Dibuja un circulo.

        Args:
            r (float): Radio del circulo.
        """
        #Creamos la figura y un eje
        fig, ax = plt.subplots()

        #Se crea un circulo con patches.Circle
        circle = patches.Circle((0, 0), r, edgecolor='magenta', facecolor='none')
        ax.add_patch(circle)

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
        plt.title(f'El circulo cuenta con un radio de {r}.')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()

def main():
    c = Circulo()
    r = 5  #Radio del circulo

    input_word = input("Ingresa la palabra: ").lower()

    #Se verifica si la palabra ingresada es correcta y se visualiza el circulo
    if c.process_word(input_word):
        print("¡LOGRASTE COMPLETAR EL CIRCULO, FELICITACIONES!")
        c.draw_circle(r)
    else:
        print("LO SIENTO, la palabra es incorrecta :c")
        print("El circulo no se pudo completar. ¡Volve a intentarlo!")

if __name__ == "__main__":
    main()
