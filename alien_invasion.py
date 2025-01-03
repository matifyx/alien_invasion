import sys # wird benötigt damit der Spieler das Spiel beenden kann.
import pygame # enthält alles was zur Entwichlung eines Spiels benötigt wird.
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Allgemeine Klasse zur Verwaltung von Spielwerten und Verhalten."""
    def __init__(self):
        """Initialisiert das Spiel und erstellt Spielresourcen"""
        pygame.init()
        # Erstellen einer Instanz der Klasse 'clock'
        # Damit wird die Uhr am Ende der While-Schleife in run_game()
        # zum Ticken gebracht
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        # Fenster indem alle grafischen Elemente erstellt werden
        # Fenster in Vollbildmodus
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

        # Legt die Hintergrundfarbe fest.
        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        """Start der Hauptschleife für das Spiel."""
        while True:
            self._check_events() # Methoden nur innerhalb der Klasse verfügbar 
            self.ship.update()
            self._update_screen() # (Punktschreibweise)
            self.clock.tick(60)

    # Code aus run_game in neue Methode eingefügt
    def _check_events(self):
            # reagiert auf Tastatur- und Mausereignisse.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)                     

    def _check_keydown_events(self, event):
        """Reagiert auf Tastenbetätigung"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Reagiert auf Tastenbetätigung"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    # Code aus run_game in neue Methode eingefügt
    def _update_screen(self):
            # Zeichnet den Bildschirm bei jedem Schleifendurchlauf neu.
            self.screen.fill(self.bg_color)
            self.ship.blitme()
            # Macht den zuletzt gezeichneten Bildschirm sichtbar.
            pygame.display.flip()      

if __name__ == '__main__':
    # Erstellt eine Spielinstanz und führt das Spiel aus.
    ai = AlienInvasion()
    ai.run_game()