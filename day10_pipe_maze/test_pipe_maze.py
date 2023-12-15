import pytest
from pipe_maze import read, calculate_distances, display, calculate_area, main


@pytest.mark.parametrize("input, s, output",
    [("day10_pipe_maze/example", "F", "day10_pipe_maze/expected"),
     ("day10_pipe_maze/example2", "F", "day10_pipe_maze/expected2"),
     ])
def test_part1(input, s, output):
    data, i, j = read(input, s)
    distances = calculate_distances(data, i, j)
    s = display(data, distances)
    with open(output, 'r') as f:
        assert s == f.read()


@pytest.mark.parametrize("input, s, expected",
    [("day10_pipe_maze/example3", "F", 4),
     ("day10_pipe_maze/example4", "F", 4),
     ("day10_pipe_maze/example5", "F", 8),
     ("day10_pipe_maze/example6", "7", 10),
     ])
def test_part2(input, s, expected):
    data, i, j = read(input, s)
    distances = calculate_distances(data, i, j)
    c = calculate_area(data, distances, i, j)
    assert abs(sum(c.values())) == expected

@pytest.mark.real
def test_main():
    with open("day10_pipe_maze/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
