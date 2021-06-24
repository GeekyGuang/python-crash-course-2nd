import sys
import pygame

from car import Car
from settings import Settings


class CarGame:
    """一款赛车游戏"""

    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)

        self.car = Car(self)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.car.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    car = CarGame()
    car.run_game()
