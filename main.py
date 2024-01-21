import pygame
import random
from imports.boundary import Boundary
from imports.particle import Particle


def lerp(A, B, t):
    return (1-t)*A + t*B
def ilerp(A, B, V):
    return (V-A)/(B-A)

pygame.init()
W2 = 1200
W1 = 600
H1 = 600

screen = pygame.display.set_mode((W2, H1))

walls = []
scene = []
heading = -70
cellW = 20
cellH = 20

for i in range(5):
    x1 = random.randint(0, W1)
    x2 = random.randint(0, W1)
    y1 = random.randint(0, H1)
    y2 = random.randint(0, H1)
    walls.append(Boundary(x1, y1, x2, y2, 5))
walltop = Boundary(0, 0, W1, 0, 5)
wallright = Boundary(W1, 0, W1, H1, 5)
wallleft = Boundary(0, 0, 0, H1, 5)
wallbottom = Boundary(0, H1, W1, H1, 5)
walls.append(walltop)
walls.append(wallright)
walls.append(wallleft)
walls.append(wallbottom)


run = True
while run:
    
    screen.fill((0, 0, 0))
    particle = Particle(300, 300, (255, 255, 255, 10), heading)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_a]:
        heading -= 1
    if keys[pygame.K_d]:
        heading += 1
    mouse = pygame.mouse.get_pos()
    if mouse[0] < W1:
        particle = Particle(mouse[0], mouse[1], (255, 255, 255, 100), heading)
        scene = particle.look(screen, walls) 
        i = 0
        w = (W1/len(scene))
        for d in scene:
            b = lerp(255, 0, ilerp(0, 1.414*W1, d))
            h = lerp(H1/2, 0, ilerp(0, 1.414*W1, d))
            pygame.draw.rect(screen, (b%255, b%255, b%255), (W1 + i*w, H1/2 - h, w, 2*h))
            i += 1
        particle.show(screen)
    for wall in walls:
        wall.show(screen)

    pygame.display.update()

