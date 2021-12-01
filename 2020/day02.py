#!/usr/bin/python3
"""
Jour 02 du défi Advent Of Code pour l'année 2020
"""

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day02.txt', 'r') as f:
        sample = f.read().split('\n')
    sample = [i for i in sample if i != '']
    return sample

def xor(a, b):
    return (a or b) and not (a and b)

def is_valid_part1(line):
    crit, password = line.split(":")
    number, letter = crit.split(" ")
    mini, maxi = number.split("-")
    return int(mini) <= password.count(letter) <= int(maxi)

def is_valid_part2(line):
    crit, password = line.split(":")
    number, letter = crit.split(" ")
    pos1, pos2 = number.split("-")
    password = password[1:]
    return xor(password[int(pos1)-1] == letter, password[int(pos2)-1] == letter)

def part1(sample):
    """Partie 1 du défi"""
    count = 0
    for password in sample:
        if is_valid_part1(password):
            count += 1
    return count

def part2(sample):
    """Partie 2 du défi"""
    count = 0
    for password in sample:
        if is_valid_part2(password):
            count += 1
    return count


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")
