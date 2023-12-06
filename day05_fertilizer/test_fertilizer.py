import pytest
from fertilizer import read, location, solve_part1, solve_part2, main

data = read("day05_fertilizer/example")

def test_locations():
    seeds, maps = data
    locations = [location(seed, maps) for seed in seeds]
    assert locations == [82, 43, 86, 35]

def test_part1():
    assert solve_part1(data) == 35

@pytest.mark.skip(reason="Not implemented")
def test_part2():
    assert solve_part2()

@pytest.mark.real
def test_main():
    with open("day05_fertilizer/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
