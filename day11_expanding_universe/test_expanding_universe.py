import pytest
from expanding_universe import read, solve_part1, main

data = read("day11_expanding_universe/example")

def test_part1():
    assert solve_part1(data) == [374]

def test_part2():
    assert solve_part1(data, [9, 99]) == [1030, 8410]

@pytest.mark.real
def test_main():
    with open("day11_expanding_universe/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
