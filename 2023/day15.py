#!/usr/bin/python3
"""
Jour 15 du défi Advent Of Code pour l'année 2023
"""
import os

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    filename = os.path.join(os.path.dirname(__file__ ), "inputs", "day15.txt")
    with open(filename, 'r') as f:
        sample = f.read().split('\n')
    sample = [ [j for j in i.split(",")] for i in sample if i != '' ][0]
    return sample

def hash(s):
    cur_val = 0
    for i in s:
        cur_val += ord(i)
        cur_val *= 17
        cur_val = cur_val % 256
    return cur_val

def print_boxes(boxes):
    print("===")
    for i in boxes.keys():
        if boxes[i] != []:
            print(f"Box {i}: ", end="")
            for a, b in boxes[i]:
                print(f"[{a}={b}] ", end="")
            print()

def part1(sample):
    """Partie 1 du défi"""
    return sum(hash(i) for i in sample)

def part2(sample):
    """Partie 2 du défi"""
    boxes = {i: [] for i in range(256)}
    for i in sample:
        if '=' in i:
            label = i.split("=")[0]
            box = hash(label)
            lens = int(i.split("=")[1])
            found = False
            for i in range(len(boxes[box])):
                if boxes[box][i][0] == label:
                    boxes[box][i] = (label, lens)
                    found = True
                    break
            if not found:
                boxes[box].append((label, lens))
        else:
            label = i.split("-")[0]
            box = hash(label)
            boxes[box] = [(a, b) for (a, b) in boxes[box] if a != label]

    print_boxes(boxes)
    return sum([sum([(1+i)*(1+j)*boxes[i][j][1] for j in range(len(boxes[i]))]) for i in boxes.keys()])


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()