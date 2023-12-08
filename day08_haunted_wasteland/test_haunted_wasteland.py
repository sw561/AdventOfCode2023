import pytest
from haunted_wasteland import read, solve_part1, solve_part2, main


def test_part1():
    example = read("day08_haunted_wasteland/example")
    example2 = read("day08_haunted_wasteland/example2")
    assert solve_part1(example) == 2
    assert solve_part1(example2) == 6

def test_part2():
    example = read("day08_haunted_wasteland/example3")
    assert solve_part2(example) == 6

@pytest.mark.real
def test_main():
    with open("day08_haunted_wasteland/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
