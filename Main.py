import pygame
from pygame.locals import *
from copy import copy

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
violet = (127, 0, 255)

largeur=800
hauteur=600

dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Notre jeu Snake')

game_over = False

l = [[300, 300], [290, 300], [280, 300]]

x1_change = 0
y1_change = 0

n = 3  # taille du serpent

clock = pygame.time.Clock()

border=True

def critere_bodure(x,y):
    if border :
        if x>=largeur or x<=0 or y>=hauteur or y<=0:
            print (x,y)
            game_over = True
    if not border:
        if x>=largeur or x<=0 or y>=hauteur or y<=0:
            x=x%largeur
            y=y%hauteur

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
    n=len(l)
    for k in range(0, n-1):
        l[n-1-k] = copy(l[n-2-k])
    l[0][0] += x1_change
    l[0][1] += y1_change
    dis.fill(black)
    for x in l:
        pygame.draw.rect(dis, violet, [x[0], x[1], 10, 10])
    critere_bodure(l[0][0],l[0][1])
    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()