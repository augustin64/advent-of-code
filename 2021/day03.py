#!/usr/bin/python3
"""
Jour 03 du défi Advent Of Code pour l'année 2021
"""

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day03.txt', 'r') as file:
        sample = file.read().split('\n')
    sample = [ i for i in sample if i != '' ]
    return sample

def bin_to_dec(binary):
    """Converts a binary number to an int"""
    binary = str(binary)
    decimal = 0
    for i, _ in enumerate(binary):
        decimal = decimal*2
        decimal += int(binary[i])
    return decimal

def comm(sample, bit):
    """Determines the most common bit in an array"""
    mst_com = {"0":0, "1":0}
    for i in sample:
        mst_com[i[bit]] += 1
    if mst_com["0"] > mst_com["1"]:
        return ("0", "1")
    if mst_com["0"] < mst_com["1"]:
        return ("1", "0")
    return("1", "0")

def part1(sample):
    """Partie 1 du défi"""
    number1 = ""
    number2 = ""
    for i in range(len(sample[0])):
        a, b = comm(sample, i)
        number1 += a
        number2 += b
    gamma_rate = bin_to_dec(number1)
    epsilon_rate = bin_to_dec(number2)
    return gamma_rate*epsilon_rate


def loop(oxygen, co2, bit):
    """Fonction principale récursive du second défi"""
    if len(oxygen) == 1 and len(co2) == 1:
        return bin_to_dec(oxygen[0]) * bin_to_dec(co2[0])

    mst_com, _ = comm(oxygen, bit)
    _, lst_com = comm(co2, bit)

    if len(oxygen) > 1:
        oxygen = [ i for i in oxygen if i[bit] == mst_com ]
    if len(co2) > 1:
        co2 = [ i for i in co2 if i[bit] == lst_com ]

    return loop(oxygen, co2, bit+1)

def part2(sample):
    """Partie 2"""
    return loop(sample.copy(), sample.copy(), 0)


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")
