import sys


def count_islands(input_file):
    # todo file validation
    islands = []
    with open(input_file, "r") as input_file:
        for row, line in enumerate(input_file):
            for col, piece in enumerate(line):
                if ord(piece) == 10:
                    break
                if int(piece) not in (0, 1):
                    print("Only 1 and 0 are valid chars in input file. Got ", piece)
                    # todo handle this case
                    return -1
                elif eval(piece) == 1:
                    added_to = {}
                    if not islands:
                        islands.append({(col, row)})
                        continue
                    for island in islands:
                        if not {(col - 1, row), (col, row - 1)}.isdisjoint(island):
                            island.add((col, row))
                            if added_to:
                                added_to.union(island)
                                islands.remove(island)
                            else:
                                added_to = island
                    if not added_to:
                        islands.append({(col, row)})
        return len(islands)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No arguments supplied. Please pass path to the input file")
    else:
        print("Island counter main.py got following input file: ", sys.argv)
        count_islands(sys.argv[1])
