import pytest
from garden import read, solve_part1, solve_part2, main

data = read("day21_garden/example")

def test_part1():
    assert solve_part1(data, total_steps=6) == 16

@pytest.mark.skip(reason="Not implemented")
def test_part2():
    assert solve_part2()

@pytest.mark.real
def test_main():
    with open("day21_garden/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
