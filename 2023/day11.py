#!/usr/bin/python3
"""
Jour 11 du défi Advent Of Code pour l'année 2023
"""
import os

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    filename = os.path.join(os.path.dirname(__file__ ), "inputs", "day11.txt")
    with open(filename, 'r') as f:
        sample = f.read().split('\n')
    sample = [ [j for j in i] for i in sample if i != '' ]
    return sample

def expansion(sample):
    doubled_rows = []
    for i in range(len(sample)):
        empty = True
        for j in range(len(sample[0])):
            if sample[i][j] != ".":
                empty = False
                break
        if empty:
            doubled_rows.append(i)

    doubled_cols = []
    for j in range(len(sample[0])):
        empty = True
        for i in range(len(sample)):
            if sample[i][j] != ".":
                empty = False
                break
        if empty:
            doubled_cols.append(j)

    return (doubled_rows, doubled_cols)


def list_galaxies(sample):
    galaxies = []
    for i in range(len(sample)):
        for j in range(len(sample[0])):
            if sample[i][j] != '.':
                galaxies.append((i, j))

    return galaxies
    
def distance(g1, g2):
    x1, y1 = g1
    x2, y2 = g2
    return abs((x2-x1))+abs((y2-y1))


def real(point, doubled_rows, doubled_cols, exp=1):
    x, y = point
    x1 = x + exp*len([i for i in doubled_rows if i < x])
    y1 = y + exp*len([i for i in doubled_cols if i < y])
    return x1, y1


def part1(sample):
    """Partie 1 du défi"""
    orig = list_galaxies(sample)
    doubled_rows, doubled_cols = expansion(sample)
    galaxies = [real(point, doubled_rows, doubled_cols) for point in orig]

    distances = []
    for i in range(len(galaxies)):
        for j in range(len(galaxies)):
            if i < j:
                distances.append(distance(galaxies[i], galaxies[j]))

    return sum(distances)

def part2(sample):
    """Partie 2 du défi"""
    orig = list_galaxies(sample)
    doubled_rows, doubled_cols = expansion(sample)
    galaxies = [real(point, doubled_rows, doubled_cols, exp=999999) for point in orig]

    distances = []
    for i in range(len(galaxies)):
        for j in range(len(galaxies)):
            if i < j:
                distances.append(distance(galaxies[i], galaxies[j]))

    return sum(distances)


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()