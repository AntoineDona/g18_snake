
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

        for event in pygame.event.get():
    
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    exit = False
                    while not(exit):
                        police = pygame.font.SysFont('times new roman', 90)
                        game_over_surface = police.render(
                            'Pause', True, (255, 0, 0))  # decription
                        # on récupère les coordonées du rectancle game_over_surface
                        game_over_rect = game_over_surface.get_rect()
                        game_over_rect.midtop = (800/2, 600/4)  # positionnement
                        dis.fill(black)
                        dis.blit(game_over_surface, game_over_rect)  # affiche

                        police_message = pygame.font.SysFont('times', 20)
                        message_surface = police_message.render(
                            'Press P to resume or Press Q to quit game', True, (255, 0, 0))
                        message_rect = message_surface.get_rect()
                        message_rect.midtop = (800/2, 600/1.5)
                        dis.blit(message_surface, message_rect)

                        for event2 in pygame.event.get():
                            if event2.type == pygame.QUIT or (event2.type == pygame.KEYDOWN and event2.key == pygame.K_q):
                                pygame.quit()
                                quit()
                            if event2.type == pygame.KEYDOWN:
                                if event2.key == pygame.K_p:
                                    exit = True
                        pygame.display.flip()
                        time.sleep(1)

                if event.key == pygame.K_LEFT and direction != 'horizontal' and not already_changed:
                    dx = -20
                    dy = 0
                    direction='horizontal'
                    already_changed=True
                elif event.key == pygame.K_RIGHT and direction != 'horizontal' and not already_changed:
                    dx = 20
                    dy = 0
                    direction='horizontal'
                    already_changed=True
                elif event.key == pygame.K_UP and direction != 'vertical'and not already_changed:
                    dx = 0
                    dy = -20
                    direction='vertical'
                    already_changed=True
                elif event.key == pygame.K_DOWN and direction != 'vertical'and not already_changed:
                    dx = 0
                    dy = 20
                    direction='vertical'
                    already_changed=True
        already_changed=False

    def update_level(score, n=5):
    return floor(score/n)