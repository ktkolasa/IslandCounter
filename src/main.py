import sys

def my_addition(a, b):
    return a + b


def count_islands(input_file):
    with open(input_file, "r") as input_file:
        for line in input_file:
            pass
    pass


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No arguments supplied. Please pass path to the input file")
    else:
        print("Island counter main.py got following input file: ", sys.argv)
        count_islands(sys.argv[1])

