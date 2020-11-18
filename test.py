
#######################
# Tests des           #
# fonctions             #
# les inputs du       #
# joueur              #
#######################
from Main.py import*
from pytest_mock import*
from pytest import*


def mock_input_return_direction(obj):
    return 'b'

def test_read_player_command(monkeypatch):
    import textual_2048 
    monkeypatch.setattr('builtins.input', mock_input_return )
    assert textual_2048.read_player_command() == 'b'    



def test_aller_à_droite():
