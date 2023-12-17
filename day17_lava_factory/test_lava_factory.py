import pytest
from lava_factory import read, solve_part1, solve_part2, main

data = read("day17_lava_factory/example")

def test_part1():
    assert solve_part1(data) == 102

@pytest.mark.skip(reason="Not implemented")
def test_part2():
    assert solve_part2()

@pytest.mark.real
def test_main():
    with open("day17_lava_factory/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
