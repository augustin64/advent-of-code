#!/usr/bin/python3
"""
Jour 21 du défi Advent Of Code pour l'année 2023
"""
import os

from aoc_utils import decorators, snippets

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    filename = os.path.join(os.path.dirname(__file__ ), "inputs", "day21.txt")
    with open(filename, 'r') as f:
        sample = f.read().split('\n')
    sample = [[j for j in i] for i in sample if i != '' ]
    return sample

def do_steps(sample, steps=26501365, ext=False):
    len_sample = len(sample)
    len_sample0 = len(sample[0])

    def find_S():
        for i in range(len_sample):
            for j in range(len_sample0):
                if sample[i][j] == 'S':
                    return (i, j)

    def valid(pos, ext=False):
        if ext:
            return True
        return pos[0] >= 0 and pos[1] >= 0 and pos[0] < len_sample and pos[1] < len_sample0

    def is_point(pos, ext=False):
        if not ext and valid(pos):
            if sample[pos[0]][pos[1]] == '.' or sample[pos[0]][pos[1]] == 'S':
                return True
            return False
        if ext and sample[pos[0]%len_sample][pos[1]%len_sample0] == '.' or sample[pos[0]%len_sample][pos[1]%len_sample0] == 'S':
            return True
        return False

    def voisins(pos, ext=False):
        i, j = pos
        v = []
        if valid((i, j-1), ext=ext) and is_point((i, j-1), ext=ext):
            v.append((i, j-1))
        if valid((i-1, j), ext=ext) and is_point((i-1, j), ext=ext):
            v.append((i-1, j))
        if valid((i, j+1), ext=ext) and is_point((i, j+1), ext=ext):
            v.append((i, j+1))
        if valid((i+1, j), ext=ext) and is_point((i+1, j), ext=ext):
            v.append((i+1, j))
        return v

    i, j = find_S()
    pos_ts = {(i, j)}
    for i in range(steps):
        new_pos_ts = set()
        for pos in pos_ts:
            for p in voisins(pos, ext=ext):
                new_pos_ts.add(p)

        pos_ts = new_pos_ts
    return pos_ts


@decorators.timeit
def part1(sample):
    """Partie 1 du défi"""
    return len(do_steps(sample, steps=64, ext=False))

@decorators.timeit
def part2(sample):
    """Partie 2 du défi"""
    def challenge(steps):
        return len(do_steps(sample, steps=steps, ext=True))


    half_size = len(sample)//2
    size = len(sample)
    points = [
        (half_size, challenge(half_size)),
        (half_size+size, challenge(half_size+size)),
        (half_size+2*size, challenge(half_size+2*size))
    ]
    return snippets.lagrange_interpolation(points, 26501365)




def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()