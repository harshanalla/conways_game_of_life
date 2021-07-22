import pytest


@pytest.fixture(scope='session')
def game():
    from game.handler import Game
    class Temp:
        def __init__(self):
            self.refresh_rate = 1000
            self.size = 30
            self.spawn_rate = 100
            self.show_coordinates = True
            self.clear_terminal = True

    game = Game(Temp())
    return game


def test_check_against_rules_rule_1_pass(game):
    live_neighbors = 1
    alive = 1
    actual = game.check_against_rules(live_neighbors, alive)
    expected = 0
    assert actual == expected


def test_check_against_rules_rule_1_pass_2(game):
    live_neighbors = 0
    alive = 1
    actual = game.check_against_rules(live_neighbors, alive)
    expected = 0
    assert actual == expected

@pytest.mark.parametrize("test_input, expected", [((2, 1), 1), ((3, 1), 1), ((4, 1), 0), ((1, 1), 0)])
def test_check_against_rules_rule_2_pass(game, test_input, expected):
    actual = game.check_against_rules(test_input[0], test_input[1])
    assert actual == expected


@pytest.mark.parametrize("test_input, expected", [((4, 1), 0), ((5, 1), 0), ((6, 1), 0), ((7, 1), 0), ((8, 1), 0)])
def test_check_against_rules_rule_3_iterate(game, test_input, expected):
    actual = game.check_against_rules(test_input[0], test_input[1])
    assert actual == expected

def test_check_against_rules_rule_4_pass(game):
    live_neighbors = 3
    alive = 0
    actual = game.check_against_rules(live_neighbors, alive)
    expected = 1
    assert actual == expected


def test_board_alive_all_zeros(game):
    game.board = [[0 for _ in range(game.size)] for _ in range(game.size)]
    assert not game.board_alive()

def test_board_alive_all_ones(game):
    game.board = [[1 for _ in range(game.size)] for _ in range(game.size)]
    assert game.board_alive()

def test_board_alive_mix(game):
    game.board = [[1,1,1],
                  [1,1,1],
                  [1,1,1]]
    assert game.board_alive()