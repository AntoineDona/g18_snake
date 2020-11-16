<<<<<<< HEAD
from pygame import * 
=======
import pygame
import time
import copy

pygame.init()

largeur = 800
hauteur = 500
l = 10

dis = pygame.display.set_mode((largeur, hauteur))
pygame.display.update()
pygame.display.set_caption('Snake Game')
gameover = False

white = (255, 255, 255)
black = (0, 0, 0)
clock = pygame.time.Clock()

x0 = 300
y0 = 300
x1 = 310
y1 = 300
x2 = 320
y2 = 300

dx1 = 0
dy1 = 0
snake = [[x0, y0], [x1, y1], [x2, y2]]
mangefruit = False


while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -10
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = 10
                dy = 0
            elif event.key == pygame.K_UP:
                dy = -10
                dx = 0
            elif event.key == pygame.K_DOWN:
                dy = 10
                dx = 0
    x_new += dx
    y_new += dy

    dis.fill(black)

    pygame.draw.rect(dis, white, [snake[0][0], snake[0][1], 10, 10])

    pygame.display.update()
    clock.tick(30)
pygame.quit()
quit()
>>>>>>> 608443a807a79b429aabc6ea785fcdb64403f92e
