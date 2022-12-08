#!/usr/bin/python3
"""
Jour 08 du défi Advent Of Code pour l'année 2022
"""

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day08.txt', 'r') as f:
        sample = f.read().split('\n')
    sample = [ [int(j) for j in i] for i in sample if i != '' ]
    return sample

def is_visible(sample, i, j):
    vis = True
    for k in range(len(sample[i])):
        if k != j and sample[i][j] <= sample[i][k]:
            vis = False
        if k == j and vis:
            return 1
        if k == j:
            vis = True
        if k > j and sample[i][j] <= sample[i][k]:
            vis = False
    if vis:
        return 1
    vis = True
    for k in range(len(sample)):
        if k != i and sample[i][j] <= sample[k][j]:
            vis = False
        if k == i and vis:
            return 1
        if k == i:
            vis = True
        if k > i and sample[i][j] <= sample[k][j]:
            vis = False
    if vis:
        return 1

    
    
def part1(sample):
    """Partie 1 du défi"""
    tot = 0
    for i in range(len(sample)):
        for j in range(len(sample[0])):
            if is_visible(sample, i, j):
                tot += 1
    return tot



def scenic_score(sample, i, j):
    left, right, up, down = j, len(sample[0])-j-1, i, len(sample)-i-1
    for k in range(1, j):
        if sample[i][k] >= sample[i][j]:
            left = j-k

    for k in range(1, len(sample[0])-j):
        if sample[i][len(sample[0])-k] >= sample[i][j]:
            right = len(sample[0])-j-k

    for k in range(1, i):
        if sample[k][j] >= sample[i][j]:
            up = i-k

    for k in range(1, len(sample)-i):
        if sample[len(sample)-k][j] >= sample[i][j]:
            down = len(sample)-i-k

    return left*right*up*down



def part2(sample):
    """Partie 2 du défi"""
    views = []
    for i in range(1, len(sample)-1): # Edges will be 0
        for j in range(1, len(sample[0])-1):
            views.append(scenic_score(sample, i, j))

    return max(views)


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()
