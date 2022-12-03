#!/usr/bin/python3
"""
Jour 03 du défi Advent Of Code pour l'année 2022
"""

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day03.txt', 'r') as f:
        sample = f.read().split('\n')
    sample = [ i for i in sample if i != '' ]
    return sample

def split(text):
    half = len(text)/2
    return text[:int(half)], text[int(half):]

def commun(tup):
    p1, p2 = tup
    for i in p1:
        if i in p2:
            return i
    raise Exception("Pas de lettre en commun")

def priority(letter):
    if ord(letter) <= 90:
        return ord(letter)-65+27
    return ord(letter)-97+1

def part1(sample):
    """Partie 1 du défi"""
    return sum(priority(commun(split(i))) for i in sample)


def count(item, iterable):
    nb = 0
    for i in iterable:
        if i == item:
            nb += 1
    return nb

def part2(sample):
    """Partie 2 du défi"""
    somme = 0
    for i in range(0, len(sample), 3):
        comm = list(sample[i])
        for j in comm:
            if j in sample[i+1] and j in sample[i+2]:
                break
        somme += priority(j)
    return somme

def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()