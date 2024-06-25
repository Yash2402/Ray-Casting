import pygame

from imports.vector2d import Vector2D


class Boundary:
    def __init__(self, x1, y1, x2, y2, color, width):
        self.a = Vector2D(x1, y1)
        self.b = Vector2D(x2, y2)
        self.width = width
        self.color = color

    def show(self, screen):
        pygame.draw.aaline(screen, self.color, self.a.coordinates, self.b.coordinates, self.width)
