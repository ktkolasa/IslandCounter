def is_newline(char: str) -> bool:
    """
    :param char:
    :return:
    """
    return ord(char) == 10


def validate_cell_value(value: int):
    """
    :param value:
    :raises: ValueError if cell is neither 0 nor 1
    """
    if not ord(value) in (48, 49):
        raise ValueError("Only 1 and 0 are valid chars in input file. Got ", value)


def is_island(value: str) -> bool:
    """
    :param value:
    :return:
    """
    return int(value) == 1


def validate_array(previous_line_len: int, line: str, row: int):
    """
    Check if two subsequent non-empty lines are of different length.
    If not, raise an exception.
    :param previous_line_len:
    :param line:
    :param row:
    :raises: ValueError if input file is not an array
    """
    if len(line) and len(line) != previous_line_len and is_newline(line[-1]):
        raise ValueError(
            f"Input file is not an array, line {row + 1} varies in length."
        )


def cell_neighbours_are_island(col: int, row: int, island: set) -> bool:
    """
    If cell to the left or cell above current cell
    are already a part of an island return True
    :param col:
    :param row:
    :param island:
    :return:
    """
    return not {(col - 1, row), (col, row - 1)}.isdisjoint(island)
