#!/usr/bin/python3
"""
Jour 01 du défi Advent Of Code pour l'année 2022
"""

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day01.txt', 'r') as f:
        sample = f.read().split('\n\n')
    sample = [ [int(j) for j in i.split("\n") if j != ''] for i in sample if i != '' ]
    return sample

def part1(sample):
    """Partie 1 du défi"""
    return max([sum(i) for i in sample])

def part2(sample):
    """Partie 2 du défi"""
    sums = [sum(i) for i in sample]
    sums.sort()
    return sums[-1] + sums[-2] + sums[-3]


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")
