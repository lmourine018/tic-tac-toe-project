"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # raise NotImplementedError
    # Count number of X's and O's on the board
    count_X = sum(row.count(X) for row in board)
    count_O = sum(row.count(O) for row in board)

    # If X has made fewer moves than O, it's X's turn
    if count_X <= count_O:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] != EMPTY:
        raise Exception("Invalid action")

    player_turn = player(board)
    new_board = [row[:] for row in board]  # Deep copy of the board
    new_board[i][j] = player_turn
    return new_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if all(cell == X for cell in row):
            return X
        elif all(cell == O for cell in row):
            return O

    # Check columns
    for j in range(3):
        if all(board[i][j] == X for i in range(3)):
            return X
        elif all(board[i][j] == O for i in range(3)):
            return O

    # Check diagonals
    if all(board[i][i] == X for i in range(3)):
        return X
    elif all(board[i][i] == O for i in range(3)):
        return O
    if all(board[i][2 - i] == X for i in range(3)):
        return X
    elif all(board[i][2 - i] == O for i in range(3)):
        return O

    return None
    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    return winner(board) is not None or all(all(cell is not None for cell in row) for row in board)



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    if result == X:
        return 1
    elif result == O:
        return -1
    else:
        return 0




def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        # Maximize for X
        value = -math.inf
        best_action = None
        for action in actions(board):
            min_value = min_value_of_minimax(result(board, action))
            if min_value > value:
                value = min_value
                best_action = action
    else:
        # Minimize for O
        value = math.inf
        best_action = None
        for action in actions(board):
            max_value = max_value_of_minimax(result(board, action))
            if max_value < value:
                value = max_value
                best_action = action

    return best_action



def max_value_of_minimax(board):
    if terminal(board):
        return utility(board)

    value = -math.inf
    for action in actions(board):
        value = max(value, min_value_of_minimax(result(board, action)))
    return value


def min_value_of_minimax(board):
    if terminal(board):
        return utility(board)

    value = math.inf
    for action in actions(board):
        value = min(value, max_value_of_minimax(result(board, action)))
    return value
