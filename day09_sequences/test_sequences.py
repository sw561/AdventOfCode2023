import pytest
from sequences import read, solve, solve_part1, solve_part2, main

data = read("day09_sequences/example")

@pytest.mark.parametrize("s, e1, e2",
    [([0,3,6,9,12,15], 18, -3),
     ([1,3,6,10,15,21], 28, 0),
     ([10,13,16,21,30,45], 68, 5)
     ])
def test_part1_examples(s, e1, e2):
    assert solve(s) == e1
    assert solve(s[::-1]) == e2

def test_part1():
    assert solve_part1(data) == 114

def test_part2():
    assert solve_part2(data) == 2

@pytest.mark.real
def test_main():
    with open("day09_sequences/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
