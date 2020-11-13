def snake_avance(snake,direction):
    """
    prend en entrée un liste de liste (serpent) et une direction (tuple ex: (0,1) pour aller à droite )
    retourne le serpent avancé de 1
    """
    snake=[snake[0]+direction]+snake[1:]
