
#######################
# Tests des           #
# fonctions           #
#######################

from Main.py import*
from pytest_mock import*
from pytest import*


def mock_input_return_direction(obj):
    return {'event.type' : 'pygame.KEYDOWN', 'event.key' :' pygame.K_LEFT'}

def test_read_player_command(monkeypatch):
    import Main.py
    monkeypatch.setattr('event', mock_input_return_direction )
    assert Main.py.moves(0,0,True) == (-20,0,False)    



