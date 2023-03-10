from src.main import count_islands
import pytest


test_cases = [
    ("tests/valid_inputs/input.txt", 2),
    ("tests/valid_inputs/6_one_column.txt", 6),
    ("tests/valid_inputs/7_one_row.txt", 7),
    ("tests/valid_inputs/emptyfile.txt", 0),
    ("tests/valid_inputs/1_big_island_small_pond.txt", 1),
    ("tests/valid_inputs/4_corners.txt", 4),
    ("tests/valid_inputs/frame.txt", 1),
    ("tests/valid_inputs/one.txt", 1),
    ("tests/valid_inputs/zero.txt", 0),
    ("tests/valid_inputs/10_adjacent_corners.txt", 10),
]


@pytest.mark.parametrize("sample, expected", test_cases)
def test_count_islands(sample, expected):
    assert count_islands(sample) == expected


err_test = [
    ("tests/test_err_inputs/abcd.txt", FileNotFoundError),
    ("tests/test_err_inputs/other_chars.txt", ValueError),
    ("tests/test_err_inputs/extra_whitespaces.txt", ValueError),
    ("tests/test_err_inputs/not_an_array.txt", ValueError),
]


@pytest.mark.parametrize("sample, expected", err_test)
def test_file_not_found(sample, expected):
    with pytest.raises(expected):
        count_islands(sample)


longrun = pytest.mark.skipif("not config.getoption('longrun')")
longrun_test = [("tests/longrun_inputs/10000x10000_big_file.txt", 1)]


@longrun
@pytest.mark.parametrize("sample, expected", longrun_test)
def test_longrun(sample, expected):
    assert count_islands(sample) == expected
