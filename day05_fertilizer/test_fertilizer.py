import pytest
from fertilizer import read, location,\
    solve_part1, translate_ranges_all,\
    solve_part2_brute, solve_part2_ranges, main

data = read("day05_fertilizer/example")

def test_locations():
    seeds, maps = data
    locations = [location(seed, maps) for seed in seeds]
    assert locations == [82, 43, 86, 35]

def test_part1():
    assert solve_part1(data) == 35

def test_part2_small_ranges():
    _, maps = data
    for seed in range(100):
        r = (seed, seed+1)
        l = location(seed, maps)
        r_locs = list(translate_ranges_all([r], maps))
        assert r_locs == [(l, l+1)]

def test_part2_big_range():
    _, maps = data
    locs = set()
    for seed in range(100):
        locs.add(location(seed, maps))

    locs_comp = set()
    for r_locs in translate_ranges_all([(0, 100)], maps):
        print("r_locs:", r_locs)
        for s in range(*r_locs):
            locs_comp.add(s)

    assert locs == locs_comp

def test_part2():
    locs = set(solve_part2_brute(data))

    locs_comp = set()
    for r in solve_part2_ranges(data):
        for s in range(*r):
            locs_comp.add(s)

    assert locs == locs_comp
    assert min(locs) == 46

@pytest.mark.real
def test_main():
    with open("day05_fertilizer/output.txt", 'r') as f:
        answer = tuple(int(x) for x in f.readlines())
    assert main() == answer
