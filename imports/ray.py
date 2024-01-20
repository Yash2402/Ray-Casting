import pygame
import math
from boundary import Boundary
from vector2d import Vector2D

class Ray():
    def __init__(self, x, y, angle, color):
        self.pos = Vector2D(x, y)
        self.angle = angle
        self.dir = Vector2D(math.cos(angle), math.sin(angle))
        self.color = color

    def show(self, screen):
        pygame.draw.aaline(screen, self.color, self.pos.coordinates, ((self.dir.mult(20)).add(self.pos)).coordinates)
        
    def setDir(self, x, y):
        self.dir = (Vector2D(x, y) - self.pos).unit()

    def setAngle(self, angle):
        self.angle += angle

    def cast(self, wall:Boundary):
        x1 = wall.a.x
        y1 = wall.a.y
        x2 = wall.b.x
        y2 = wall.b.y

        x3 = self.pos.x
        y3 = self.pos.y
        x4 = self.pos.x + self.dir.x
        y4 = self.pos.y + self.dir.y
        
        den = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
        if den == 0:
            return
        else:
            t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4))/den
            u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3))/den

            if t > 0 and t < 1 and u > 0:
                pt = Vector2D((x1 + t * (x2 - x1)),(y1 + t * (y2 - y1)))
                return pt
            
            else:
                return None