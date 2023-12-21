#!/usr/bin/python3
"""
Jour 21 du défi Advent Of Code pour l'année 2023
"""
import os
from tqdm import tqdm

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

    def valid(pos):
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
        if valid((i, j-1)) and is_point((i, j-1), ext=ext):
            v.append((i, j-1))
        if valid((i-1, j)) and is_point((i-1, j), ext=ext):
            v.append((i-1, j))
        if valid((i, j+1)) and is_point((i, j+1), ext=ext):
            v.append((i, j+1))
        if valid((i+1, j)) and is_point((i+1, j), ext=ext):
            v.append((i+1, j))
        return v

    i, j = find_S()
    pos_ts = {(i, j): [(0, 0)]}
    for i in tqdm(range(steps)):
        new_pos_ts = {}
        for pos in pos_ts.keys():
            for p in voisins(pos, ext=ext):
                mp = (p[0]%len_sample, p[1]%len_sample0)
                tile = (p[0]//len_sample, p[1]//len_sample0)
                if mp not in new_pos_ts.keys():
                    new_pos_ts[mp] = []
                for elem in pos_ts[pos]:
                    t = (tile[0]+elem[0], tile[1]+elem[1])
                    if t not in new_pos_ts[mp]:
                        new_pos_ts[mp].append(t)

        pos_ts = new_pos_ts
    return pos_ts


def part1(sample):
    """Partie 1 du défi"""
    return sum([len(i) for i in do_steps(sample, steps=64, ext=False).values()])

def part2(sample):
    """Partie 2 du défi"""
    print("WARNING, this will take a lot of time (and could not even work)")
    return sum([len(i) for i in do_steps(sample, ext=True).values()])


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()