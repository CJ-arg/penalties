from project import get_turn, get_goal, get_player, get_player_vs

def test_get_turn():
    assert get_turn(True) == False
    assert get_turn(False) == True


def test_get_goal():
    goal = get_goal()
    assert goal.x  == 120
    assert goal.y  == 100



def test_get_player():
    player = get_player()
    assert player.x  == 400
    assert player.y  == 250


def test_get_player_vs():
    playervs = get_player_vs()
    assert playervs.x  == 400
    assert playervs.y  == 250
