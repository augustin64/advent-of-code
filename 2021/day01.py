#!/usr/bin/python3
"""
Jour 01 du défi Advent Of Code pour l'année 2021
"""

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day01.txt', 'r') as f:
        sample = f.read().split('\n')
    sample = [int(i) for i in sample if i != '']
    return sample


def increased(sample):
    """renvoie le nombre de fois que l'échantillon a augmenté"""
    depth = sample[0]
    depth_incr = 0
    for i in sample:
        if i > depth:
            depth_incr += 1
        depth = i

    return depth_incr

def part1(sample):
    """Partie 1 du défi"""
    return increased(sample)

def part2(sample):
    """Partie 2 du défi"""
    sum_of_measurements = [sample[i]+sample[i+1]+sample[i+2] for i in range(len(sample)-2)]
    return increased(sum_of_measurements)


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")
