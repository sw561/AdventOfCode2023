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
    # stage is a series of rules, each rule is [destination, source, range length]
    for (d, s, l) in stage:
        if x in range(s, s+l):
            return d + x - s
    return x

def location(seed, maps):
    x = seed
    for stage in maps:
        x = translate(x, stage)
    location = x
    # print("seed, location:", seed, location)
    return location

def solve_part1(data):
    seeds, maps = data

    return min(location(seed, maps) for seed in seeds)

def solve_part2(data):
    return 0

def main():
    data = read("day05_fertilizer/input.txt")
    # data = read("day05_fertilizer/example")

    return solve_part1(data), solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
