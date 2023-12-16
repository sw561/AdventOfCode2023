import pytest
from broken_springs import read, solve_part1, solve_part2, main

data = read("day12_broken_springs/example")

def test_part1():
    assert solve_part1(data) == 21

@pytest.mark.skip(reason="Not implemented")
def test_part2():
    assert solve_part2()

@pytest.mark.real
def test_main():
    with open("day12_broken_springs/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
