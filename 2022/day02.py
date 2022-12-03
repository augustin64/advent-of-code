#!/usr/bin/python3
"""
Jour 02 du défi Advent Of Code pour l'année 2022
"""

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day02.txt', 'r') as f:
        sample = f.read().split('\n')
    sample = [ i for i in sample if i != '' ]
    return sample

def score(text):
    fst = text.split(" ")[0]
    snd = text.split(" ")[1]
    choice = ord(snd)-87
    if ord(fst) == ord(snd)-23:
        return choice+3 # Nul
    perdants = [("A", "Z"), ("B", "X"), ("C", "Y")]
    if (fst, snd) in perdants:
        return choice # Défaite
    return choice+6 # Victoire
    

def part1(sample):
    """Partie 1 du défi"""
    return sum([score(i) for i in sample])

def score2(text):
    fst = text.split(" ")[0]
    snd = text.split(" ")[1]
    val = {
        "X": {"A":3, "B":1, "C":2},
        "Z": {"A":2, "B":3, "C":1},
    }
    if snd=="Y":
        return (ord(fst)-64) +3 #tie
    if snd=="X":
        return val["X"][fst]#Loss
    if snd=="Z":
        return val["Z"][fst]+6#Win


def part2(sample):
    """Partie 2 du défi"""
    return sum([score2(i) for i in sample])


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()