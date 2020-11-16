import pygame
from pygame.locals import *
from copy import copy

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
violet = (127, 0, 255)

dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake Game by Edureka')

game_over = False

l = [[300, 300], [290, 300], [280, 300]]


x1_change = 0
y1_change = 0

n = 3  # taille du serpent

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
    for k in range(0, n-1):
        l[n-1-k] = copy(l[n-2-k])
    l[0][0] += x1_change
    l[0][1] += y1_change
    dis.fill(black)
    print(l)
    for x in l:
        pygame.draw.rect(dis, violet, [x[0], x[1], 10, 10])
    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()
