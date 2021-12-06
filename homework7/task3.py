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
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    """
    Checks who won in the tic tac toe game
    :param board: Game board 3x3
    :return: "x wins!" when 3 "x" in one line, "o wins!" when
    3 "o" in one line, "draw!" when
    """
    diagonal = []
    antidiaginal = []

    # check horizontal lines
    for idx, row in enumerate(board):
        diagonal.append(row[idx])
        antidiaginal.append(row[-idx - 1])
        if all([row[i] == "x" for i in range(len(row))]):
            return "x wins!"
        if all([row[i] == "o" for i in range(len(row))]):
            return "o wins!"

    # check vertical lines
    for col in zip(*board):
        if all([col[i] == "x" for i in range(len(col))]):
            return "x wins!"
        if all([col[i] == "o" for i in range(len(col))]):
            return "o wins!"

    # check main diagonal lines
    if all([diagonal[i] == "x" for i in range(len(diagonal))]):
        return "x wins!"
    if all([diagonal[i] == "o" for i in range(len(diagonal))]):
        return "o wins!"

    # check antidiagonal lines
    if all([antidiaginal[i] == "x" for i in range(len(antidiaginal))]):
        return "x wins!"
    if all([antidiaginal[i] == "o" for i in range(len(antidiaginal))]):
        return "o wins!"

    # check unfinished
    if any("-" in row for row in board):
        return "unfinished!"
    return "draw!"
