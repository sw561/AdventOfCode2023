#!/usr/bin/env python3

from collections import deque, defaultdict

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
    # for k, v in components.items():
    #     if k in conjunctions:
    #         print("&&&:", k, v, conjunctions[k])
    #     else:
    #         print("k, v:", k, v)

    memory = dict()
    for comp in components:
        if comp not in conjunctions:
            memory[comp] = 0

    conjunction_memory = dict()
    for conj in conjunctions:
        conjunction_memory[conj] = {inp: 0 for inp in conjunctions[conj]}

    l, h = 0, 0

    for button_presses in range(1000):
        # print(button_presses)
        l, h = process_signals(components, conjunctions, memory, conjunction_memory, l, h)

        # print()
        # # print("-----------------------")

        # print(l, h)

        # print()

        # print(memory)
        # print(conjunction_memory)


    return l * h

def process_signals(components, conjunctions, memory, conjunction_memory, lowbies, highbies):
    signals = deque([('button', 'broadcaster', LOW)]) # Use a stack to process signals

    while signals:
        origin, dest, signal = signals.popleft()
        # print(origin, "-high->" if signal else "-low->", dest)

        if dest == "rx" and signal == LOW:
            raise Exception("RX")

        #
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
    # print("-----------------")

    return solve_part1(data), solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
