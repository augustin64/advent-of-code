#!/usr/bin/python3
"""
Jour 04 du défi Advent Of Code pour l'année 2023
"""
import os

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    filename = os.path.join(os.path.dirname(__file__ ), "inputs", "day04.txt")
    with open(filename, 'r') as f:
        sample = f.read().split('\n')
    sample = [ i for i in sample if i != '' ]
    return sample


def parse_card(text):
    text = text.split(": ")[1]
    p1, p2 = text.split(" | ")
    return ([int(i) for i in p1.split(" ") if i!=""], [int(i) for i in p2.split(" ") if i!=""])


def matching(card):
    winning = card[0]
    possessed = card[1]
    return sum([1 for i in possessed if i in winning])


def points(card):
    total = matching(card)
    if (total > 0):
        return 2**(total-1)
    return 0


def part1(sample):
    """Partie 1 du défi"""
    cards = [parse_card(i) for i in sample]
    return sum([points(card) for card in cards])

def part2(sample):
    """Partie 2 du défi"""
    cards = [parse_card(i) for i in sample]
    cards_d = {i: (1, cards[i]) for i in range(len(cards))}
    
    for key in cards_d.keys():
        count, card = cards_d[key]
        p = matching(card)
        if p > 0:
            for i in range(key+1, key+p+1):
                if (i in cards_d.keys()):
                    cards_d[i] = ( cards_d[i][0]+count, cards_d[i][1])
    
    return sum([cards_d[key][0] for key in cards_d.keys()])


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()