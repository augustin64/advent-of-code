#!/usr/bin/python3
"""
Jour 03 du défi Advent Of Code pour l'année 2025
"""
import os

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    filename = os.path.join(os.path.dirname(__file__ ), "inputs", "day03.txt")
    with open(filename, 'r') as f:
        sample = f.read().split('\n')
    sample = [ list(map(int, i)) for i in sample if i != '' ]
    return sample

def part1(sample):
    """Partie 1 du défi"""
    total = 0
    for bat in sample:
        volt = max(bat[:-1])
        volt=volt*10+max(bat[bat.index(volt)+1:])
        total += volt
    return total

def part2(sample):
    """Partie 2 du défi"""
    total = 0
    for bat in sample:
        idx = 0
        volt = 0
        for i in range(12):
            if i==11:
                maxi = max(bat)
            else:
                maxi = max(bat[:-11+i])

            volt = volt*10+maxi
            idx = bat.index(maxi)
            bat = bat[idx+1:]
        total += volt
    return total


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()