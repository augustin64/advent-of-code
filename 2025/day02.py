#!/usr/bin/python3
"""
Jour 02 du défi Advent Of Code pour l'année 2025
"""
import os
import math
import tqdm
import itertools

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    filename = os.path.join(os.path.dirname(__file__ ), "inputs", "day02.txt")
    with open(filename, 'r') as f:
        sample = f.read().split('\n')
    sample = [ i for i in sample if i != '' ]
    products = [list(map(int, a.split("-"))) for a in sample[0].split(",")]
    return products

def is_invalid(num):
    """
    Checks if a number is invalid in part 1
    eg, it follows (aa)
    """
    s = str(num)
    return s[:int(len(s)/2)] == s[int(len(s)/2):]

def part1(sample):
    """Partie 1 du défi"""
    invalids = set()
    for start, end in sample:
        row_inv = set()
        for i in range(0, int(1+math.log10(end))):
            # We just try numbers that are multiple of 1(00)*1
            # in the range of start-end
            invalid = 10**(i+1)+1
            s = start/invalid
            e = end/invalid
            for j in range(int(s), int(e)+1):
                num = j*invalid
                if num < start or num > end:
                    continue
                if not is_invalid(num):
                    continue
                row_inv.add(num)
        invalids = invalids | row_inv 
    return sum(invalids)


def is_invalid2(num):
    """
    Checks if a number is invalid in part 2
    eg it follows (a){2:}
    """
    s = str(num)
    for rep_size in range(1, len(s)): # répétitions de taille..
        if len(s) % rep_size != 0:
            continue

        rep = s[:rep_size]
        for part in range(int(len(s)/rep_size)):
            if rep != s[rep_size*part:rep_size*(part+1)]:
                break
        else:
            return True
    return False


def get_pows(s):
    """
    Returns an enumeration of 1, 10, 11, 100... until s
    (in fact, if log10(s)==3, until 1111)
    """
    r = itertools.product(*[(1, 0) for _ in range(int(math.log10(s))+1)])
    for res in r:
        val = sum([res[i]*10**i for i in range(len(res))])
        if val == 0:
            continue
        yield val


def part2(sample):
    """Partie 2 du défi"""
    invalids = set()
    for start, end in sample:
        row_inv = set()
        for invalid in get_pows(end):
            s = start/invalid
            e = end/invalid
            for j in range(int(s), int(e)+1):
                num = j*invalid
                if num < start or num > end:
                    continue
                if not is_invalid2(num):
                    continue
                row_inv.add(num)

        invalids = invalids | row_inv 
    return sum(invalids)



def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()