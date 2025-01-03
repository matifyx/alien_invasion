import sys # wird benötigt damit der Spieler das Spiel beenden kann.
import pygame # enthält alles was zur Entwichlung eines Spiels benötigt wird.

class AlienInvasion:
    """Allgemeine Klasse zur Verwaltung von Spielwerten und Verhalten."""
    def __init__(self):
        """Initialisiert das Spiel und erstellt Spielresourcen"""
        pygame.init()
        # Fenster indem alle grafischen Elemente erstellt werden
        # Übergabe eines Tupels -> Fenstergröße 1200 x 800 Pixel (B x H)
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start der Hauptschleife für das Spiel."""
        while True:
            # reagiert auf Tastatur- und Mausereignisse.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Macht den zuletzt gezeichneten Bildschirm sichtbar.
            pygame.display.flip()

if __name__ == '__main__':
    # Erstellt eine Spielinstanz und führt das Spiel aus.
    ai = AlienInvasion()
    ai.run_game()