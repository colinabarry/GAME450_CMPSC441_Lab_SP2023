"""
Extra Credit Task-

Tic tac toe input
Here's the backstory for this challenge: imagine you're writing a tic-tac-toe game, where the board looks like this:

1:  X | O | X
   -----------
2:    |   |  
   -----------
3:  O |   |
    A   B   C
The board is represented as a 2D list:

board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    ["O", " ", " "],
]
Imagine if your user enters "C1" and you need to see if there's an X or O in that cell on the board. To do so, you need to translate from the string "C1" to row 0 and column 2 so that you can check board[row][column].

Your task is to write a function that can translate from strings of length 2 to a tuple (row, column). Name your function get_row_col; it should take a single parameter which is a string of length 2 consisting of an uppercase letter and a digit.

For example, calling get_row_col("A3") should return the tuple (2, 0) because A3 corresponds to the row at index 2 and column at index 0in the board.
"""

from typing import List, Tuple


def get_row_col(cell: str) -> Tuple[int, int]:

    valid_chars: List[str] = ["A", "B", "C"]
    valid_digits: List[str] = ["1", "2", "3"]

    if cell.__len__() != 2:
        raise Exception(
            "invalid input -> cell must be 2 characters consisting of a letter and a digit"
        )

    if not cell[0] in valid_chars:
        raise Exception("invalid input -> first char must be one of: ['A', 'B', 'C']")

    if not cell[1] in valid_digits:
        raise Exception("invalid input -> second char must be one of: ['1', '2', '3']")

    return (
        valid_digits.index(cell[1]),
        valid_chars.index(cell[0]),
    )
