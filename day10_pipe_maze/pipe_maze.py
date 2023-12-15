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

look_up = {k: [(d, *directions[d]) for d in v] for k, v in look_up.items()}

def neighbours(symbol, i, j):
    for (d, di, dj) in look_up[symbol]:
        yield d, i+di, j+dj

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

            for (d, p, q) in neighbours(data[i][j], i, j):
                if (p, q) in distances:
                    continue

                distances[(p, q)] = distance
                new_to_consider.append((p, q))

        to_consider = new_to_consider
        distance += 1

    return distances

def calculate_area(data, distances, i, j):
    start = i, j

    c = {}

    to_consider = [start]

    visited = set()
    visited.add(start)

    def process(d, p, j):
        count = sum(1 for jj in range(j) if (p, jj) not in distances)
        if d == "S":
            count *= -1
        c[(p, j)] = count

    last_NS = None

    while to_consider:
        new_to_consider = []
        for (i, j) in to_consider:

            for (d, p, q) in neighbours(data[i][j], i, j):
                if (p, q) in visited:
                    continue

                if d in "NS":
                    if last_NS is None or d != last_NS:
                        process(d, i, j)
                    process(d, p, j)
                    last_NS = d

                visited.add((p, q))
                new_to_consider.append((p, q))
                break


        to_consider = new_to_consider

    return c


def solve_part1(data, i, j):

    distances = calculate_distances(data, i, j)

    c = calculate_area(data, distances, i, j)

    print(display(data, distances, c))

    return max(distances.values()), abs(sum(c.values()))

def display_chars(data, distances, c):
    ld = len(str(max(distances.values())))
    for i in range(len(data)):
        for j in range(len(data[0])):
            if c is not None and (i, j) in c:
                yield "{0:{1}d}".format(c[i, j], ld)
            elif c is not None and (i, j) in distances:
                yield " "*(ld-1) + "-"
            elif (i, j) in distances:
                yield "{0:{1}d}".format(distances[i, j], ld)
            else:
                yield " "*(ld-1) + "."
        yield "\n"

def display(data, distances, c=None):
    return "".join(display_chars(data, distances, c))

def main():
    data, i, j = read("day10_pipe_maze/input.txt", "7")
    # data, i, j = read("day10_pipe_maze/example", "F")
    # data, i, j = read("day10_pipe_maze/example2", "F")
    # data, i, j = read("day10_pipe_maze/example3", "F")
    # data, i, j = read("day10_pipe_maze/example4", "F")
    # data, i, j = read("day10_pipe_maze/example5", "F")
    # data, i, j = read("day10_pipe_maze/example6", "7")

    return solve_part1(data, i, j)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
