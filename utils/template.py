#!/usr/bin/python3
"""
Jour DAY du défi Advent Of Code pour l'année YEAR
"""
import os

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    filename = os.path.join(os.path.dirname(__file__ ), "inputs", "dayDAY.txt")
    with open(filename, 'r') as f:
        sample = f.read().split('\n')
    sample = [ i for i in sample if i != '' ]
    return sample

def part1(sample):
    """Partie 1 du défi"""
    return NotImplementedError

def part2(sample):
    """Partie 2 du défi"""
    return NotImplementedError


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()