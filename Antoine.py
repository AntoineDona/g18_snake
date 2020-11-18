import pygame
pygame.init()
dis=pygame.display.set_mode((400,300))
 
pygame.display.set_caption('Snake game by Edureka')
 
blue=(0,0,255)
red=(255,0,0)
 
game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
    pygame.draw.rect(dis,blue,[0,0,20,20])
    pygame.display.update()
pygame.quit()
quit()

direction = 'null'

if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != 'horizontal':
                dx = -20
                dy = 0
                direction='horizontal'
            elif event.key == pygame.K_RIGHT and direction != 'horizontal':
                dx = 20
                dy = 0
                direction='horizontal'
            elif event.key == pygame.K_UP and direction != 'vertical':
                dx = 0
                dy = -20
                direction='vertical'
            elif event.key == pygame.K_DOWN and direction != 'vertical':
                dx = 0
                dy = 20
                direction='vertical'
