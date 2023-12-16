#!/usr/bin/env python3

from collections import defaultdict, OrderedDict

def read(fname):
    with open(fname, 'r') as f:
        return f.read().strip().split(',')

def my_hash(x):
    h = 0
    for c in x:
        h = (h + ord(c))*17 % 256
    return h

def solve_part1(data):
    return sum(map(my_hash, data))

def solve_part2(data):
    boxes = defaultdict(OrderedDict)

    for instruction in data:
        s_index = max(instruction.find('='), instruction.find('-'))

        label = instruction[:s_index]
        box = boxes[my_hash(label)]

        if instruction[s_index] == "=":
            focal_length = int(instruction[s_index+1:])
            box[label] = focal_length

        else:
            box.pop(label, None)

        # for i in sorted(boxes.keys()):
        #     print("i, boxes[i]:", i, boxes[i])

    total_power = 0
    for box_number, box in boxes.items():
        for slot, lens in enumerate(box, start=1):
            total_power += (box_number+1) * slot * box[lens]

    return total_power

def main():
    data = read("day15_hashmap/input.txt")
    # data = read("day15_hashmap/example")

    return solve_part1(data), solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
