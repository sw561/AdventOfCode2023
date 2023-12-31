import pytest
from cube_conundrum import read, solve_part1, solve_part2, main

data = read("day02_cube_conundrum/example")

def test_part1():
    assert solve_part1(data) == 8

def test_part2():
    assert solve_part2(data) == 2286

@pytest.mark.real
def test_main():
    with open("day02_cube_conundrum/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
