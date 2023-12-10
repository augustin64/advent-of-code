#!/usr/bin/python3
"""
Jour 06 du défi Advent Of Code pour l'année 2023
"""
import os

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    filename = os.path.join(os.path.dirname(__file__ ), "inputs", "day06.txt")
    with open(filename, 'r') as f:
        sample = f.read().split('\n')
    sample = [ i for i in sample if i != '' ]
    return sample

def parse_2(sample):
    sample = [i.replace(" ", "") for i in sample]
    return parse_sample(sample)

def parse_sample(sample):
    data = [[int(i) for i in line.split(":")[-1].split(" ") if i != "" ] for line in sample]
    return [(data[0][i], data[1][i]) for i in range(len(data[0]))]


def ways(race):
    time, dist = race
    possible = []
    for i in range(time): # C'est pas le plus beau ni le plus efficace
        speed = i
        time_running = time - i
        if speed * time_running > dist:
            possible.append(i)
    return possible


def mult(l):
    if len(l) == 0:
        return 1
    return l[0]*mult(l[1:])

def part1(sample):
    """Partie 1 du défi"""
    data = parse_sample(sample)
    return mult([len(ways(race)) for race in data])

def part2(sample):
    """Partie 2 du défi"""
    data = parse_2(sample)
    return mult([len(ways(race)) for race in data])


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()