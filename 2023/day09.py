#!/usr/bin/python3
"""
Jour 09 du défi Advent Of Code pour l'année 2023
"""

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day09.txt', 'r') as f:
        sample = f.read().split('\n')
    sample = [ [int(j) for j in i.split()] for i in sample if i != '' ]
    return sample


def differences(seq):
    return [seq[i+1]-seq[i] for i in range(len(seq)-1)]

def null_list(seq):
    return False not in [i==0 for i in seq]

def extrapolate(seq, rev=False):
    if rev:
        seq = list(reversed(seq))
        
    seqs = [seq]
    while not null_list(seqs[-1]):
        seqs.append(differences(seqs[-1]))

    seqs[-1].append(0)
    for i in range(len(seqs)-1):
        seq = seqs[len(seqs)-2-i]
        prev = seqs[len(seqs)-i-1]
        seqs[len(seqs)-2-i].append(seq[-1]+prev[-1])

    return seqs

        


def part1(sample):
    """Partie 1 du défi"""
    return sum([extrapolate(seq, rev=False)[0][-1] for seq in sample])

def part2(sample):
    """Partie 2 du défi"""
    return sum([extrapolate(seq, rev=True)[0][-1] for seq in sample])


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()