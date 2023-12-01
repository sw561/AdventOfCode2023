#!/usr/bin/env python3

def read(fname):
    with open(fname, 'r') as f:
        pass

def solve_part1(data):
    return 0

def solve_part2(data):
    return 0

def main():
    data = read("dayXX_YYY/input.txt")
    # data = read("dayXX_YYY/example")

    return solve_part1(data), solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
