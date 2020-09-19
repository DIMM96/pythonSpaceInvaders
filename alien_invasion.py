import sys

import pygame

class AlienInvasion:
    """Clase principal para manejar comportamientos y recursos del juego"""

    def __init__(self):
        """Se inicializa el juego y se crean los recursos del juego"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game():
        """Inicia loop principal del juego"""
        while True:
            #Se graban las interacciones de teclado y mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Muestra la pantalla mas reciente
            pygame.display.flip()


if __name__ == '__main__':
    #Instancia de la clase creada, corre juego
    ai = AlienInvasion()
    ai.run_game