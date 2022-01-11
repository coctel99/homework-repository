"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from itertools import chain
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    """
    Checks who won in the tic tac toe game
    :param board: Game board 3x3
    :return: "x wins!" when 3 "x" in one line, "o wins!" when
    3 "o" in one line, "draw!" when
    """
    rows = [row for row in board]
    cols = [col for col in zip(*board)]
    main_diag = [[board[i][i] for i in range(len(board))]]
    anti_diag = [[board[i][-i - 1] for i in range(len(board))]]
    lines = list(chain(rows, cols, main_diag, anti_diag))
    board_string = [char for row in board for char in row]

    for line in lines:
        if len(set(line)) == 1 and line[0] != "-":
            return f"{line[0]} wins!"
    if "-" in board_string:
        return "unfinished!"
    return "draw!"
