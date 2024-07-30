import pytest
from workflows import read, solve_part1, solve_part2, main

data = read("day19_workflows/example")

def test_part1():
    assert solve_part1(data) == 19114

def test_part2():
    assert solve_part2(data) == 167409079868000

@pytest.mark.real
def test_main():
    with open("day19_workflows/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
