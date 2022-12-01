# -*- coding: utf-8 -*-

"""
Created on Wed Dec  1 16:59:02 2021

@author: 
"""
import os
import time
t = time.time()

currentpath = os.path.dirname(os.path.realpath(__file__));
#input_File= os.path.join(currentpath, "input.txt")
input_File= os.path.join(currentpath, "Example_input.txt")

with open(input_File) as file:
        lines = file.readlines()
        for l in lines:
            for e in l.split(','):
                print(e)


    
# do stuff
elapsed = time.time() - t
 
print("")
print("time: " + str(elapsed) )

from re import finditer
# test_file = 'data/test/day-18.txt'
# data_file = 'data/day-18.txt'


data_file = os.path.join(currentpath, "input.txt")

def pair(left, right):
    return f'[{left},{right}]'


def find_ranges(pattern, line):
    for x in finditer(pattern, line):
        yield x.start(), x.end()


def explode(string, added, direction):
    for s, e in list(find_ranges(r'\d+', string))[::direction]:
        new_value = int(string[s:e]) + int(added)
        return string[:s] + str(new_value) + string[e:]
    return string


def reducer(line):
    for ds, de in find_ranges(r'\[\d+,\d+\]', line):
        before = line[:ds]
        if before.count('[') - before.count(']') >= 4:
            after = line[de:]
            d1, d2 = line[ds+1:de-1].split(',')
            before = explode(before, d1, -1)
            after = explode(after, d2, 1)
            return reducer(f'{before}0{after}')

    for s, e in find_ranges(r'\d{2,}', line):
        large = int(line[s:e])
        down = large // 2
        up = large - down
        return reducer(line[:s] + pair(down, up) + line[e:])

    return line


def magnitude(line):
    while ranges := list(find_ranges(r'\[\d+,\d+\]', line)):
        for s, e in reversed(ranges):
            n1, n2 = map(int, line[s+1: e-1].split(','))
            n = n1*3 + n2*2
            line = line[:s] + str(n) + line[e:]
    return int(line)


def process(file):
    lines = open(file).read().splitlines()
    reduced = []
    last = None
    for line in lines:
        line = reducer(line)
        reduced.append(line)
        if last:
            last = reducer(pair(last, line))
        else:
            last = line

    highest = 0
    for left in reduced:
        for right in reduced:
            if left != right:
                line = reducer(pair(left, right))
                current = magnitude(line)
                highest = max(highest, current)

    part_1 = magnitude(last)
    part_2 = highest

    return [part_1, part_2]


# p1t, p2t = process(test_file)
# assert p1t == 4140, p1t
# assert p2t == 3993, p2t


p1, p2 = process(data_file)

print('Part 1:', p1)
print('Part 2:', p2)