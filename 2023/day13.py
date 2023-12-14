#!/usr/bin/python3
"""
Jour 13 du défi Advent Of Code pour l'année 2023
"""
import os

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    filename = os.path.join(os.path.dirname(__file__ ), "inputs", "day13.txt")
    with open(filename, 'r') as f:
        sample = f.read().split('\n\n')
    sample = [ [[k for k in j] for j in i.split('\n') if j != ''] for i in sample if i != '' ]
    return sample

def diff(line1, line2):
    return sum([1 for i in range(len(line1)) if line1[i] != line2[i]])

def transpose(pattern):
    return [[pattern[j][i] for j in range(len(pattern))] for i in range(len(pattern[0]))]

def h_reflects(pattern, smudge=0):
    nb = 0
    for i in range(len(pattern)):
        total_diff = sum((diff(pattern[i-j], pattern[i+j-1]) for j in range(len(pattern[0])) if i-j >= 0 and i+j-1 < len(pattern) and i+j-1 > 0 and i-j < i+j-1))
        if total_diff == smudge:
            nb += i
    return nb


def part1(sample):
    """Partie 1 du défi"""
    return sum((h_reflects(pattern) for pattern in sample))*100 + sum((h_reflects(transpose(pattern)) for pattern in sample))

def part2(sample):
    """Partie 2 du défi"""
    return sum((h_reflects(pattern, smudge=1) for pattern in sample))*100 + sum((h_reflects(transpose(pattern), smudge=1) for pattern in sample))


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()