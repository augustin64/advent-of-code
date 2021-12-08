#!/usr/bin/python3
"""
Jour 07 du défi Advent Of Code pour l'année 2021
"""

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day07.txt', 'r') as f:
        sample = f.read().split(',')
    sample = [ int(i) for i in sample if i != '' ]
    return sample

def one_move_cost(n):
    """Renvoie le coût d'un mouvement dans la partie 2"""
    return int(n*(n+1)/2)

def cost_of(sample, position):
    """Renvoie le coût d'un mouvement de crabes pour la partie 1"""
    return sum([abs(position - i) for i in sample])

def part2_cost_of(sample,position):
    """Renvoie le coût d'un mouvement de crabes pour la partie 2"""
    return sum([one_move_cost(abs(position - i)) for i in sample])

def part1(sample):
    """Partie 1 du défi"""
    mini, maxi = min(sample), max(sample)
    cheapest = (mini, cost_of(sample, mini))
    for i in range(mini+1, maxi+1):
        cost = cost_of(sample, i)
        if cost < cheapest[1]:
            cheapest = (i, cost)

    return cheapest[1]

def part2(sample):
    """Partie 2 du défi"""
    mini, maxi = min(sample), max(sample)
    cheapest = (mini, part2_cost_of(sample, mini))
    for i in range(mini+1, maxi+1):
        cost = part2_cost_of(sample, i)
        if cost < cheapest[1]:
            cheapest = (i, cost)

    return cheapest[1]


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")
main()
