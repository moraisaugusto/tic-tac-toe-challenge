import math
import random

HUMAN = "X"
MACHINE = "O"
PINS = [HUMAN, MACHINE]


def set_move(board, position, player):
    """define player's moviment
    Args:
        board (dict): game board
        position (int): player position
        player (str): player that will execute the moviment
    Results:
        Board updated
    """
    row = math.ceil(position/3)
    col = position % 3 if position % 3 else 3

    # fix position according array indexes
    # array starts at 0 not 1
    row -= 1
    col -= 1
    if board[row][col] != " ":
        raise ValueError("This position is already used.")
    board[row][col] = PINS[int(player)]

    return board


def print_board(board):
    """print board - just for log

    Args:
        board (dict): game board
    Results:
        None
    """
    i = 0
    n = len(board)
    for line in board:
        for col in line:
            sep = "" if (i % n) == (n - 1) else "|"
            print(f" {col} ", end=sep)
            i += 1
        print("\n-----------")
    print("")


def free_slots(board):
    """return all free slots in the board

    Args:
        board (dict): game board
    Results:
        list of empty slots
    """
    empty_slots = []
    j = 0
    for i in range(len(board)):
        empty_in_row = [
            (i+j) for i, value in enumerate(board[i]) if value == " "
        ]
        empty_slots.extend(empty_in_row)
        j += 3
    return empty_slots


def machine_move(board):
    """machine moviment

    Args:
        board (dict): game board
    Results:
        machine position (int)
    """
    empty_slots = free_slots(board)
    position = random.choices(empty_slots)[0]
    return position + 1


def check_win(board):
    """Check winner

    Args:
        board (dict): game board

    Return
        True if there is a winner, otherwise, False
    """
    # just transpose the board to check cols
    board_transposed = [list(i) for i in zip(*board)]

    # check diagonals (principal and leading)
    diagonals = [
        [board[0][0], board[1][1], board[2][2]],  # principal
        [board[0][2], board[1][1], board[2][0]],  # leading
    ]

    for player in [HUMAN, MACHINE]:
        # check rows
        if [player, player, player] in board:
            return True

        # check cols
        if [player, player, player] in board_transposed:
            return True

        # check diagonals
        if [player, player, player] in diagonals:
            return True

    return False


def update_game(board, position, player, has_machine_player=None):
    """Update game
    Function very similar to set_move but,
    I prefered to keep it separated.

    Args:
        board (dict): board game
        position (int): player position
        player (str): player to execute the moviment
    Results
        return board
    """
    board = set_move(board, position, player)
    print_board(board)

    return board
