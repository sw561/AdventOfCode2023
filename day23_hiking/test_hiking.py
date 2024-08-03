import pytest
from hiking import read, display, solve_part1, solve_part2, main

data = read("day23_hiking/example")

def test_part1():
    longest_route = solve_part1(data)

    T = """#O#####################
#OOOOOOO#########...###
#######O#########.#.###
###OOOOO#OOO>.###.#.###
###O#####O#O#.###.#.###
###OOOOO#O#O#.....#...#
###v###O#O#O#########.#
###...#O#O#OOOOOOO#...#
#####.#O#O#######O#.###
#.....#O#O#OOOOOOO#...#
#.#####O#O#O#########v#
#.#...#OOO#OOO###OOOOO#
#.#.#v#######O###O###O#
#...#.>.#...>OOO#O###O#
#####v#.#.###v#O#O###O#
#.....#...#...#O#O#OOO#
#.#########.###O#O#O###
#...###...#...#OOO#O###
###.###.#.###v#####O###
#...#...#.#.>.>.#.>O###
#.###.###.#.###.#.#O###
#.....###...###...#OOO#
#####################.#"""

    assert display(data, longest_route) == T
    assert len(longest_route) == 94


def test_part2():
    longest_route, longest_length = solve_part2(data)
    assert longest_length == 154

@pytest.mark.real
def test_main():
    with open("day23_hiking/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
