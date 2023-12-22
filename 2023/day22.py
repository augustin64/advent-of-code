#!/usr/bin/python3
"""
Jour 22 du défi Advent Of Code pour l'année 2023
"""
import os
import string
import random

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    filename = os.path.join(os.path.dirname(__file__ ), "inputs", "day22.txt")
    with open(filename, 'r') as f:
        sample = f.read().split('\n')
    sample = [ i for i in sample if i != '' ]
    return sample

def copy_bricks(bricks):
    return [b.copy() for b in bricks]

class Brick:
    def __init__(self, text):
        coords = text.split("~")
        coords = (coords[0].split(','), coords[1].split(','))

        self.x0 = int(coords[0][0])
        self.y0 = int(coords[0][1])
        self.z0 = int(coords[0][2])

        self.x1 = int(coords[1][0])
        self.y1 = int(coords[1][1])
        self.z1 = int(coords[1][2])

        self.label = random.choice(string.ascii_letters)
        self.text = text

    def __repr__(self):
        return f"[{self.label}]{self.x0},{self.y0},{self.z0}~{self.x1},{self.y1},{self.z1}"
        #return self.text+f"[{self.label}] [h:{self.z0}]"

    def supported_by(self, brick):
        def intersect(interval1, interval2):
            if interval2[0] > interval1[1] or interval1[0] > interval2[1]:
                return None
            new_min = max(interval1[0], interval2[0])
            new_max = min(interval1[1], interval2[1])
            return [new_min, new_max]

        if brick.z1 == self.z0-1:
            if intersect([self.x0, self.x1], [brick.x0, brick.x1]) is not None \
                and intersect([self.y0, self.y1], [brick.y0, brick.y1]) is not None:
                return True
        return False

    def can_fall(self, bricks):
        if self.z0 == 1:
            return False
        for brick in bricks:
            if brick != self and self.supported_by(brick):
                return False
        return True

    def copy(self):
        # Assuming your class has a constructor that accepts the same parameters
        copie = Brick(f"{self.x0},{self.y0},{self.z0}~{self.x1},{self.y1},{self.z1}")
        copie.label = self.label
        return copie

def intersect(interval1, interval2):
    if interval2[0] > interval1[1] or interval1[0] > interval2[1]:
        return None
    new_min = max(interval1[0], interval2[0])
    new_max = min(interval1[1], interval2[1])
    return [new_min, new_max]


def print_pile(bricks):
    def occupied(x, z):
        for b in bricks:
            if b.x0 <= x and x <= b.x1 and b.z0 <= z and z <= b.z1:
                return b
        return False

    for z in reversed(range(max((b.z1 for b in bricks))+1)):
        for x in range(max((b.x1 for b in bricks))+1):
            occ = occupied(x, z)
            if occ:
                print(occ.label, end="")
            else:
                print(".", end="")
        print()


def fall(bricks, count="z"):
    fallen = 0
    has_fallen = False
    bricks.sort(key=lambda b: b.z1)
    for brick in bricks:
        has_fallen = False
        while brick.can_fall(bricks):
            if count == "z":
                fallen += 1
            
            has_fallen = True
            brick.z0 -= 1
            brick.z1 -= 1
        
        if count != "z" and has_fallen:
            fallen += 1

    return fallen

def is_stable(_bricks):
    for b in _bricks:
        if b.can_fall(_bricks):
            return False
    return True

def count_disintegrable(bricks):
    count = 0
    bricks_c = copy_bricks(bricks)
    for i in range(len(bricks_c)):
        del bricks[i]

        if is_stable(bricks):
            count += 1

        bricks = copy_bricks(bricks_c)
    return count

def count_chain(bricks):
    count = 0
    bricks_c = copy_bricks(bricks)
    for i in range(len(bricks_c)):
        del bricks[i]
        b = bricks_c[i]

        cur = fall(bricks, count="count")
        count += cur
        #print("==========", b, cur)

        bricks = copy_bricks(bricks_c)
    return count



def part1(sample):
    """Partie 1 du défi"""
    bricks = [Brick(i) for i in sample]

    fall(bricks)
    assert is_stable(bricks)
    return count_disintegrable(bricks)

def part2(sample):
    """Partie 2 du défi"""
    bricks = [Brick(i) for i in sample]

    #print_pile(bricks)
    fall(bricks)
    #print_pile(bricks)

    assert is_stable(bricks)
    return count_chain(bricks)


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()