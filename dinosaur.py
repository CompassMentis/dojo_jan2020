import pygame

from settings import Settings


class Dinosaur:
    def __init__(self, canvas, landscape):
        self.image = pygame.image.load('dinosaur.png')
        self.canvas = canvas
        self.landscape = landscape
        self.rect = self.image.get_rect()
        self.height = self.rect.height

    def draw(self):
        self.canvas.blit(self.image, (Settings.centre_x, self.landscape.dinosaur_height - self.height))
