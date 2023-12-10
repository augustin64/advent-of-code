#!/usr/bin/python3
"""
Jour 01 du défi Advent Of Code pour l'année 2023
"""
import os

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    filename = os.path.join(os.path.dirname(__file__ ), "inputs", "day01.txt")
    with open(filename, 'r') as f:
        sample = f.read().split('\n')
    sample = [ i for i in sample if i != '' ]
    return sample

def number(word):
    nbs = (0, 0)
    seen = 0
    for i in word:
        if i >= '0' and i <= '9':
            if seen == 0:
                nbs = (int(i), int(i))
                seen += 1
            else:
                nbs = (nbs[0], int(i))
    return 10*nbs[0]+nbs[1]

def part1(sample):
    """Partie 1 du défi"""
    return sum([
        number(word) for word in sample
    ])

def treat_input(sample):
    pairs = [
        ("one", "o1e"),
        ("two", "t2o"),
        ("three", "th3ee"),
        ("four", "fo4r"),
        ("five", "f5ve"),
        ("six", "s6x"),
        ("seven", "se7en"),
        ("eight", "eig8ht"),
        ("nine", "ni9ne"),
        ("zero", "ze0ro")
    ]
    for base, rep in pairs:
        sample = [i.replace(base, rep) for i in sample]

    return sample

def part2(sample):
    """Partie 2 du défi"""
    return sum([
        number(word) for word in treat_input(sample)
    ])


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()