import pytest

from src.modules.tic_tac_toe import tic_tac_toe


def test_set_move():
    """test position overlap"""
    position = 1
    player = 1
    board = [
        ["X", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    with pytest.raises(ValueError):
        tic_tac_toe.set_move(board, position, player)


def test_free_slots():
    """retrieve free slots in the board"""

    board = [
        ["X", " ", " "],
        [" ", "X", "O"],
        ["X", "O", " "]
    ]

    assert [1, 2, 3, 8] == tic_tac_toe.free_slots(board)
    assert [4, 2, 5, 8] != tic_tac_toe.free_slots(board)


def test_check_win_diagonal():
    """docstring for test_check"""

    # principal diagonal
    board = [
        ["X", " ", " "],
        [" ", "X", "O"],
        ["X", "O", "X"]
    ]

    assert True == tic_tac_toe.check_win(board)

    # leading diagonal
    board = [
        ["X", " ", "X"],
        [" ", "X", "O"],
        ["X", "O", "O"]
    ]

    assert True == tic_tac_toe.check_win(board)


def test_check_win_columns():
    """docstring for test_check"""

    # column one
    board = [
        ["X", " ", " "],
        ["X", "X", "O"],
        ["X", "O", "X"]
    ]

    assert True == tic_tac_toe.check_win(board)

    # column two
    board = [
        ["X", "O", "X"],
        [" ", "O", "O"],
        ["X", "O", "O"]
    ]

    assert True == tic_tac_toe.check_win(board)

    # column three
    board = [
        ["X", "X", "O"],
        [" ", "O", "O"],
        ["X", "O", "O"]
    ]

    assert True == tic_tac_toe.check_win(board)


def test_check_win_rows():
    """docstring for test_check"""

    # row one
    board = [
        ["X", "X", "X"],
        ["O", " ", " "],
        ["O", "O", "X"]
    ]

    assert True == tic_tac_toe.check_win(board)

    # row two
    board = [
        ["O", " ", " "],
        ["X", "X", "X"],
        ["O", "O", "X"]
    ]

    assert True == tic_tac_toe.check_win(board)

    # row three
    board = [
        ["O", " ", " "],
        ["O", "O", "X"],
        ["X", "X", "X"]
    ]

    assert True == tic_tac_toe.check_win(board)


def test_machine_move():
    """test machine moviment"""

    board = [
        ["O", "O", " "],
        ["O", "O", "X"],
        ["X", "X", "X"]
    ]

    free_slot = tic_tac_toe.free_slots(board)

    # transform real position to array index - sub -1
    real_machine_position = tic_tac_toe.machine_move(board)
    machine_position = (real_machine_position - 1)

    assert free_slot[0] == machine_position 
