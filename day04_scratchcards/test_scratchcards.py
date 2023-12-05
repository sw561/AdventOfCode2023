import pytest
from scratchcards import read, solve, main

def test_example():
    data = read("day04_scratchcards/example")
    assert solve(data) == (13, 30)

@pytest.mark.real
def test_main():
    with open("day04_scratchcards/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
