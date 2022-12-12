#!/usr/bin/python3
"""
Jour 10 du défi Advent Of Code pour l'année 2022
"""

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day10.txt', 'r') as f:
        sample = f.read().split('\n')
    sample = [ i for i in sample if i != '' ]
    return sample


def generate(sample):
    cursor = 0
    X_values = [1]
    X = 1

    for instr in sample:
        if instr.split(" ")[0] == "noop":
            X_values.append(X)
        else:
            X_values.append(X)
            X_values.append(X)
            X += int(instr.split(" ")[1])

    return X_values


def part1(sample):
    """Partie 1 du défi"""
    checks = [20, 60, 100, 140, 180, 220]
    X_values = generate(sample)

    return sum([X_values[i]*i for i in range(len(X_values)) if i in checks])

def part2(sample):
    """Partie 2 du défi"""
    checks = [20, 60, 100, 140, 180, 220]
    positions = [[' ' for _ in range(40)] for _ in range(6)]
    X_values = generate(sample)[1:]
    
    for i in range(6):
        for j in range(40):
            if j in [X_values[i*40+j]-1, X_values[i*40+j], X_values[i*40+j]+1]:
                positions[i][j] = '#'

    return ("\n"+"\n".join(["".join(positions[i]) for i in range(len(positions))]))


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()