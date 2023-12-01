#!/usr/bin/python3
"""
Jour 13 du défi Advent Of Code pour l'année 2022
"""
import functools

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day13.txt', 'r') as f:
        sample = f.read().split('\n\n')
    sample = [ [eval(j) for j in i.split('\n') if j != ''] for i in sample if i != '' ]
    return sample

def is_right_order(elem1, elem2):
    if type(elem1) == type(0) and type(elem2) == type(0): # two ints
        if elem1 == elem2:
            return None
        return elem1 < elem2

    if type(elem1) == type([]) and type(elem2) == type([]): # two lists
        if len(elem1) == 0:
            return True

        for i in range(len(elem1)):
            if i > len(elem2)-1:
                return False # Out

            order = is_right_order(elem1[i], elem2[i])
            if order is not None:
                return order

        return is_right_order(len(elem1), len(elem2))

    if type(elem1) == type(0) and type(elem2) == type([]):
        return is_right_order([elem1], elem2)

    if type(elem2) == type(0) and type(elem1) == type([]):
        return is_right_order(elem1, [elem2])




def part1(sample):
    """Partie 1 du défi"""
    somme = 0
    for i in range(len(sample)):
        order = is_right_order(sample[i][0], sample[i][1])
        if order is None:
            order = True
        if order:
            somme += i+1
    return somme

def part2(sample):
    """Partie 2 du défi"""
    n_sample = []
    for i in sample:
        for j in i:
            n_sample.append(j)
    n_sample.append([[2]])
    n_sample.append([[6]])
    def comparaison(x, y):
        order = is_right_order(x, y)
        if order is None:
            return 0
        if order:
            return 1
        return -1

    keys = functools.cmp_to_key(comparaison)
    n_sample = sorted(n_sample, key=keys)
    n_sample.reverse()

    tot = 1
    for ind in range(len(n_sample)):
        i = n_sample[ind]
        if len(i)==1 and isinstance(i[0], list) and len(i[0])==1 and i[0][0]==2:
            tot *= ind+1
        elif len(i)==1 and isinstance(i[0], list) and len(i[0])==1 and i[0][0]==6:
            tot *= ind+1
    return tot


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(read_sample())}")
    print(f"part2: {part2(read_sample())}")

if __name__ == "__main__":
    main()