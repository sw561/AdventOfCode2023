import pytest
from broken_springs import read, solve_part1, valid_arrangements_brute, solve_part2, main

data = read("day12_broken_springs/example")

def test_part1():
    assert solve_part1(data) == 21

def test_part1_brute():
    assert solve_part1(data, va=valid_arrangements_brute) == 21

def test_part2():
    assert solve_part2(data) == 525152

@pytest.mark.real
def test_main():
    with open("day12_broken_springs/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
