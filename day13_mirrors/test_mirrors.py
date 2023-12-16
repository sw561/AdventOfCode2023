import pytest
from mirrors import read, solve, main

def test_example():
    data = read("day13_mirrors/example")
    assert solve(data) == (405, 400)

@pytest.mark.real
def test_main():
    with open("day13_mirrors/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
