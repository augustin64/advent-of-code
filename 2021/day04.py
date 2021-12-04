#!/usr/bin/python3
"""
Jour 04 du défi Advent Of Code pour l'année 2021
"""

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day04.txt', 'r') as file:
        sample = file.read().split('\n\n')
    nums = [int(i) for i in sample[0].split(',')]
    grids = [[[(int(k),False) for k in j.split(' ') if k!=''] for j in i.split('\n') if j!=''] for i in sample[1:]]
    return nums, grids

def calc_score(grid):
    """Calcule le score d'une grille de bingo validée"""
    score = 0
    for _, ligne in enumerate(grid):
        for _, num in enumerate(ligne):
            if not num[1]:
                score += num[0]
    return score

def rotate_grid(grid):
    """Fait pivoter la grille en échangeant les indices i et j"""
    r_grid = [[] for i in grid[0]]
    for ligne in grid:
        for j, num in enumerate(ligne):
            r_grid[j].append(num)
    return r_grid

def is_valid(grid, rotated):
    """Determine si une grille de bingo est valide"""
    for ligne in grid:
        valid = True
        for num in ligne:
            if not num[1]:
                valid = False
                break
        if valid:
            return (True, calc_score(grid))
    if not rotated:
        return is_valid(rotate_grid(grid), True)
    return (False, 0)

def validate(grid, number):
    """Valide un numéro pour une grille"""
    for i, ligne in enumerate(grid):
        for j, num in enumerate(ligne):
            if num[0] == number:
                grid[i][j] = (num[0], True)
    return grid

def part1(sample):
    """Partie 1 du défi"""
    nums, grids = sample
    turn = 0
    while True:
        for i, grid in enumerate(grids):
            grids[i] = validate(grid, nums[turn])
        for grid in grids:
            valid, score = is_valid(grid, False)
            if valid:
                return score*nums[turn]
        turn += 1

def part2(sample):
    """Partie 2 du défi"""
    nums, grids = sample
    turn = 0
    grids = [(grid, False) for grid in grids]
    last_val = None
    while True:
        for i, (grid, valid) in enumerate(grids):
            grids[i] = (validate(grids[i][0], nums[turn]), grids[i][1])
        for i, (grid, valid) in enumerate(grids):
            if valid:
                pass
            else:
                validation, _ = is_valid(grid, False)
                if validation:
                    grids[i] = (grid, True)
                    last_val = i
        if False not in [i for _, i in grids]:
            return is_valid(grids[last_val][0], False)[1]*nums[turn]
        turn += 1

def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")
