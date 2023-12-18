import pytest
from lagoon import read, solve_part1, solve_part2, main

data = read("day18_lagoon/example", "DR")

def test_part1():
    assert solve_part1(data) == 62

def test_part2():
    assert solve_part2(data) == 952408144115

@pytest.mark.real
def test_main():
    with open("day18_lagoon/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
