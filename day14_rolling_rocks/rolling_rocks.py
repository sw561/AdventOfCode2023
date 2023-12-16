#!/usr/bin/env python3

from collections import defaultdict

def read(fname):
    with open(fname, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]

def tilt_north(data):
    for j in range(len(data[0])):
        for i in range(len(data)):
            if data[i][j] == "O":
                i_new = i
                while i_new-1 >= 0 and data[i_new-1][j] == ".":
                    i_new -= 1

                data[i][j] = "."
                data[i_new][j] = "O"

def tilt_south(data):
    for j in range(len(data[0])):
        for i in range(len(data)-1,-1,-1):
            if data[i][j] == "O":
                i_new = i
                while i_new+1 < len(data) and data[i_new+1][j] == ".":
                    i_new += 1

                data[i][j] = "."
                data[i_new][j] = "O"

def tilt_west(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "O":
                j_new = j
                while j_new-1 >= 0 and data[i][j_new-1] == ".":
                    j_new -= 1

                data[i][j] = "."
                data[i][j_new] = "O"

def tilt_east(data):
    for i in range(len(data)):
        for j in range(len(data[0])-1,-1,-1):
            if data[i][j] == "O":
                j_new = j
                while j_new+1 < len(data[0]) and data[i][j_new+1] == ".":
                    j_new += 1

                data[i][j] = "."
                data[i][j_new] = "O"

def calculate_score(data):
    total_score = 0

    for i in range(len(data)):
        score = len(data) - i
        count = sum(1 for si in data[i] if si == "O")

        total_score += score*count

    return total_score

def solve_part1(data):
    tilt_north(data)
    return calculate_score(data)

def cycle(data):
    tilt_north(data)
    tilt_west(data)
    tilt_south(data)
    tilt_east(data)

def solve_part2(data):

    state_dict = defaultdict(list)

    cycle_counter = 0
    while True:

        state = tuple("".join(row) for row in data)
        state_dict[state].append(cycle_counter)

        if len(state_dict[state]) >= 2:
            last_occurence = state_dict[state][-2]

            if (1_000_000_000 - cycle_counter) % (cycle_counter - last_occurence) == 0:
                return calculate_score(data)

        cycle(data)
        cycle_counter += 1

def main():
    data = read("day14_rolling_rocks/input.txt")
    # data = read("day14_rolling_rocks/example")

    return solve_part1([line[:] for line in data]), solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
