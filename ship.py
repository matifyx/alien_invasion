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

        # Movemant flag; , beginne mit einem unbewegtem Schiff.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Aktualisiert die Position des Schiffs abhängig von Movement Flag"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Platziert das Schiff auf seine aktuelle Position"""
        self.screen.blit(self.image, self.rect)