import pytest
from hashmap import read, my_hash, solve_part1, solve_part2, main

data = read("day15_hashmap/example")

def test_basic():
    assert my_hash("HASH") == 52

def test_part1_individual():
    sol = [my_hash(x) for x in data]
    expected = [30, 253, 97, 47, 14, 180, 9, 197, 48, 214, 231]
    assert sol == expected

def test_part1():
    assert solve_part1(data) == 1320

def test_part2():
    assert solve_part2(data) == 145

@pytest.mark.real
def test_main():
    with open("day15_hashmap/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
