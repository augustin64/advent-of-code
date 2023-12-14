#!/usr/bin/python3
"""
Jour 14 du défi Advent Of Code pour l'année 2023
"""
import os
from functools import cache

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    filename = os.path.join(os.path.dirname(__file__ ), "inputs", "day14.txt")
    with open(filename, 'r') as f:
        sample = f.read().split('\n')
    sample = [ [j for j in i] for i in sample if i != '' ]
    return sample

@cache
def in_bounds(i_, j_, i, j):
    return i >=0  and j >= 0 and i < i_ and j < j_


def tilt(sample, direction=(1, 0)):
    i_, j_ = len(sample), len(sample[0])
    change = True
    while change:
        change = False
        for i in range(len(sample)):
            for j in range(len(sample[0])):
                if sample[i][j] == 'O' and in_bounds(i_, j_, i+direction[0], j+direction[1]) and sample[i+direction[0]][j+direction[1]] == '.':
                    sample[i][j] = '.'
                    sample[i+direction[0]][j+direction[1]] = 'O'
                    change = True
    #print("\n".join(["".join(i) for i in sample]))
    #print()


def load(sample):
    load = 0
    for i in range(len(sample)):
        for j in range(len(sample)):
            if sample[i][j] == 'O':
                load += len(sample)-i
    return load

def s_to_str(sample):
    return "\n".join(["".join(i) for i in sample])

def cycle(sample, cycles):
    views = {}
    for i in range(cycles):
        s = s_to_str(sample)
        if s in views.keys():
            cycle_length = i-views[s]
            break
        else:
            views[s] = i

        tilt(sample, direction=(-1, 0))
        tilt(sample, direction=(0, -1))
        tilt(sample, direction=(1, 0))
        tilt(sample, direction=(0, 1))

    for i in range((cycles-i)%cycle_length):
        tilt(sample, direction=(-1, 0))
        tilt(sample, direction=(0, -1))
        tilt(sample, direction=(1, 0))
        tilt(sample, direction=(0, 1))

    return load(sample)

def part1():
    """Partie 1 du défi"""
    sample = read_sample()
    tilt(sample, direction=(-1, 0))
    return load(sample)

def part2():
    """Partie 2 du défi"""
    sample = read_sample()
    return cycle(sample, 1000000000)


def main():
    """Fonction principale"""
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")

if __name__ == "__main__":
    main()