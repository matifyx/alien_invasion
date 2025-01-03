import pygame

class Ship():
    """Klasse für die Verwaltung des Schiffs"""

    def __init__(self, ai_game):
        """Initialisiert das Schiff und setzt es auf die Startposition"""        
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Lädt das Bild des Schiffes und ruft dessen umgebendes Rechteck ab.
        self.image = pygame.image.load('images\ship.bmp')
        self.rect = self.image.get_rect()

        # Platziert jedes neue Schiff mittig am unteren Bildschirmrand.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Platziert das Schiff auf seine aktuelle Position"""
        self.screen.blit(self.image, self.rect)