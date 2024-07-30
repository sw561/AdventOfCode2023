#!/usr/bin/env python3

from collections import deque, defaultdict
from math import lcm

def read(fname):
    components = dict()
    conjunctions = dict()
    with open(fname, 'r') as f:
        for line in f.read().strip().split('\n'):
            name, outputs = line.split(' -> ')
            if name[0] in '%&':
                components[name[1:]] = outputs.split(', ')
            else:
                components[name] = outputs.split(', ')
            if name[0] == '&':
                conjunctions[name[1:]] = []

    for c in components:
        for o in components[c]:
            if o in conjunctions:
                conjunctions[o].append(c)

    return components, conjunctions

LOW = 0
HIGH = 1

def solve_part1(data):
    components, conjunctions = data

    memory = dict()
    for comp in components:
        if comp not in conjunctions:
            memory[comp] = 0

    conjunction_memory = dict()
    for conj in conjunctions:
        conjunction_memory[conj] = {inp: 0 for inp in conjunctions[conj]}

    l, h = 0, 0

    part2 = 'hp' in conjunctions

    # hp is conjunction node which outputs to rx
    controllers = {c: None for c in ([] if not part2 else conjunctions['hp'])}

    button_presses = 0
    while button_presses < 1000 or (part2 and any(v is None for v in controllers.values())):
        button_presses += 1

        l, h = process_signals(button_presses, controllers,
            components, conjunctions,
            memory, conjunction_memory,
            l, h)

        if button_presses == 1000:
            part1 = l * h

    if part2:
        part2 = lcm(*controllers.values())
        return part1, part2
    return part1, None

def process_signals(button_presses,
        controllers,
        components,
        conjunctions,
        memory,
        conjunction_memory,
        lowbies,
        highbies):

    signals = deque([('button', 'broadcaster', LOW)])

    while signals:
        origin, dest, signal = signals.popleft()
        # print(origin, "-high->" if signal else "-low->", dest)

        if dest == "rx" and signal == LOW:
            raise Exception("RX")

        if dest == "hp" and signal == HIGH:
            print(button_presses, origin, "-high->" if signal else "-low->", dest)
            if controllers[origin] is None:
                controllers[origin] = button_presses

        if signal == LOW:
            lowbies += 1
        else:
            highbies += 1

        if dest == "broadcaster":
            for o in components[dest]:
                signals.append((dest, o, signal))

        elif dest == "output":
            continue

        elif dest not in conjunctions:
            # flip flop
            if signal == HIGH:
                continue

            memory[dest] = 1 - memory[dest]
            for o in components[dest]:
                signals.append((dest, o, memory[dest]))

        else:
            # conjunction
            conjunction_memory[dest][origin] = signal
            if all(v == HIGH for v in conjunction_memory[dest].values()):
                for o in components[dest]:
                    signals.append((dest, o, LOW))
            else:
                for o in components[dest]:
                    signals.append((dest, o, HIGH))

    return lowbies, highbies

def solve_part2(data):
    return 0

def main():
    data = read("day20_pulses/input.txt")
    # data = read("day20_pulses/example")
    # data = read("day20_pulses/example1")

    return solve_part1(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
