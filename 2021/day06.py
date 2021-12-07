#!/usr/bin/python3
"""
Jour 06 du défi Advent Of Code pour l'année 2021
"""

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day06.txt', 'r') as f:
        sample = f.read().split(',')
    sample = [ int(i) for i in sample if i != '' ]
    return sample

def part1(sample):
    """Partie 1 du défi"""
    return NotImplementedError

def part2(sample):
    """Partie 2 du défi"""
    print(sample)
    fishes = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for i in sample:
        fishes[i] += 1
    for i in range(256):
        (fishes[0], fishes[1], fishes[2], fishes[3],
         fishes[4], fishes[5], fishes[6] ,fishes[7], fishes[8]) = (
             fishes[1], fishes[2], fishes[3], fishes[4], fishes[5],
             fishes[6], fishes[7] + fishes[0], fishes[8], fishes[0])
    somme = 0
    for i in range(9):
        somme += fishes[i]
    return somme


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")
