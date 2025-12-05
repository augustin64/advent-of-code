#!/usr/bin/python3
"""
Jour 05 du défi Advent Of Code pour l'année 2025
"""
import os

def ra(i):
    a,b = i.split("-")
    return int(a), int(b)

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    filename = os.path.join(os.path.dirname(__file__ ), "inputs", "day05.txt")
    with open(filename, 'r') as f:
        sample = f.read().split("\n\n")
    sample = [ ra(i) for i in sample[0].split("\n") if i != '' ], [ int(i) for i in sample[1].split("\n") if i != '' ]
    return sample

def is_fresh(ranges, i):
    for a, b in ranges:
        if i >= a and i <= b:
            return True
    return False

def part1(sample):
    """Partie 1 du défi"""
    ranges, ids = sample
    count = 0
    for i in ids:
        if is_fresh(ranges, i):
            count += 1
    return count

def part2(sample):
    """Partie 2 du défi"""
    ranges,_ = sample
    ranges_d = {k:v for k,v in ranges}
    for a,b in ranges: # deduplicate beginnings
        ranges_d[a] = max(ranges_d[a], b)
    ranges = list(ranges_d.items())
    ranges = sorted(ranges, key=lambda x:x[0])

    segm = []
    cur_i = 0
    next_i = 0
    while next_i < len(ranges):
        cur_i = next_i
        next_i = cur_i+1
        cur_end = ranges[cur_i][1]
        for j in range(cur_i+1, len(ranges)):
            if ranges[cur_i][1] > ranges[j][1]:
                # skip next one
                next_i = j+1
                continue
            elif ranges[cur_i][1] >= ranges[j][0]:
                cur_end = ranges[j][0]-1 # stops just before the next one
                break
            else: # no intersection
                break
        segm.append((ranges[cur_i][0], cur_end))

    return sum([b-a+1 for (a,b) in segm])



def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()