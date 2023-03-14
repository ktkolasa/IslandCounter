import os
import sys
from cell_validation import is_island, is_newline, cell_neighbours_are_island,\
    validate_array, validate_cell_value


def validate_file(user_input: str) -> bool:
    """
    :param user_input:
    :return:
    """
    if not os.path.isfile(user_input):
        raise FileNotFoundError(f"{user_input} is not a file.")
    if not user_input.endswith(".txt"):
        raise UserWarning(f"{user_input} is not a .txt file.")
    return True


def count_islands(user_input: str) -> int:
    """Return number of groups of 'islands' (groups of 1) among '0's"""
    islands, previous_line_len = [], 0
    with open(user_input, "r", encoding="utf-8") as input_file:
        for row, line in enumerate(input_file):
            if not previous_line_len:
                previous_line_len = len(line)
            validate_array(previous_line_len, line, row)
            for col, cell_value in enumerate(line):
                if is_newline(cell_value):
                    break
                validate_cell_value(cell_value)
                if is_island(cell_value):
                    adjacent_island = set()
                    if not islands:
                        islands.append({(col, row)})
                        continue
                    for island in islands:
                        if cell_neighbours_are_island(col, row, island):
                            island.add((col, row))
                            # if this there is already an adjacent island, merge them
                            if adjacent_island:
                                adjacent_island.union(island)
                                islands.remove(island)
                                # for the first island containing the cell, save the information
                            else:
                                adjacent_island = island
                    if not adjacent_island:
                        islands.append({(col, row)})
        print(len(islands))
        return len(islands)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "No arguments supplied. Please pass path to the input text file.",
        )
    else:
        try:
            validate_file(sys.argv[1])
            count_islands(sys.argv[1])
        except (FileNotFoundError, ValueError, UserWarning) as e:
            print(e, file=sys.stderr)
