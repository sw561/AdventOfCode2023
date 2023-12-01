#!/usr/bin/env python3

def read(fname):
    with open(fname, 'r') as f:
        return f.read().split()

written_digits = {1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"}

str_digits = {str(x): x for x in written_digits.keys()}

def part1(letter, suffix):
    if letter in str_digits:
        return str_digits[letter]

def part2(letter, suffix):
    if letter in str_digits:
        return str_digits[letter]

    for k, v in written_digits.items():
        if suffix.startswith(v):
            return k

def calibration_value(s, get_digit):
    first = next(d for i in range(len(s))
            if (d:=get_digit(s[i], s[i:])) is not None
        )
    last = next(d for i in range(len(s)-1,-1,-1)
            if (d:=get_digit(s[i], s[i:])) is not None
        )

    return 10*first + last

def solve(data, part):
    return sum(
        calibration_value(line, part) for line in data
        )

def main():
    data = read("day01_trebuchet/input.txt")
    # data = read("day01_trebuchet/example")
    # data = read("day01_trebuchet/example2")

    return solve(data, part1), solve(data, part2)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
