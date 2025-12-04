#!/usr/bin/python3
"""
Jour 04 du défi Advent Of Code pour l'année 2025
"""
import os
from aoc_utils import snippets

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    filename = os.path.join(os.path.dirname(__file__ ), "inputs", "day04.txt")
    with open(filename, 'r') as f:
        sample = f.read().split('\n')
    sample = [ list(i) for i in sample if i != '' ]
    return sample

def print_puzzle(sample, acc):
    for i in range(len(sample)):
        line = "".join([
            sample[i][j] if not (i, j) in acc else "x"
            for j in range(len(sample[0]))
        ])
        print(line)

def get_removable_rolls(sample):
    max_i = len(sample)
    max_j = len(sample[0])
    acc = []
    for i in range(max_i):
        for j in range(max_j):
            if sample[i][j] != "@":
                continue
            adj = snippets.get8_adj(i, j, max_i, max_j)
            tot = 0
            for (x, y) in adj:
                if sample[x][y] == "@":
                    tot += 1
                    if tot >= 4:
                        break
            else:
                #print(f"{i, j} accessible, {tot}/{len(adj)}")
                acc.append((i, j))
    return acc

def part1(sample):
    """Partie 1 du défi"""
    return len(get_removable_rolls(sample))

def part2(sample):
    """Partie 2 du défi"""
    total = 0
    removable = get_removable_rolls(sample)
    while len(removable) > 0:
        total += len(removable)
        for (x, y) in removable:
            sample[x][y] = "."
        removable = get_removable_rolls(sample)
        #print_puzzle(sample, removable)
    return total
        


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()