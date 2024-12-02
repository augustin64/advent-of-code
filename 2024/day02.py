#!/usr/bin/python3
"""
Jour 02 du défi Advent Of Code pour l'année 2024
"""
import os

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    filename = os.path.join(os.path.dirname(__file__ ), "inputs", "day02.txt")
    with open(filename, 'r') as f:
        sample = f.read().split('\n')
    sample = [ list(map(int, i.split())) for i in sample if i != '' ]
    return sample

def part1(sample):
    """Partie 1 du défi"""
    def safe(report):
        def valid(r1, r2):
            return r1 > r2 and r1-3 <= r2
        return all(valid(report[i], report[i+1]) for i in range(len(report)-1)) or all(valid(report[i+1], report[i]) for i in range(len(report)-1))
    return sum([1 for report in sample if safe(report)])

def part2(sample):
    """Partie 2 du défi"""
    def supersafe(report):
        def valid(r1, r2):
            return r1 > r2 and r1-3 <= r2
        return all(valid(report[i], report[i+1]) for i in range(len(report)-1)) or all(valid(report[i+1], report[i]) for i in range(len(report)-1))

    def safe(report):
        return supersafe(report) or any(supersafe(report[0:i]+report[i+1:len(report)]) for i in range(len(report)+1)) 
    return sum([1 for report in sample if safe(report)])


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()