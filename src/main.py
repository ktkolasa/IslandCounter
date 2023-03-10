import os
import sys


def is_newline_char(char):
    return ord(char) == 10


def do_array_check(previous_line_len, line, row):
    """Check if two subsequent non-empty lines are of different length.
    If not, raise an exception."""
    if len(line) and len(line) != previous_line_len and is_newline_char(line[-1]):
        raise ValueError(
            f"Input file is not an array, line {row + 1} varies in length."
        )


def count_islands(user_input):
    """Return number of groups of 'islands' (groups of 1) among '0's"""
    if not os.path.isfile(user_input):
        raise FileNotFoundError(f"{user_input} is not a file.")

    islands, previous_line_len = [], 0
    with open(user_input, "r", encoding="utf-8") as input_file:
        for row, line in enumerate(input_file):
            if not previous_line_len:
                previous_line_len = len(line)
            do_array_check(previous_line_len, line, row)

            for col, cell_value in enumerate(line):
                if is_newline_char(cell_value):
                    break
                if ord(cell_value) not in (48, 49):
                    raise ValueError(
                        "Only 1 and 0 are valid chars in input file. Got ", cell_value
                    )

                if int(cell_value) == 1:
                    adjacent_island = {}
                    if not islands:
                        islands.append({(col, row)})
                        continue
                    for island in islands:
                        # if cell to the left or cell above current cell
                        # are already a part of an island, add curr cell to that island
                        if not {(col - 1, row), (col, row - 1)}.isdisjoint(island):
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
            count_islands(sys.argv[1])
        except FileNotFoundError as fnf:
            print(fnf, file=sys.stderr)
        except ValueError as ve:
            print(ve, file=sys.stderr)
