#!/usr/bin/env python3

def read(fname):
    with open(fname, 'r') as f:
        data = [line for line in f.read().strip().split('\n')]

    for i, line in enumerate(data):
        if (c := line.find('S')) != -1:
            data[i] = line.replace('S', '.')
            source = (i, c)

    return data, source

def neighbours(pos, data):
    x, y = pos
    for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if 0 <= i < len(data[j]) and 0 <= j < len(data):
            if data[j][i] == '.':
                yield i, j

def display(visited, data):
    last = max(visited.values())
    count = 0
    for j, row in enumerate(data):
        for i, x in enumerate(row):
            if (i, j) in visited and visited[(i, j)]%2 == last%2:
                print('O', end='')
                count += 1
            else:
                print(x, end='')
        print()

    return count

def solve_part1(data, total_steps=64):
    data, source = data

    for line in data:
        print(line)

    print("source:", source)

    # Do BFS
    visited = dict()
    visited[source] = 0

    pos = [source]
    display(visited, data)
    for n_steps in range(1, total_steps+1):
        new_pos = []
        for p in pos:
            for n in neighbours(p, data):
                if n not in visited:
                    new_pos.append(n)
                    visited[n] = n_steps

        pos = new_pos

    count = display(visited, data)

    return count

def solve_part2(data):
    return 0

def main():
    data = read("day21_garden/input.txt")
    # data = read("day21_garden/example")

    return solve_part1(data), solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
