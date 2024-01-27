import pygame
import math
from imports.boundary import Boundary
from imports.particle import Particle, polygon


def lerp(A, B, t):
    return (1-t)*A + t*B
def ilerp(A, B, V):
    return (V-A)/(B-A)

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
W2 = screen.get_width()
W1 = W2//2
H1 = screen.get_height()

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
# shapes = []
# shapes.extend([polygon(20, math.sqrt(2)*(W1/8), rotation=math.pi/4, translation=(W1/2, H1/2)), polygon(10, 50, translation=(50+(W1-100)/4, 50+(H1-100)/4)), polygon(4, 50, translation=(3*W1/4, 60)), polygon(5, 50, translation=(3*W1/4, 3*H1/4)), polygon(6, 50, translation=(1*W1/4, 3*H1/4))])
# for shape in shapes:
#     for i in range(len(shape)):
#         walls.append(Boundary(shape[i][0], shape[i][1], shape[(i + 1)%len(shape)][0], shape[(i + 1)%len(shape)][1], (255, 0, 0), 5))
#         walls.extend([walltop, wallbottom, wallright, wallleft])


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

    mouse = pygame.mouse.get_pos()
    if mouse[0] < W1 and mouse[1] < H1:
        particle = Particle(mouse[0], mouse[1], (255, 255, 255, 0.3), heading)
        scene = particle.look(screen, walls)
        i = 0
        width = (W1//len(scene))
        for d in scene:
            dSq = d*d
            wSq = width*width
            brightness = lerp(1, 0, ilerp(0, 1.414*W1, dSq))
            print(brightness)
            height = lerp(H1/2.4, 0, ilerp(0, 1.414*W1, d))
            # print((brightness*color[0], brightness*color[1], brightness*color[2]))
            # print((color[0], color[1], color[2]))
            # pygame.draw.rect(screen, (brightness*color[0], brightness*color[1], brightness*color[2]), (W1 + i*width, H1/2 - height, width, 2*height))
            pygame.draw.rect(screen, (brightness%255, brightness%255, brightness%255), (W1 + i*width, H1/2 - height, width, 2*height))
            i += 1

        particle.show(screen)

    for wall in walls:
        wall.show(screen)

    pygame.display.update()
