#!/usr/bin/python3
"""
Jour 03 du défi Advent Of Code pour l'année 2020
"""

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day03.txt', 'r') as f:
        sample = f.read().split('\n')
    sample = [ i for i in sample if i != '' ]
    return sample

def slope(mv_x, mv_y, sample):
    """Compte le nombre d'arbres que se prend le marcheur"""
    pos = (0,0)
    n1 = len(sample)
    n2 = len(sample[0])
    count = 0
    while pos[1] < n1-mv_y:
        pos = ((pos[0]+mv_x)%n2, (pos[1]+mv_y))
        if sample[pos[1]][pos[0]] == "#":
            count += 1
    return count

def part1(sample):
    """Partie 1 du défi"""
    return slope(3, 1, sample)

def part2(sample):
    """Partie 2 du défi"""
    sol = 1
    sol *= slope(1, 1, sample)
    sol *= slope(3, 1, sample)
    sol *= slope(5, 1, sample)
    sol *= slope(7, 1, sample)
    sol *= slope(1, 2, sample)
    return sol


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")
