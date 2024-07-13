import math

import pygame

from imports.ray import Ray
from imports.vector2d import Vector2D


class Particle:
    def __init__(self, x, y, color: tuple, heading, FOV):
        self.x = x
        self.y = y
        self.rays = []
        self.pos = Vector2D(self.x, self.y)
        self.color = color
        self.heading = heading
        self.FOV = FOV

    def shootRays(self):
        self.a = self.heading - self.FOV / 2
        while int(self.a) != int(self.heading + self.FOV / 2):
            self.rays.append(
                Ray(self.pos.x, self.pos.y, math.radians(self.a), self.color)
            )
            self.a += 1

    def show(self, screen):
        pygame.draw.circle(screen, self.color, self.pos.coordinates, 5)

    def updateFOV(self, newFOV):
        self.rays = []
        self.FOV = newFOV
        self.a = self.heading - self.FOV / 2
        while int(self.a) != int(self.heading + self.FOV / 2):
            self.rays.append(
                Ray(self.pos.x, self.pos.y, math.radians(self.a), self.color)
            )
            self.a += 1

    def rotate(self, a):
        self.heading += a

    def setPos(self, newx, newy):
        self.pos = Vector2D(newx, newy)

    def look(self, screen, walls):
        scene = []
        colors = []

        for ray in self.rays:
            closest = None
            record = 10000000
            for wall in walls:
                pt = ray.cast(wall)
                if pt:
                    d = (self.pos - pt).mag()
                    if d < record:
                        record = d
                        closest = pt
                        ray.color = wall.color
            colors.append(ray.color)
            scene.append(record)
            if closest:
                pygame.draw.aaline(
                    screen, ray.color, self.pos.coordinates, closest.coordinates
                )
        return scene, colors


def polygon(sides, radius=1.0, rotation=0.0, translation=None):
    one_segment = math.pi * 2 / sides
    vertices = [
        (
            math.sin(one_segment * i + rotation) * radius,
            math.cos(one_segment * i + rotation) * radius,
        )
        for i in range(sides)
    ]
    if translation:
        vertices = [
            [sum(pair) for pair in zip(point, translation)] for point in vertices
        ]
    return vertices
