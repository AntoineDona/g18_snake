#######################
# Tests des           #
# fonctions           #
#######################

from pytest_mock import*
from pytest import*
from fonctions_affichage import*
from fonctions_pomme import * 
from fonctions_avance import*


snake_init = [[300, 300], [280, 300], [260, 300]]

# -------------------- TESTS DES FONCTIONS D'AFFICHAGE ----------------------------------------------------

def test_new_snake(): 
    snake = newsnake([[300, 300], [280, 300], [260, 300]],3,0,-20)
    assert snake == [[300, 280], [300, 300], [280, 300]]

def test_update_level():
    level, levelup = update_level(99,8)
    assert level == 9
    assert levelup 

#--------------------- TESTS DES FONCTIONS POMMES ----------------------------------------------------------

def test_proba_pomme_jaune():
    pomme_jaune = proba_pomme_jaune([0,0,False],10)
    assert pomme_jaune[0] <= 800 and pomme_jaune[1] <= 600
    assert pomme_jaune[2] or not pomme_jaune[2]

def test_pomme_jaune():
    score, pomme, tps = pomme_jaune(snake_init,10,[300,300,True],0)
    assert score == 20
    assert pomme[2] == False
    assert tps == 0

def test_ralentissement():
    pass

def test_proba_pomme_blanche():
    pomme_blanche = proba_pomme_blanche([0,0,False],10)
    assert pomme_blanche[0] <= 800 and pomme_blanche[1] <= 600
    assert pomme_blanche[2] or not pomme_blanche[2]

def test_pomme_blanche():
    score, pomme, tps = pomme_blanche(snake_init,10,[300,300,True],[])
    assert score == 20
    assert pomme[2] == False
    assert tps == [0]

def test_acceleration():
    tps , freq  = acceleration([0,1,3,0],15)
    assert tps == [0,2,4,2]
    assert freq == 25

def test_collision_pomme():
    score, pomme, snake, queue = collision_pomme(10,[300,300],snake_init,[260,300])
    assert score == 11
    assert queue == [260,300]
    assert pomme[0] <= 800 and pomme[1] <= 600

def test_collision_pomme_rose():
    snake, score = collision_pomme_rose(snake_init,11,[300,300,True],[260,300])
    assert score == 14

def test_pomme_turquoise():
    score, snake, pomme = pomme_turquoise(10,snake_init,[0,0,False])
    assert score == 10
    assert pomme[2] or not pomme[2]
    assert pomme[0] <= 800 and pomme[1] <= 600

def test_collision_pomme_turquoise():
    score, pomme, tps, border = coll_pomme_turquoise(12,snake_init,[300,300,True],1,True)
    assert score == 13
    assert pomme[2] == False 
    assert border == False
    assert tps == 0

def test_temps_border():
    tps, border = temps_border(0,False,10)
    assert not border 
    tps, border = temps_border(12,False,1)
    assert tps == -1
    assert border

def test_pomme_coupe2():
    pomme = pomme_coupe2(12,[0,0,False],snake_init)
    assert pomme[2] or not pomme[2]
    assert pomme[0] <= 800 and pomme[1] <= 600

def test_coll_pomme_coupe():
    snake, score, pomme = coll_pomme_coupe([[300,300],[280,300],[260,300],[240,300],[220,300],[200,300]],12,[300,300,True])
    assert score == 13
    assert not pomme[2]
    assert len(snake) ==3 
    assert snake == [[300,300],[280,300],[260,300]]

# -------------------------------------- TESTS COLLISIONS ------------------------------------------------

def test_detection_collision_bordure():
    snake, game_over,collision_mur = detection_collision_bordure([[0,0],[10,0],[20,0]],True,False,True)
    assert game_over == True
    assert collision_mur
    snake, game_over,collision_mur = detection_collision_bordure([[-10,0],[0,0],[10,0]],False,False,False)
    assert not game_over
    assert snake == [[760,560],[0,0],[10,0]]

def test_detection_auto_collision():
    game_over = detection_auto_collision([[300,300],[280,300],[260,300],[300,300]],True,False,4)
    assert game_over
    game_over_False = detection_auto_collision(snake_init,True,False,3)
    assert game_over