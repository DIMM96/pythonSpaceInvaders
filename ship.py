import pygame

class Ship:
    def __init__(self, ai_game):
        """Se inicializa la nave y se establece su posición inicial"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Se carga la imagen de la nave y se le asigna un rectangulo 
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Se inicia en el centro inferior una nueva nave al iniciar una partida 
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Se dibuja la nave en la posición establecida"""
        self.screen.blit(self.image, self.rect)
