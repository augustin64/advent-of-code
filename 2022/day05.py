#!/usr/bin/python3
"""
Jour 05 du défi Advent Of Code pour l'année 2022
"""

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day05.txt', 'r') as f:
        sample = f.read().split('\n\n')

    base = [[] for _ in range(int(len(sample[0][:-1].split("\n")[0])/4)+1)]
    for line in sample[0].split("\n"):
        for j in range(0, len(line) -1, 4):
            if line[j+1] != " ":
                base[int(j/4)].append(line[j+1])

    for i in base:
        i.reverse()

    moves = [ (int(i.split(" ")[1]), int(i.split(" ")[3]), int(i.split(" ")[5])) for i in sample[1].split("\n") if i != '' ]
    return (base, moves)

def move1(nb, init, fin, base):
    sp = base[init][-nb:]
    base[init] = base[init][:-nb]
    sp.reverse()
    for i in sp:
        base[fin].append(i)
    return base

def part1(sample):
    """Partie 1 du défi"""
    base, moves = sample
    for (number, init, fin) in moves:
        base = move1(number, init-1, fin-1, base)

    text = ""
    for i in base:
        text += i[-1]

    return text

def move2(nb, init, fin, base):
    sp = base[init][-nb:]
    base[init] = base[init][:-nb]
    for i in sp:
        base[fin].append(i)
    return base

def part2(sample):
    """Partie 1 du défi"""
    base, moves = sample
    for (number, init, fin) in moves:
        base = move2(number, init-1, fin-1, base)

    text = ""
    for i in base:
        text += i[-1]

    return text


def main():
    """Fonction principale"""
    print(f"part1: {part1(read_sample())}")
    print(f"part2: {part2(read_sample())}")

if __name__ == "__main__":
    main()