#!/usr/bin/python3
"""
Jour 12 du défi Advent Of Code pour l'année 2023
"""
import os
from functools import cache, wraps
from time import time

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    filename = os.path.join(os.path.dirname(__file__ ), "inputs", "day12.txt")
    with open(filename, 'r') as f:
        sample = f.read().split('\n')
    sample = [ i for i in sample if i != '' ]
    return sample


def parse_sample(sample):
    springs = []
    counts = []
    for i in range(len(sample)):
        springs.append(sample[i].split(" ")[0])
        counts.append([int(i) for i in sample[i].split(" ")[1].split(",")])
    return springs, counts


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('> %s: %2.4f sec' % \
          (f.__name__, te-ts))
        return result
    return wrap


def nb_poss(spring, count):
    def check_new_elem(elem, size, count):
        if size > len(count):
            return False
        if elem != count[size-1]:
            return False
        return True

    @cache
    def nb_poss_rec(actual_count_size, cur, pos, first):
        """
            actual_count_size: already added elements
            cur: current number of # in the spring pos
            pos: current position in the spring
            first: first elem of the upcoming spring
        """
        # While loop for first elem
        if pos < len(spring) and first != '?':
            if first == '.':
                if cur > 0:
                    actual_count_size += 1
                    if not check_new_elem(cur, actual_count_size, count):
                        return 0
                    cur = 0
            elif first == '#':
                cur += 1
            pos += 1

        # Exactly the same loop for the other elems
        while pos < len(spring) and spring[pos] != '?':
            if spring[pos] == '.':
                if cur > 0:
                    actual_count_size += 1
                    if not check_new_elem(cur, actual_count_size, count):
                        return 0
                    cur = 0
            elif spring[pos] == '#':
                cur += 1
            pos += 1

        # spring ends with # ?
        if pos == len(spring) and cur > 0:
            actual_count_size += 1
            if not check_new_elem(cur, actual_count_size, count):
                return 0

        # End of spring ?
        if pos >= len(spring):
            if len(count) == actual_count_size:
                return 1
            return 0
        
        # Debugging
        if spring[pos] != '?':
            print("weird", spring, count, actual_count_size, pos, spring[pos], len(spring))
            return

        # Recursive calls
        if spring[pos] == '?':
            if cur > 0:
                if len(count) > actual_count_size:
                    if cur == count[actual_count_size]:
                        return nb_poss_rec(actual_count_size, cur, pos, '.') # break the #### with a .
                    elif cur < count[actual_count_size]:
                        return nb_poss_rec(actual_count_size, cur, pos, '#') # continue with #
                    else:
                        return 0 # not possible
            return nb_poss_rec(actual_count_size, cur, pos, '.') + nb_poss_rec(actual_count_size, cur, pos, '#')

    return nb_poss_rec(0, 0, 0, spring[0])


def unfold(springs, counts):
    for i in range(len(springs)):
        springs[i] = '?'.join([springs[i]]*5)
        counts[i] = counts[i]*5


@timing
def part1(sample):
    """Partie 1 du défi"""
    springs, counts = parse_sample(sample)
    possibilities = []
    for i in range(len(springs)):
        possibilities.append(nb_poss(springs[i], counts[i]))
        
    return sum(possibilities)


@timing
def part2(sample):
    """Partie 2 du défi"""
    springs, counts = parse_sample(sample)
    unfold(springs, counts)
    
    possibilities = []
    for i in range(len(springs)):
        possibilities.append(nb_poss(springs[i], counts[i]))
        
    return sum(possibilities)


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()