import pytest
from pulses import read, solve_part1, solve_part2, main

data = read("day20_pulses/example")
data1 = read("day20_pulses/example1")

def test_part1():
    assert solve_part1(data) == 8000 * 4000
    assert solve_part1(data1) == 4250 * 2750

@pytest.mark.skip(reason="Not implemented")
def test_part2():
    assert solve_part2()

@pytest.mark.real
def test_main():
    with open("day20_pulses/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
