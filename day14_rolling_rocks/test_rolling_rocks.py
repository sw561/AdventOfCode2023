import pytest
from rolling_rocks import read, solve_part1, solve_part2, main

data = read("day14_rolling_rocks/example")

def test_part1():
    assert solve_part1(data) == 136

@pytest.mark.skip(reason="Not implemented")
def test_part2():
    assert solve_part2()

@pytest.mark.real
def test_main():
    with open("day14_rolling_rocks/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
