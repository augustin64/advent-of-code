#!/usr/bin/python3
"""
Jour 22 du défi Advent Of Code pour l'année 2022
    <!-- NE FONCTIONNE PAS --!>
"""

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day22.txt', 'r') as f:
        sample = f.read().split('\n\n')
    map = [ i for i in sample[0] if i != '' ]
    moves = []
    cur = 0
    for i in sample[1]:
        if i in ['R', 'L']:
            moves.append(({'R': 1, 'L': -1}[i], cur))
        else:
            cur = cur*10+int(i)

    return map, moves


def has_wall(map, pos):
    if pos[2] == 0:
        if map[pos[0]][pos[1]+1] == '#':
            return True



def move(map, pos, distance):
    for i in range(distance):
        if has_wall(map, pos):
            break



        
    return pos



def part1(sample):
    """Partie 1 du défi"""
    map, moves = sample
    pos = (0, min([i for i in range(len(sample[0])) if sample[0][i] == '.']), 0)
    for i in moves:
        pos = move(map, pos, i[1])
        pos = (pos[0], pos[1], (pos[2]+i[0])%4)
    return NotImplementedError

def part2(sample):
    """Partie 2 du défi"""
    return NotImplementedError


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()