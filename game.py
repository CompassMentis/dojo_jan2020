import pygame

from settings import Settings
from landscape import Landscape
from dinosaur import Dinosaur

pygame.init()
canvas = pygame.display.set_mode(Settings.screen_size)

landscape = Landscape(canvas)
dinosaur = Dinosaur(canvas, landscape)

clock = pygame.time.Clock()

done = False
while not done:
    canvas.fill((0, 0, 0))
    landscape.draw()
    dinosaur.draw()
    pygame.display.flip()
    landscape.update()
    clock.tick(10)
