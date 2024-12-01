#!/usr/bin/python3
"""
Jour 01 du défi Advent Of Code pour l'année 2024
"""
import os

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    filename = os.path.join(os.path.dirname(__file__ ), "inputs", "day01.txt")
    with open(filename, 'r') as f:
        sample = f.read().split('\n')
    sample = [ list(map(int, i.split())) for i in sample if i != '' ]
    return sample

def part1(sample):
    """Partie 1 du défi"""
    l1, l2 = sorted([l[0] for l in sample]), sorted([l[1] for l in sample])
    
    return sum(abs(l1[i]-l2[i]) for i in range(len(l1)))

def part2(sample):
    """Partie 2 du défi"""
    l1, l2 = sorted([l[0] for l in sample]), sorted([l[1] for l in sample])
    pres = {}
    for i in l2:
        if i not in pres:
            pres[i] = 0
        pres[i] += 1

    score = 0
    for i in l1:
        if i in pres:
            score += pres[i]*i
    return score


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()