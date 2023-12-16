import pytest
from mirrors import read, solve_part1, solve_part2, main

data = read("day13_mirrors/example")

def test_part1():
    assert solve_part1(data) == 405

def test_part2():
    assert solve_part2(data) == 400

@pytest.mark.real
def test_main():
    with open("day13_mirrors/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
