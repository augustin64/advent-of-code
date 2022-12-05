#!/usr/bin/python3
"""
Jour 04 du défi Advent Of Code pour l'année 2022
"""

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day04.txt', 'r') as f:
        sample = f.read().split('\n')
    sample = [ ([int(j) for j in i.split(",")[0].split("-")], [int(j) for j in i.split(",")[1].split("-")]) for i in sample if i != '' ]
    return sample

def part1(sample):
    """Partie 1 du défi"""
    complete_overlaps = 0
    for i in sample:
        if i[0][0] <= i[1][0] and i[0][1] >= i[1][1]:
            # Left overlap
            complete_overlaps += 1
        elif i[1][0] <= i[0][0] and i[1][1] >= i[0][1]:
            # Right overlap
            complete_overlaps += 1
    return complete_overlaps

def part2(sample):
    """Partie 2 du défi"""
    partial_overlaps = 0
    for i in sample:
        if i[0][0] <= i[1][0]:
            if i[0][1] >= i[1][0]:
                partial_overlaps += 1
        elif i[1][0] <= i[0][0]:
            if i[1][1] >= i[0][0]:
                partial_overlaps += 1
    return partial_overlaps


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()