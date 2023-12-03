import pytest
from gear_ratios import read, solve, main

data = read("day03_gear_ratios/example")

def test_part1():
    assert solve(data) == (4361, 467835)

@pytest.mark.real
def test_main():
    with open("day03_gear_ratios/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
