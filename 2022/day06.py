#!/usr/bin/python3
"""
Jour 06 du défi Advent Of Code pour l'année 2022
"""
import os

def read_sample(base_dir="."):
    """récupère les entrées depuis le fichier texte correspondant"""
    with open(os.path.join(base_dir, 'inputs/day06.txt'), 'r') as f:
        sample = f.read().split('\n')
    sample = [ i for i in sample if i != '' ][0]
    return sample

def count(item, iterable):
    nb = 0
    for i in iterable:
        if i == item:
            nb += 1
    return nb

def start_of_something(text, size): # Complexité affreuse
    for i in range(0, len(text)-size):
        rolling = text[i:size+i]
        good = True
        for c in rolling:
            if count(c, rolling) > 1:
                good = False
        if good:
            return i

            

def part1(sample):
    """Partie 1 du défi"""
    return start_of_something(sample, 4)+4

def part2(sample):
    """Partie 2 du défi"""
    return start_of_something(sample, 14)+14


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()