#!/usr/bin/python3
"""
Jour 18 du défi Advent Of Code pour l'année 2022
"""
import copy

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day18.txt', 'r') as f:
    #with open('test.txt', 'r') as f:
        sample = f.read().split('\n')
    sample = [ (int(i.split(",")[0]), int(i.split(",")[1]), int(i.split(",")[2])) for i in sample if i != '' ]
    return sample

def nb_voisins(cube, sample):
    vois = 0
    if (cube[0]-1, cube[1], cube[2]) in sample:
        vois += 1
    if (cube[0]+1, cube[1], cube[2]) in sample:
        vois += 1
    if (cube[0], cube[1]-1, cube[2]) in sample:
        vois += 1
    if (cube[0], cube[1]+1, cube[2]) in sample:
        vois += 1
    if (cube[0], cube[1], cube[2]-1) in sample:
        vois += 1
    if (cube[0], cube[1], cube[2]+1) in sample:
        vois += 1

    return vois
         

def nb_voisins2(cube, sample, carte, num):
    vois = 0
    x, y, z = cube
    if (x-1, y, z) in sample and carte[x-1][y][z] == num:
        vois += 1
    if (x+1, y, z) in sample and carte[x+1][y][z] == num:
        vois += 1
    if (x, y-1, z) in sample and carte[x][y-1][z] == num:
        vois += 1
    if (x, y+1, z) in sample and carte[x][y+1][z] == num:
        vois += 1
    if (x, y, z-1) in sample and carte[x][y][z-1] == num:
        vois += 1
    if (x, y, z+1) in sample and carte[x][y][z+1] == num:
        vois += 1

    return vois


def part1(sample):
    """Partie 1 du défi"""
    sides = 6*len(sample)
    for cube in sample:
        sides -= nb_voisins(cube, sample)
    return sides



def print_cubes(sample, carte=None):
    min_x, max_x = 0, max([i[0] for i in sample])+2
    min_y, max_y = 0, max([i[1] for i in sample])+2
    min_z, max_z = 0, max([i[2] for i in sample])+2

    for z in range(min_z, max_z):
        print(f"\n--- Couche {z} ---\n")
        for y in range(min_x, max_x):
            for x in range(min_x, max_x):
                if carte is not None and carte[x][y][z] == 2:
                    print("%", end="")
                elif (x, y, z) in sample:
                    print("#", end="")
                elif carte is not None and carte[x][y][z] == 1:
                    print('.', end="")
                else:
                    print(" ", end="")
            print()


def init_propagation(carte):
    for x in range(len(carte)):
        for y in range(len(carte[0])):
            for z in range(len(carte[0][0])):
                if x == 0 or y == 0 or z == 0 or x == len(carte)-1 or y == len(carte[0])-1 or z == len(carte[0][0])-1:
                    carte[x][y][z] = 1


def propagation(cart, sample):
    carte = copy.deepcopy(cart)
    modif = False
    for x in range(len(carte)):
        for y in range(len(carte[0])):
            for z in range(len(carte[0][0])):
                bon = False
                if not(x == 0 or y == 0 or z == 0 or x == len(carte)-1 or y == len(carte[0])-1 or z == len(carte[0][0])-1 or cart[x][y][z] != 0):
                    if cart[x-1][y][z]==1:
                        bon = True
                    elif cart[x+1][y][z]==1:
                        bon = True
                    elif cart[x][y+1][z]==1:
                        bon = True
                    elif cart[x][y-1][z]==1:
                        bon = True
                    elif cart[x][y][z+1]==1:
                        bon = True
                    elif cart[x][y][z+1]==1:
                        bon = True
                    if bon:
                        if (x, y, z) in sample:
                            carte[x][y][z] = 2
                        else:
                            carte[x][y][z] = 1
                        modif = True
    return modif, carte


def part2(sample):
    """Partie 2 du défi, simule l'eau qui se propage"""
    min_x, max_x = 0, max([i[0] for i in sample])+2
    min_y, max_y = 0, max([i[1] for i in sample])+2
    min_z, max_z = 0, max([i[2] for i in sample])+2
    carte = [[[0 for z in range(min_z, max_z)] for y in range(min_y, max_y)] for x in range(min_x, max_x)]

    init_propagation(carte)
    test, carte = propagation(carte, sample)
    while(test):
        test, carte = propagation(carte, sample)
        None

    sides = part1(sample)
    for x in range(len(carte)):
        for y in range(len(carte[0])):
            for z in range(len(carte[0][0])):
                if carte[x][y][z] == 0:
                    sides -= nb_voisins2((x, y, z), sample, carte, 2)

    return sides



def is_exterior(cube, sample):
    if nb_voisins(cube, sample) == 6:
        return False
    if cube[0] == min([i[0] for i in sample if (i[1], i[2])==(cube[1], cube[2])]):
        return True
    if cube[0] == max([i[0] for i in sample if (i[1], i[2])==(cube[1], cube[2])]):
        return True
    if cube[1] == min([i[1] for i in sample if (i[0], i[2])==(cube[0], cube[2])]):
        return True
    if cube[1] == max([i[1] for i in sample if (i[0], i[2])==(cube[0], cube[2])]):
        return True
    if cube[2] == min([i[2] for i in sample if (i[0], i[1])==(cube[0], cube[1])]):
        return True
    if cube[2] == max([i[2] for i in sample if (i[0], i[1])==(cube[0], cube[1])]):
        return True

    return False

def part2_old(sample):
    """Partie 2 du défi"""
    """Ne regarde que les extrema, omet des résultats"""
    sides = 6*len(sample)
    for cube in sample:
        if not is_exterior(cube, sample):
            sides -= 6
        else:
            sides -= nb_voisins(cube, sample)
    return sides


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()