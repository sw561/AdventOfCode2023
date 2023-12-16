#!/usr/bin/env python3

def read(fname):
    with open(fname, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]

def tilt_north(data):

    # for line in data:
    #     print("".join(line))

    for j in range(len(data[0])):
        for i in range(len(data)):

            if data[i][j] == "O":
                # Find northenmost resting spot
                i_new = i
                while i_new-1 >= 0 and data[i_new-1][j] == ".":
                    i_new -= 1

                data[i][j] = "."
                data[i_new][j] = "O"

    # print("-----------------------------------")
    # for line in data:
    #     print("".join(line))

def solve_part1(data):

    tilt_north(data)

    total_score = 0

    for i in range(len(data)):
        score = len(data) - i
        count = sum(1 for si in data[i] if si == "O")

        total_score += score*count

    return total_score

def solve_part2(data):
    return 0

def main():
    data = read("day14_rolling_rocks/input.txt")
    # data = read("day14_rolling_rocks/example")

    return solve_part1(data), solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
