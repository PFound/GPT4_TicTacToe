import pytest
from board import Board

def test_board_initialization():
    board = Board()
    expected_grid = [['', '', ''], ['', '', ''], ['', '', '']]
    assert board.grid == expected_grid

def test_board_check_win():
    board = Board()

    # Test winning rows
    for row in range(3):
        board.grid[row] = ['X', 'X', 'X']
        assert board.check_win('X') == True
        board.grid[row] = ['', '', '']

    # Test winning columns
    for col in range(3):
        board.grid[0][col] = 'O'
        board.grid[1][col] = 'O'
        board.grid[2][col] = 'O'
        assert board.check_win('O') == True
        board.grid[0][col] = ''
        board.grid[1][col] = ''
        board.grid[2][col] = ''

    # Test winning diagonals
    board.grid[0][0] = 'X'
    board.grid[1][1] = 'X'
    board.grid[2][2] = 'X'
    assert board.check_win('X') == True

    board.grid[0][0] = ''
    board.grid[1][1] = ''
    board.grid[2][2] = ''

    board.grid[0][2] = 'O'
    board.grid[1][1] = 'O'
    board.grid[2][0] = 'O'
    assert board.check_win('O') == True
