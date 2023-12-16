import pytest
from rolling_rocks import read, solve_part1, solve_part2, main


def test_part1():
    data = read("day14_rolling_rocks/example")
    assert solve_part1(data) == 136

def test_part2():
    data = read("day14_rolling_rocks/example")
    assert solve_part2(data) == 64

@pytest.mark.real
def test_main():
    with open("day14_rolling_rocks/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
