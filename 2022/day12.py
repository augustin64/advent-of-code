#!/usr/bin/python3
"""
Jour 12 du défi Advent Of Code pour l'année 2022
"""
import copy # pour deepcopy

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day12.txt', 'r') as f:
        sample = f.read().split('\n')
    sample = [ [j for j in i] for i in sample if i != '' ]
    return sample

def elevation(char):
    return ord(char) - ord('a')


def direction(sample, i, j):
    dirs = []
    if i > 0 :
        hdiff = (elevation(sample[i-1][j]) - elevation(sample[i][j]))
        if hdiff <= 1:
            dirs.append('up')
    if j > 0:
        hdiff = (elevation(sample[i][j-1]) - elevation(sample[i][j]))
        if hdiff <= 1:
            dirs.append('left')
    if i < len(sample)-1 :
        hdiff = (elevation(sample[i+1][j]) - elevation(sample[i][j]))
        if hdiff <= 1:
            dirs.append('down')
    if j < len(sample[0])-1:
        hdiff = (elevation(sample[i][j+1]) - elevation(sample[i][j]))
        if hdiff <= 1:
            dirs.append('right')

    if len(dirs)==0:
        return []
    return dirs

def better_height(moves, heights, i, j, sample):
    available = []
    if heights[i][j] != -1:
        available.append(heights[i][j])
    if i > 0 :
        if ('down' in moves[i-1][j] and heights[i-1][j] != -1):
            available.append(heights[i-1][j]+1)
    if j > 0:
        if ('right' in moves[i][j-1] and heights[i][j-1] != -1):
            available.append(heights[i][j-1]+1)
    if i < len(sample)-1 :
        if ('up' in moves[i+1][j] and heights[i+1][j] != -1):
            available.append(heights[i+1][j]+1)
    if j < len(sample[0])-1:
        if ('left' in moves[i][j+1] and heights[i][j+1] != -1):
            available.append(heights[i][j+1]+1)
    
    if len(available) == 0:
        return -1
    return min(available)


def update_heights(moves, heights, sample):
    changed = False
    heights_c = copy.deepcopy(heights)
    for i in range(len(sample)):
        for j in range(len(sample[0])):
            heights_c[i][j] = better_height(moves, heights, i, j, sample)
            changed = changed or (heights_c[i][j] != heights[i][j])

    return heights_c, changed

def print_val(sample, heights):
    """Afficher l'état actuel des chemins découverts"""
    for i in range(len(sample)):
        for j in range(len(sample[0])):
            if heights[i][j] != -1:
                print(f"\x1b[38;2;{heights[i][j]};{heights[i][j]};{heights[i][j]}m", end='')
            else:
                print("\x1b[38;2;0;0;0m", end='')
            print("#", end='')
        print("\033[0m")


def part1(sample):
    """Partie 1 du défi"""
    start = (-1, -1)
    end = (-1, -1)
    # Récupère le début et la fin
    for i in range(len(sample)):
        for j in range(len(sample[0])):
            if sample[i][j] == 'E':
                end = (i, j)
                sample[i][j] = 'z'
            elif sample[i][j] == 'S':
                start = (i, j)
                sample[i][j] = 'a'

    moves = [['.' for _ in range(len(sample[0]))] for _ in range(len(sample))]
    # Calcul des positions directement accessibles
    for i in range(len(sample)):
        for j in range(len(sample[0])):
            moves[i][j] = direction(sample, i, j)

    # Initialisation des hauteurs
    heights = [[-1 for _ in range(len(sample[0]))] for _ in range(len(sample))]
    heights[start[0]][start[1]] = 0

    steps = 0
    changed = True
    while heights[end[0]][end[1]] == -1 and changed:
        steps += 1
        heights, changed = update_heights(moves, heights, sample)

        #print_val(sample, heights)

    return heights[end[0]][end[1]]

def part2(sample):
    """Partie 2 du défi"""
    start = (-1, -1)
    end = (-1, -1)
    for i in range(len(sample)):
        for j in range(len(sample[0])):
            if sample[i][j] == 'E':
                end = (i, j)
                sample[i][j] = 'z'
            elif sample[i][j] == 'S':
                start = (i, j)
                sample[i][j] = 'a'

    moves = [['.' for _ in range(len(sample[0]))] for _ in range(len(sample))]
    for i in range(len(sample)):
        for j in range(len(sample[0])):
            moves[i][j] = direction(sample, i, j)

    # Chaque 'a' est maintenant un point de départ
    heights = [[-1 for _ in range(len(sample[0]))] for _ in range(len(sample))]
    for i in range(len(sample)):
        for j in range(len(sample[0])):
            if sample[i][j] == 'a':
                heights[i][j] = 0
    

    steps = 0
    changed = True
    while heights[end[0]][end[1]] == -1 and changed:
        steps += 1
        heights, changed = update_heights(moves, heights, sample)

        #print_val(sample, heights)

    return heights[end[0]][end[1]]


def main():
    """Fonction principale"""
    print(f"part1: {part1(read_sample())}")
    print(f"part2: {part2(read_sample())}")

if __name__ == "__main__":
    main()