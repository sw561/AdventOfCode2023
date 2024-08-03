import pytest
from hail_stones import read, solve_part1, solve_part2, main

data = read("day24_hail_stones/example")
xymin = 7
xymax = 27

def test_part1():
    assert solve_part1(data, xymin, xymax) == 2

@pytest.mark.skip(reason="Not implemented")
def test_part2():
    assert solve_part2()

@pytest.mark.real
def test_main():
    with open("day24_hail_stones/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
