#!/usr/bin/env python3

def read(fname, x):
    with open(fname, 'r') as f:
        data = [line.strip() for line in f.readlines()]

    for i in range(len(data)):
        if (a := data[i].find("S")) != -1:
            data[i] = data[i].replace("S", x)
            return data, i, a

directions = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1)
}

look_up = {
    "|": "NS",
    "-": "EW",
    "L": "NE",
    "J": "NW",
    "7": "SW",
    "F": "SE"
}

look_up = {k: [directions[d] for d in v] for k, v in look_up.items()}

print(look_up)

def neighbours(symbol, i, j):
    for (di, dj) in look_up[symbol]:
        yield i+di, j+dj

def calculate_distances(data, i, j):
    start = i, j
    distances = {}
    distances[start] = 0
    to_consider = [start]

    distance = 1

    # Do bfs in the pipe
    while to_consider:
        new_to_consider = []
        for (i, j) in to_consider:

            for (p, q) in neighbours(data[i][j], i, j):
                if (p, q) in distances:
                    continue

                distances[(p, q)] = distance
                new_to_consider.append((p, q))

        to_consider = new_to_consider
        distance += 1

    return distances

def solve_part1(data, i, j):

    distances = calculate_distances(data, i, j)

    return max(distances.values())

def display_chars(data, distances):
    for i in range(len(data)):
        for j in range(len(data[0])):
            if (i, j) in distances:
                yield str(distances[i, j])
            else:
                yield "."
        yield "\n"

def display(data, distances):
    return "".join(display_chars(data, distances))

def solve_part2(data):
    return 0

def main():
    data, i, j = read("day10_pipe_maze/input.txt", "7")
    # data, i, j = read("day10_pipe_maze/example", "F")
    # data, i, j = read("day10_pipe_maze/example2", "F")

    return solve_part1(data, i, j), solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
