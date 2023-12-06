import pytest
from racing import read, winning_ways, solve_part2, main

data = read("day06_racing/example")

def test_part1():
    assert list(winning_ways(data)) == [4, 8, 9]

@pytest.mark.skip(reason="Not implemented")
def test_part2():
    assert solve_part2()

@pytest.mark.real
def test_main():
    with open("day06_racing/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
