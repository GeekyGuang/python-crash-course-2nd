import pygame


class Car:

    def __init__(self, car_game):
        self.screen = car_game.screen
        self.screen_rect = car_game.screen.get_rect()

        self.image = pygame.image.load('images/car.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
