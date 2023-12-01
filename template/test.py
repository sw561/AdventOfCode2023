import pytest
from YYY import read, solve_part1, solve_part2, main

# data = read("dayXX_YYY/example")

@pytest.mark.skip(reason="Not implemented")
def test_part1():
    assert solve_part1()

@pytest.mark.skip(reason="Not implemented")
def test_part2():
    assert solve_part2()

@pytest.mark.real
def test_main():
    with open("dayXX_YYY/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
