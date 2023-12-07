import pytest
from poker import read, solve, main

def test_example():
    data = read("day07_poker/example")
    assert solve(data) == (6440, 5905)

def test_example2():
    data = read("day07_poker/example2")
    assert solve(data) == (201, 102)

@pytest.mark.real
def test_main():
    with open("day07_poker/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
