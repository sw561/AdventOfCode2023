#!/usr/bin/env python3

def read(fname):
    with open(fname, 'r') as f:
        data = [[int(x) for x in line.split()] for line in f.read().strip().split('\n')]
    return data

def display(i, s):
    print(i, s[:i], s[i:])

def solve(s):
    # i is index of where sequence starts, values before s[i] are starting
    # values for the reconstruction
    i = 0

    # display(i, s)
    while not all(si == 0 for si in s[i:]):
        for j in range(len(s)-1,i,-1):
            s[j] -= s[j-1]
        i += 1
        # display(i, s)

    s.append(0)
    # print("----")

    while i > 0:
        for j in range(i, len(s)):
            s[j] += s[j-1]
        i -= 1
        # display(i, s)
    # print("------------------------------")

    return s[-1]


def solve_part1(data):
    # return 0
    return sum(solve(line[:]) for line in data)

def solve_part2(data):
    return sum(solve(line[::-1]) for line in data)

def main():
    data = read("day09_sequences/input.txt")
    # data = read("day09_sequences/example")

    return solve_part1(data), solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
