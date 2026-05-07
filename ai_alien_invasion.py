import sys
import pygame
from settings import Settings
from ship import Ship


class AI_AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Set the dimensions of the window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        # Set the window tile
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Fill the screen with a background color.
        self.screen.fill(self.settings.bg_color)

        # Draw the ship
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
        self.clock.tick(60)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    ai = AI_AlienInvasion()
    ai.run_game()
