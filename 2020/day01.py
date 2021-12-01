#!/usr/bin/python3
"""
Jour 01 du défi Advent Of Code pour l'année 2021
"""

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day01.txt', 'r') as f:
        sample = f.read().split('\n')
    sample = [int(i) for i in sample if i != '']
    return sample

def part1(sample):
    """Partie 1 du défi"""
    for i in sample:
        for j in sample:
            if i+j == 2020:
                return i*j

    return 0

def part2(sample):
    """Partie 2 du défi"""
    for i in sample:
        for j in sample:
            for k in sample:
                if i+j+k == 2020:
                    return i*j*k
    return 0


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")
