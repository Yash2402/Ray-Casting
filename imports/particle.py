import pygame
import math
from vector2d import Vector2D
from ray import Ray

class Particle():
    def __init__(self, x, y, color, heading):
        self.x = x
        self.y = y
        self.pos = Vector2D(self.x, self.y)
        self.rays = []
        self.color = color
        self.heading = heading
        for a in range(self.heading, self.heading + 50,  1):
            self.rays.append(Ray(self.pos.x, self.pos.y, math.radians(a), self.color))
        
    def show(self, screen):
        pygame.draw.circle(screen, self.color, self.pos.coordinates, 4)
 
    def rotate(self, a):
        self.heading += a

    def setPos(self, newx, newy):
        self.pos = Vector2D(newx, newy)

    def look(self, screen, walls):
        scene = []
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
            scene.append(record)
            if closest:
                    pygame.draw.aaline(screen, self.color, self.pos.coordinates, closest.coordinates)
        return scene