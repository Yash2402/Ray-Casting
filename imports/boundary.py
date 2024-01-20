import pygame
from vector2d import Vector2D


class Boundary():   
    def __init__(self, x1, y1, x2, y2, width):
        self.a = Vector2D(x1, y1)
        self.b = Vector2D(x2, y2)
        self.width = width

    def show(self, screen):
        pygame.draw.aaline(screen, (255, 255, 255), self.a.coordinates, self.b.coordinates, self.width)

