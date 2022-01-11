from homework7.task3 import tic_tac_toe_checker

x_win_board = [["-", "-", "o"],
               ["-", "-", "o"],
               ["x", "x", "x"]]


o_win_diagonal_board = [["o", "-", "-"],
                        ["-", "o", "x"],
                        ["x", "x", "o"]]

unfinished_board = [["-", "-", "o"],
                    ["-", "x", "o"],
                    ["x", "o", "-"]]

draw_board = [["o", "x", "o"],
              ["x", "x", "o"],
              ["x", "o", "x"]]


def test_x_win():
    """Testing that 3 'x' in a row give 'x wins!' message."""
    assert tic_tac_toe_checker(x_win_board) == "x wins!"


def test_o_win_diagonal():
    """Testing that 3 'o' in a diagonal give 'o wins!' message."""
    assert tic_tac_toe_checker(o_win_diagonal_board) == "o wins!"


def test_unfinished():
    """Testing that with no winner and having '-' on board give
    'unfinished!' message."""
    assert tic_tac_toe_checker(unfinished_board) == "unfinished!"


def test_draw():
    """Testing that with no winners and no '-' on board give 'draw' message."""
    assert tic_tac_toe_checker(draw_board) == "draw!"
