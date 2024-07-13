from math import ceil, floor
import pygame
import random

from imports.boundary import Boundary
from imports.particle import Particle, polygon


def lerp(A, B, t): return (1 - t) * A + t * B


def ilerp(A, B, V): return (V - A) / (B - A)


pygame.init()

W2 = 1200
W1 = 600
H1 = 600
screen = pygame.display.set_mode((W2, H1), pygame.RESIZABLE, vsync=1)
pygame.display.set_caption("Ray Casting")

walls = []
scene = []
heading = 0
cellW = 20
cellH = 20
FOV = 50

boundaryColor = (245, 243, 187)
walltop = Boundary(0, 0, W1, 0, boundaryColor, 5)
wallright = Boundary(W1, 0, W1, H1, boundaryColor, 5)
wallleft = Boundary(0, 0, 0, H1, boundaryColor, 5)
wallbottom = Boundary(0, H1, W1, H1, boundaryColor, 5)
walls.extend([walltop, wallbottom, wallright, wallleft])

shapes = []
shapes.extend(
    [
        polygon(3, 50, translation=(50 + (W1 - 100) / 4, 50 + (H1 - 100) / 4)),
        polygon(4, 50, translation=(3 * W1 / 4, 60)),
        polygon(5, 50, translation=(3 * W1 / 4, 3 * H1 / 4)),
        polygon(6, 50, translation=(1 * W1 / 4, 3 * H1 / 4)),
    ]
)
for shape in shapes:
    for i in range(len(shape)):
        walls.append(
            Boundary(
                shape[i][0],
                shape[i][1],
                shape[(i + 1) % len(shape)][0],
                shape[(i + 1) % len(shape)][1],
                [(223, 41, 53), (0, 124, 200), (180, 140, 20)][i % 3],
                5,
            )
        )

clock = pygame.time.Clock()
run = True

while run:
    clock.tick(120)
    screen.fill((65, 39, 34))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.rect(screen, (0, 191, 255), (W1, 0, W1, H1//2))
    pygame.draw.rect(screen, (0, 191, 255), (W1, 0, W1, H1), 1)
    mouse = pygame.mouse.get_pos()
    particle = Particle(mouse[0], mouse[1], (255, 255, 255, 3), heading, FOV)
    if mouse[0] < W1 and mouse[1] < H1:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            heading -= 1
        if keys[pygame.K_d]:
            heading += 1
        if keys[pygame.K_UP] and FOV < 360:
            FOV += 5
        if keys[pygame.K_DOWN] and FOV > 5:
            FOV -= 5

        particle.shootRays()
        scene, colors = particle.look(screen, walls)
        i = 0
        width = round(W1 / len(scene))

        for i in range(len(scene)):
            d = scene[i]
            color = colors[i]
            brightness = lerp(1, 0, ilerp(0, 1.414 * W1, d))
            height = lerp(H1 / 2.4, 0, ilerp(0, 1.414 * W1, d))
            pygame.draw.rect(screen, (255, 255, 255), (W1 + W2, 0, W2, H1))
            pygame.draw.rect(
                screen,
                (brightness*color[0], brightness *
                 color[1], brightness*color[2]),
                (W1 + i * width, H1 / 2 - height, width, 2 * height),
            )
            i += 1
        particle.show(screen)

    for wall in walls:
        wall.show(screen)

    pygame.display.update()
