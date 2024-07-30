#!/usr/bin/env python3

from collections import defaultdict

# Encode objects as lists with 4 elements.
#
X = 0
M = 1
A = 2
S = 3
#
# Encode instructions as attribute index plus flag plus threshold plus destination.

# e.g. s < 2006:qkq becomes [S, '<', 2006, 'qkq']
#     m > 2090:A            [M, '>', 2090,

translator = {'x': X, 'm': M, 'a': A, 's': S}


def read(fname):
    with open(fname, 'r') as f:
        a, b = f.read().strip().split('\n\n')

    instructions = defaultdict(list)
    literal_instructions = defaultdict(str)
    for line in a.split('\n'):
        c, d = line.strip('}').split('{')
        for x in d.split(','):
            if (s:=max(x.find('>'), x.find('<'))) != -1:
                instruction = [0, 0, 0, 0]
                instruction[0] = translator[x[:s]]
                instruction[1] = x[s]
                instruction[2] = int(x[s+1:x.index(':')])
                instruction[3] = x[x.index(':')+1:]
            else:
                instruction = x

            instructions[c].append(instruction)

        literal_instructions[c] = d

    parts = []
    for line in b.split('\n'):
        part = [0, 0, 0, 0]
        for x in line.strip('{}').split(','):
            name, v = x.split('=')
            part[translator[name]] = int(v)
        parts.append(part)

    return instructions, parts, literal_instructions

def follow(instructions, location, part):
    while location not in 'AR':
        for i in instructions[location]:
            if type(i) is str:
                location = i
                break

            attribute, symbol, threshold, accept_destination = i

            if symbol == '>':
                if part[attribute] > threshold:
                    location = accept_destination
                    break
            elif symbol == '<':
                if part[attribute] < threshold:
                    location = accept_destination
                    break

    return location


def solve_part1(data):
    instructions, parts, literal_instructions = data

    total = 0
    for p in parts:
        location = follow(instructions, 'in', p)
        print(p, location)

        if location == "A":
            total += sum(p)

    return total

# Define a 4 way range as inclusive [(min, max), (min, max), (min, max), (min, max)]

def count(four_range):
    # Return number of corresponding possible parts
    n = 1
    for i in range(4):
        n *= max(0, four_range[i][1] - four_range[i][0] + 1)

    return n

def all_four_ranges(instructions, literal_instructions, location, four_range):

    while location not in 'AR':
        print("investigation", location, four_range, literal_instructions[location])

        for i in instructions[location]:
            if type(i) is str:
                location = i
                break

            attribute, symbol, threshold, accept_destination = i

            smin, smax = four_range[attribute]
            if symbol == '>':
                accept = (max(threshold+1, smin), smax)
                reject = (smin, min(threshold, smax))
            elif symbol == '<':
                accept = (smin, min(smax, threshold-1))
                reject = (max(smin, threshold), smax)

            if accept[0] <= accept[1]:
                nfr_a = four_range[:]
                nfr_a[attribute] = accept
                yield from all_four_ranges(instructions, literal_instructions, accept_destination, nfr_a)

            if reject[0] > reject[1]:
                return

            four_range[attribute] = reject

    if location == 'A':
        print("accepting", four_range)
        yield four_range


def solve_part2(data):

    instructions, _, literal_instructions = data

    location = 'in'

    total = 0
    four_range = [(1, 4000) for _ in range(4)]
    for fr in all_four_ranges(instructions, literal_instructions, location, four_range):
        total += count(fr)

    return total

def main():
    data = read("day19_workflows/input.txt")
    # data = read("day19_workflows/example")

    return solve_part1(data), solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
