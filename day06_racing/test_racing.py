import pytest
from racing import read, winning_ways, brute_winning_ways, main

part1, part2 = read("day06_racing/example")

def test_part1():
    l_fast = [winning_ways(t, d) for t, d in zip(*part1)]
    l_brute = [brute_winning_ways(t, d) for t, d in zip(*part1)]
    assert l_fast == l_brute == [4, 8, 9]

def test_part2():
    for t, d in zip(*part2):
        assert winning_ways(t, d) == 71503

@pytest.mark.real
def test_main():
    with open("day06_racing/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
