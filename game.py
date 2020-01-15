import pygame

from settings import Settings
from landscape import Landscape


pygame.init()
canvas = pygame.display.set_mode(Settings.screen_size)

landscape = Landscape(canvas)

clock = pygame.time.Clock()

done = False
while not done:
    canvas.fill((0, 0, 0))
    landscape.draw()
    pygame.display.flip()
    landscape.update()
    clock.tick(10)
