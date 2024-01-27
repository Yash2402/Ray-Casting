import pygame
import math
from imports.boundary import Boundary
from imports.particle import Particle, polygon


def lerp(A, B, t):
    return (1-t)*A + t*B
def ilerp(A, B, V):
    print((V-A)/(B-A))
    return (V-A)/(B-A)

pygame.init()
W2 = 1200
W1 = 600
H1 = 600
screen = pygame.display.set_mode((W2, H1), pygame.RESIZABLE)


walls = []
scene = []
heading = -70
cellW = 20
cellH = 20

walltop = Boundary(0, 0, W1, 0, (255, 255, 255), 5)
wallright = Boundary(W1, 0, W1, H1, (255, 255, 255), 5)
wallleft = Boundary(0, 0, 0, H1, (255, 255, 255), 5)
wallbottom = Boundary(0, H1, W1, H1, (255, 255, 255), 5)
walls.extend([walltop, wallbottom, wallright, wallleft])
shapes = []
shapes.extend([polygon(3, 50, translation=(50+(W1-100)/4, 50+(H1-100)/4)), polygon(4, 50, translation=(3*W1/4, 60)), polygon(5, 50, translation=(3*W1/4, 3*H1/4)), polygon(6, 50, translation=(1*W1/4, 3*H1/4))])
for shape in shapes:
    for i in range(len(shape)):
        walls.append(Boundary(shape[i][0], shape[i][1], shape[(i + 1)%len(shape)][0], shape[(i + 1)%len(shape)][1], (255, 0, 0), 5))



run = True
while run:
    screen.fill((0, 0, 0))
    particle = Particle(300, 300, (255, 255, 255, 10), heading)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        heading -= 1
    if keys[pygame.K_d]:
        heading += 1
    if keys[pygame.K_UP]:
        fov = particle.FOV
        fov += 10
        particle.updateFOV(fov)
    if keys[pygame.K_DOWN]:
        fov = particle.FOV
        fov -= 10
        particle.updateFOV(fov)

    mouse = pygame.mouse.get_pos()
    if mouse[0] < W1 and mouse[1] < H1:
        particle = Particle(mouse[0], mouse[1], (255, 255, 255, 0.3), heading)
        scene = particle.look(screen, walls)
        i = 0
        width = (W1/len(scene))

        for d in scene:
            brightness = lerp(255, 0, ilerp(0, 1.414*W1, d))
            height = lerp(H1/2.4, 0, ilerp(0, 1.414*W1, d))
            pygame.draw.rect(screen, (brightness%255, brightness%255, brightness%255), (W1 + i*width, H1/2 - height, width, 2*height))
            i += 1

        particle.show(screen)

    for wall in walls:
        wall.show(screen)

    pygame.display.update()
