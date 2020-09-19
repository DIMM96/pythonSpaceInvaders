import sys
from settings import Settings #Se llama a la clase Settings de settings.py
from ship import Ship #Se llama a la clase Ship de ship.py
import pygame

class AlienInvasion:
    """Clase principal para manejar comportamientos y recursos del juego"""

    def __init__(self):
        """Se inicializa el juego y se crean los recursos del juego"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #Se inicializa la nave 

        self.ship = Ship(self)

        #Cambio de color de fondo en pantalla 
        self.bg_color = (230,230,230)

    def run_game(self):
        """Inicia loop principal del juego"""
        while True:
            #Se graban las interacciones de teclado y mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #La pantalla se renderiza de nuevo en cada loop
            self.screen.fill(self.settings.bg_color)

            #Nave 
            self.ship.blitme()

            #Muestra la pantalla mas reciente
            pygame.display.flip()


if __name__ == '__main__':
    #Instancia de la clase creada, corre juego
    ai = AlienInvasion()
    ai.run_game()