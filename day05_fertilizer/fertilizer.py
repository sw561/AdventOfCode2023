#!/usr/bin/env python3

def read(fname):
    with open(fname, 'r') as f:
        inp = f.read().strip()

    maps = []

    for section in inp.split('\n\n'):
        lines = section.split('\n')
        if lines[0].startswith("seeds"):
            rest = lines[0].split(': ')[1]
            seeds = [int(x) for x in rest.split()]
            continue

        m = [[int(x) for x in line.split()] for line in lines[1:]]
        maps.append(m)

    return seeds, maps

def translate(x, stage):
    # stage is a series of rules, each rule is [destination, source, range
    # length]
    for (d, s, l) in stage:
        if x in range(s, s+l):
            return d + x - s
    return x

def translate_range(r, stage, start_index=0, indent=0):

    # Range includes start, doesn't include end
    start, end = r
    # print("stage:", stage)
    if start >= end:
        return

    # print("-"*indent, "start, end:", start, end)

    for index in range(start_index, len(stage)):
        (d, s, l) = stage[index]
        # print("-"*indent, "d, s, l:", d, s, l)
        # Map overlapping portion of r with range(s, s+l)

        if end <= s or start >= s+l:
            # No overlap
            continue

        o_start = max(s, start)
        o_end = min(s+l, end)

        yield (d + o_start - s, d + o_end -s)

        yield from translate_range(
            (start, o_start), stage, index+1, indent=indent+1
            )

        yield from translate_range(
            (o_end, end), stage, index+1, indent=indent+1
            )

        return

    yield (start, end)

def translate_ranges(rs, stage):
    # Translate a range, and yield
    for r in rs:
        yield from translate_range(r, stage)

def translate_ranges_all(rs, stages):

    if len(stages) == 1:
        yield from translate_ranges(rs, stages[0])

    else:
        yield from translate_ranges_all(
            translate_ranges(rs, stages[0]),
            stages[1:]
            )

def location(seed, maps):
    x = seed
    for stage in maps:
        x = translate(x, stage)
        # print("x:", x)
    location = x
    # print("seed, location:", seed, location)
    return location

def solve_part1(data):
    seeds, maps = data

    return min(location(seed, maps) for seed in seeds)

def solve_part2_brute_gen(data):
    seeds, maps = data

    for si in range(0, len(seeds), 2):

        r = (seeds[si], seeds[si]+seeds[si+1])

        for s in range(*r):
            yield location(s, maps)

def solve_part2_brute(data):
    return min(solve_part2_brute_gen(data))



def solve_part2_ranges(data):
    seeds, maps = data

    for si in range(0, len(seeds), 2):

        r = (seeds[si], seeds[si]+seeds[si+1])

        yield from translate_ranges_all([r], maps)

def solve_part2(data):

    return min(r[0] for r in solve_part2_ranges(data))



def main():
    data = read("day05_fertilizer/input.txt")
    # data = read("day05_fertilizer/example")

    return solve_part1(data), solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
