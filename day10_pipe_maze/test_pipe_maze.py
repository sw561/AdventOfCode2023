import pytest
from pipe_maze import read, calculate_distances, display, solve_part2, main


@pytest.mark.parametrize("input, s, output",
    [("day10_pipe_maze/example", "F", "day10_pipe_maze/expected"),
     ("day10_pipe_maze/example2", "F", "day10_pipe_maze/expected2"),
     ])
def test_part1(input, s, output):
    data, i, j = read(input, s)
    d = calculate_distances(data, i, j)
    s = display(data, d)
    with open(output, 'r') as f:
        assert s == f.read()


@pytest.mark.skip(reason="Not implemented")
def test_part2():
    assert solve_part2()

@pytest.mark.real
def test_main():
    with open("day10_pipe_maze/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
