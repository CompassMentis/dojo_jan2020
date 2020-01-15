import random
from collections import deque

import pygame

from settings import Settings


class Landscape:
    def __init__(self, canvas):
        self.canvas = canvas
        self.heights = deque()
        self.current = 0
        for _ in range(Settings.screen_width):
            self.next_height()
            self.heights.append(int(self.current))

    def update(self):
        self.heights.popleft()
        self.next_height()
        self.heights.append(int(self.current))

    def next_height(self):
        self.current += random.randint(-1, 1) / 2
        self.current = max(min(self.current, Settings.terrain_height), -Settings.terrain_height)

    def draw(self):
        for x in range(Settings.screen_width):
            pygame.draw.line(
                self.canvas,
                Settings.terrain_colour,
                (x, Settings.screen_height - 1),
                (x, Settings.terrain_base + self.heights[x])
            )
