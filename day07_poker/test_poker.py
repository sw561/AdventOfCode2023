import pytest
from poker import read, solve_part1, solve_part2, main

data = read("day07_poker/example")

def test_part1():
    assert solve_part1(data) == 6440

def test_part2():
    assert solve_part2(data) == 5905

@pytest.mark.real
def test_main():
    with open("day07_poker/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
