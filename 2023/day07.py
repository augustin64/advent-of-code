#!/usr/bin/python3
"""
Jour 07 du défi Advent Of Code pour l'année 2023
"""
from functools import cmp_to_key


def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day07.txt', 'r') as f:
        sample = f.read().split('\n')
    sample = [ (i.split(" ")[0], i.split(" ")[1]) for i in sample if i != '' ]
    return sample

def handtype(hand):
    occurences = {}
    for elem in hand:
        if elem not in occurences.keys():
            occurences[elem] = 0
        occurences[elem] += 1
    match sorted([occurences[key] for key in occurences.keys()], reverse=True):
        case [1, 1, 1, 1, 1]: # High card
            return 1
        case [2, 1, 1, 1]: # One pair
            return 2
        case [2, 2, 1]: # Two pairs
            return 3
        case [3, 1, 1]: # Three of a kind
            return 4
        case [3, 2]: # Full house
            return 5
        case [4, 1]: # Four of a kind
            return 6
        case [5]: # Five of a kind
            return 6

def joker_handtype(hand):
    if 'J' in hand:
        best = handtype(hand)
        for c in 'AKQT98765432':
            best = max(best, handtype(hand.replace('J', c)))
        return best
    return handtype(hand)


card_ranks = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1
}
def match(h1, h2, ht=handtype):
    hand1, _ = h1
    hand2, _ = h2
    handtype1 = ht(hand1)
    handtype2 = ht(hand2)
    if (handtype1 > handtype2):
        return 1
    if (handtype2 > handtype1):
        return -1

    for i in range(len(hand1)):
        if hand1[i] != hand2[i]:
            if card_ranks[hand1[i]] > card_ranks[hand2[i]]:
                return 1
            return -1
    return 0


def part1(sample):
    """Partie 1 du défi"""
    sample_s = sorted(sample, key=cmp_to_key(match))
    return sum([(i+1)*int(sample_s[i][1]) for i in range(len(sample_s))])

def part2(sample):
    """Partie 2 du défi"""
    sample_s = sorted(sample, key=cmp_to_key(lambda x, y: match(x, y, ht=joker_handtype)))
    return sum([(i+1)*int(sample_s[i][1]) for i in range(len(sample_s))])


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()