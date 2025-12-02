#!/usr/bin/python3
"""
Jour 01 du défi Advent Of Code pour l'année 2025
"""
import os

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    filename = os.path.join(os.path.dirname(__file__ ), "inputs", "day01.txt")
    with open(filename, 'r') as f:
        sample = f.read().split('\n')
    sample = [ i for i in sample if i != '' ]
    return sample

def part1(sample):
    """Partie 1 du défi"""
    pos = 50
    nb = 0
    for s in sample:
        v = int(s[1:])
        if 'R' in s:
            pos = (pos+v)%100
        else:
            pos = (pos+1000-v)%100 # We should just invert the number before %
        if pos == 0:
            nb+=1
    return nb


def part2(sample):
    """Partie 2 du défi"""
    pos = 50
    nb= 0
    for s in sample:
        pre_nb = nb
        v = int(s[1:])
        if 'R' in s:
            new = (pos+v)
            nb += int(new/100)
            pos = new%100
        elif 'L' in s:
            new = (pos-v)
            nb += -int((pos-v-100)/100)
            if (pos == 0):
                nb -= 1
            pos = new%100
        # print(f"Rotation {s} goes to {pos}, with {nb-pre_nb} clicks")
    return nb


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()