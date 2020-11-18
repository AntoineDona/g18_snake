
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
