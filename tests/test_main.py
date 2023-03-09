from src.main import count_islands
import pytest

test_cases = [
    ('tests/test_inputs/input.txt', 2),
    ('tests/test_inputs/6_one_column.txt', 6),
    ('tests/test_inputs/7_one_row.txt', 7),
    ('tests/test_inputs/emptyfile.txt', 0),
    ('tests/test_inputs/1_big_island_small_pond.txt', 1),
    ('tests/test_inputs/4_corners.txt', 4),
    ('tests/test_inputs/frame.txt', 1),
    ('tests/test_inputs/one.txt', 1),
    ('tests/test_inputs/zero.txt', 0),
    ('tests/test_inputs/10_adjacent_corners.txt', 10),
]

@pytest.mark.parametrize('sample, expected', test_cases)
def test_count_islands(sample, expected):
    assert count_islands(sample) == expected

# todo:
# not an array (rows of different length)
# very big file
# extra whitespaces
# file with wrong extension / not a file
