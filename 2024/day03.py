#!/usr/bin/python3
"""
Jour 03 du défi Advent Of Code pour l'année 2024
"""
import os

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    filename = os.path.join(os.path.dirname(__file__ ), "inputs", "day03.txt")
    with open(filename, 'r') as f:
        sample = f.read()
    return sample

def part1(sample):
    """Partie 1 du défi"""
    tot = 0
    spaces = sample.split("mul(")[1:]
    for space in spaces:
        space = space.split(")")[0]
        try:
            i, j = map(int, space.split(","))
            tot += i*j
        except ValueError:
            continue
    return tot


def part2(sample):
    """Partie 2 du défi"""
    tot = 0
    for sample in sample.split("do()"):
        tot += part1(sample.split("don't()")[0])
    return tot


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()