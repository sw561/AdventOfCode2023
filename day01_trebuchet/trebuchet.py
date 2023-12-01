#!/usr/bin/env python3

import string

def read(fname):
    with open(fname, 'r') as f:
        return f.read().split()

def first_last(it):
    try:
        first = next(it)
    except StopIteration:
        print(list(it))
        raise
    last = first
    for i in it:
        last = i
    return first, last

def calibration_value(digit_iterator):
    first, last = first_last(digit_iterator)
    return 10*first + last

def solve_part1(data):
    return sum(
        calibration_value(int(s) for s in line if s in string.digits)
            for line in data
        )

written_digits = {1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"}

def get_digits(s):

    for i in range(len(s)):

        if s[i] in string.digits:
            yield int(s[i])

        else:
            for k, v in written_digits.items():
                if s[i:].startswith(v):
                    yield k


def solve_part2(data):
    return sum(
        calibration_value(get_digits(line))
            for line in data
        )

def main():
    data = read("day01_trebuchet/input.txt")
    # data = read("day01_trebuchet/example")
    # data = read("day01_trebuchet/example2")

    return solve_part1(data), solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
