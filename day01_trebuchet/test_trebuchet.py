import pytest
from trebuchet import read, solve, part1, part2, main

e1 = read("day01_trebuchet/example")
e2 = read("day01_trebuchet/example2")

def test_part1():
    assert solve(e1, part1) == 142

def test_part2():
    assert solve(e2, part2) == 281

@pytest.mark.real
def test_main():
    with open("day01_trebuchet/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
