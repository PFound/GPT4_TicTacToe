import pytest
from game import Game
from board import Board

@pytest.fixture
def game():
    return Game()

def test_game_is_draw(game):
    # Test an empty board (not a draw)
    game.board = Board()
    assert game.is_draw() == False

    # Test a board with a win (not a draw)
    game.board.grid = [
        ['X', 'O', 'X'],
        ['X', 'O', 'O'],
        ['O', 'O', 'X']  # Change this line to have a win
    ]
    assert game.is_draw() == False

    # Test a full board with no win (a draw)
    game.board.grid = [
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        ['X', 'X', 'O']
    ]
    assert game.is_draw() == True
