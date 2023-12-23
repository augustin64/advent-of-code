#!/usr/bin/python3
"""
Jour 18 du défi Advent Of Code pour l'année 2023
"""
import os

from aoc_utils import snippets

directions = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0)
}

dir_col = ['R', 'D', 'L', 'U']

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    filename = os.path.join(os.path.dirname(__file__ ), "inputs", "day18.txt")
    with open(filename, 'r') as f:
        sample = f.read().split('\n')
    sample = [ i for i in sample if i != '' ]
    return sample


def parse_sample(sample, new_method=False):
    if new_method:
        def parse_instr(c):
            c = c.replace("(", '').replace(")", '')
            dir_t = dir_col[int(c[-1])]
            length = int(c[1:-1], 16)
            return dir_t, length, c


        return [parse_instr(c) for (a, b, c) in [j.split(" ") for j in sample]]
    return [(a, int(b), c) for (a, b, c) in [j.split(" ") for j in sample]]


def voisins(i, j):
    return {(i+a, j+b) for (a, b) in directions.values()}


def dig(data, only_edges=False):
    terrain = []
    pos = (0, 0)
    for dir_t, length, color in data:
        if only_edges:
            terrain.append((pos, color))
            pos = (pos[0]+directions[dir_t][0]*length, pos[1]+directions[dir_t][1]*length)
        else:
            for i in range(length):
                terrain.append((pos, color))
                pos = (pos[0]+directions[dir_t][0], pos[1]+directions[dir_t][1])

    new_terrain = {t[0] for t in terrain}
    min_x = min((i[1] for i in new_terrain))
    min_y = min((i[0] for i in new_terrain))
    return [((i-min_y, j-min_x), color) for ((i, j), color) in terrain]


def count_holes(terrain):
    new_terrain = {t[0] for t in terrain}
    max_y = max((i[1] for i in new_terrain))+1
    max_x = max((i[0] for i in new_terrain))+1

    flow = set()

    def has_hole(i, j):
        cpt = 0
        for k in range(j):
            if (i, k) in new_terrain:
                cpt += 1
        if cpt == 1:
            return True
        return False

    count = 0
    for i in range(max_x):
        for j in range(max_y):
            if has_hole(i, j) and (i, j) not in new_terrain:
                flow.add((i, j))

    modif = True
    while modif:
        modif = False
        for i in range(max_x):
            for j in range(max_y):
                if ((i, j) not in flow and len(voisins(i, j) & flow) > 0):
                    if (i, j) not in new_terrain:
                        modif = True
                        flow.add((i, j))

    #print_terrain({(i, '0') for i in flow|new_terrain})
    return len(flow|new_terrain)


def print_terrain(terrain):
    new_terrain = {t[0] for t in terrain}
    max_x = max((i[1] for i in new_terrain))
    max_y = max((i[0] for i in new_terrain))

    for i in range(max_y+1):
        for j in range(max_x+1):
            if (i, j) in new_terrain:
                print('#', end='')
            else:
                print('.', end='')
        print()


def part1(sample):
    """Partie 1 du défi"""
    data = parse_sample(sample, new_method=False)
    terrain = dig(data)
    return count_holes(terrain)

def part2(sample):
    """Partie 2 du défi"""
    data = parse_sample(sample, new_method=True)
    terrain = dig(data, only_edges=True)
    points = [i[0] for i in terrain]
    return snippets.area(points)


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()