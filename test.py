
#######################
# Tests des           #
# fonctions           #
#######################

from pytest_mock import*
from pytest import*
from fonctions_affichage import*
from fonctions_pomme import * 

snake_init = [[300, 300], [280, 300], [260, 300]]

def test_new_snake(): 
    snake = newsnake([[300, 300], [280, 300], [260, 300]],3,0,-20)
    assert snake == [[300, 280], [300, 300], [280, 300]]

def test_update_level():
    level = update_level(100,10)
    assert level == 10

def test_proba_pomme_jaune():
    pomme_jaune = proba_pomme_jaune([0,0,False])
    assert pomme_jaune[0] <= 800 and pomme_jaune[1] <= 600
    assert pomme_jaune[2] or not pomme_jaune[2]

def test_pomme_jaune():
    score, pomme, tps = pomme_jaune(snake_init,10,[300,300,True],[])
    assert score == 20
    assert pomme[2] == False
    assert tps == [0]

def test_ralentissement():
    pass


def test_proba_pomme_blanche():
    pomme_blanche = proba_pomme_blanche([0,0,False])
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
    assert freq == 30

def test_pomme_verte():
    pass    

def test_collision_pomme():
    score, pomme, snake, queue = collision_pomme(10,[300,300],snake_init,snake_init[-1])
    assert score == 11
    assert snake == [[300, 300], [280, 300], [260, 300], [260, 300]]
    assert queue == [260,300]
    assert pomme[0] <= 800 and pomme[1] <= 600
