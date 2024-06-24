import matplotlib.pyplot as plt
import matplotlib.patches as patches

class TuringMachine:
    def __init__(self):
        """
        Inicializa la maquina de Turing para reconocer la palabra 'box'.
        Define los estados y transiciones necesarios.
        """
        self.states = {
            0: {'b': (1, 'R')},
            1: {'o': (2, 'R')},
            2: {'x': (3, 'R')},
        }
        self.head_position = 0
        self.current_state = 0

    def step(self, input_char):
        """
        Realiza una transicion de estado basada en el caracter de entrada.

        Args:
            input_char (str):Caracter ingresado por el usuario.

        Returns:
            bool:True si la transicion es valida, False si no lo es.
        """
        #Se simula el comportamiento de una maquina de Turing, evalua cada caracter de entrada en self.states.
        if input_char in self.states[self.current_state]:
            next_state, direction = self.states[self.current_state][input_char]
            if direction == 'R':
                self.head_position += 1
            elif direction == 'L':
                self.head_position -= 1
            self.current_state = next_state
            return True
        else:
            return False

    def draw_rectangle(self, ancho, alto):
        """
        Dibuja un rectangulo en base al ancho y alto dados.

        Args:
            ancho (float):Ancho del rectangulo.
            alto (float):Alto del rectangulo.
        """
        fig, ax = plt.subplots()

        #Dibuja el rectangulo
        rectangle = patches.Rectangle((0, 0), ancho, alto, edgecolor='magenta', linewidth=2, fill=False)
        ax.add_patch(rectangle)

        #Configura el grafico
        ax.set_xlim(0, ancho + 1)
        ax.set_ylim(0, alto + 1)
        ax.set_aspect('equal', 'box')

        #Muestra el grafico
        plt.title(f'Rectangulo: Ancho={ancho}, Alto={alto}')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()

        #Retorna el objeto rectangulo creado
        return rectangle

def main():
    tm = TuringMachine()
    ancho = 8.0
    alto = 4.0
    progress = 0

    while tm.current_state != 3:
        input_char = input(f"Ingresa la letra numero {progress + 1}: ").lower()

        if tm.step(input_char):
            progress += 1
            if tm.current_state == 3:
                tm.draw_rectangle(ancho, alto)
        else:
            print("LO SIENTO, la letra es incorrecta :c")
            break

    if tm.current_state == 3:
        print("¡HAZ COMPLETADO EL RECTANGULO, FELICITACIONES!")
    else:
        print("El rectangulo no se pudo completar. ¡Volve a intentarlo!")

if __name__ == "__main__":
    main()
