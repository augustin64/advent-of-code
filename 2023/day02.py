#!/usr/bin/python3
"""
Jour 02 du défi Advent Of Code pour l'année 2023
"""

class Tirage():
    def __init__(self, tirage):
        self.red=0
        self.green=0
        self.blue=0

        sets = tirage.split(", ")
        for i in sets:
            count, color = i.split(" ")
            if color == "blue":
                self.blue = int(count)
            elif color == "red":
                self.red = int(count)
            elif color == "green":
                self.green = int(count)

    def __repr__(self):
        return f"r{self.red}g{self.green}b{self.blue}"


def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day02.txt', 'r') as f:
        sample = f.read().split('\n')
    sample = [ i.split(": ")[1] for i in sample if i != '' ]
    return sample

def parse_tirage(tirage):
    tirage.split(", ")

def parse_input(sample):
    return [
        [Tirage(j) for j in i.split("; ")]
        for i in sample
    ]

def game_possible(game, red=12, green=13, blue=14):
    for tirage in game:
        if tirage.red > red or tirage.green > green or tirage.blue > blue:
            return False
    return True

def games_possible(sample, red=12, green=13, blue=14):
    possible = []
    for i in range(len(sample)):
        if game_possible(sample[i], red=red, green=green, blue=blue):
            possible.append(i+1)
    return possible



def part1(sample):
    """Partie 1 du défi"""
    sample = parse_input(sample)
    return sum(games_possible(sample))


def minimal_set(game):
    t = Tirage("green 0")
    for tirage in game:
        t.red = max(t.red, tirage.red)
        t.green = max(t.green, tirage.green)
        t.blue = max(t.blue, tirage.blue)
    return t

def power(game):
    t = minimal_set(game)
    return t.red * t.green * t.blue

def powers(sample):
    return [power(game) for game in sample]

def part2(sample):
    """Partie 2 du défi"""
    sample = parse_input(sample)
    return sum(powers(sample))


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()