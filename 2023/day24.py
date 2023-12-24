#!/usr/bin/python3
"""
Jour 24 du défi Advent Of Code pour l'année 2023
"""
import os
import z3

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    filename = os.path.join(os.path.dirname(__file__ ), "inputs", "day24.txt")
    with open(filename, 'r') as f:
        sample = f.read().split('\n')
    sample = [ i for i in sample if i != '' ]
    return sample

class Hailstone:
    def __init__(self, text):
        self.px = int(text.split(" @ ")[0].split(", ")[0])
        self.py = int(text.split(" @ ")[0].split(", ")[1])
        self.pz = int(text.split(" @ ")[0].split(", ")[2])

        self.dx = int(text.split(" @ ")[1].split(", ")[0])
        self.dy = int(text.split(" @ ")[1].split(", ")[1])
        self.dz = int(text.split(" @ ")[1].split(", ")[2])

    def __repr__(self):
        return f"{self.px}, {self.py}, {self.pz} @ {self.dx}, {self.dy}, {self.dz}"


def intersection(h1, h2):
    try:
        # ax+b
        # cx+d
        b, a = h1.py - (h1.px/h1.dx)*h1.dy, h1.dy/h1.dx
        d, c = h2.py - (h2.px/h2.dx)*h2.dy, h2.dy/h2.dx
        
        x =  (d - b) / (a - c)
        y = a*x+b

        if (x-h1.px)/h1.dx < 0:
            return None
        if (x-h2.px)/h2.dx < 0:
            return None
    except ZeroDivisionError:
        return None

    return x, y



def part1(sample, left=200000000000000, right=400000000000000):
    """Partie 1 du défi"""
    hailstones = [Hailstone(i) for i in sample]
    
    count = 0
    for i in range(len(hailstones)):
        for j in range(i):
            res = intersection(hailstones[i], hailstones[j])
            if res is not None:
                x, y = res
                if left <= x and x <= right and left <= y and y <= right:
                    count += 1

    return count

def part2(sample):
    """Partie 2 du défi"""
    hailstones = [Hailstone(i) for i in sample]

    px, py, pz, dx, dy, dz = z3.Ints("px py pz dx dy dz")
    collision = [z3.Int("t"+str(i)) for i in range(len(hailstones))]
    solver = z3.Solver()
    for i in range(len(hailstones)):
        h = hailstones[i]
        solver.add(px + dx*collision[i] == h.px + h.dx*collision[i])
        solver.add(py + dy*collision[i] == h.py + h.dy*collision[i])
        solver.add(pz + dz*collision[i] == h.pz + h.dz*collision[i])
    
    solver.check()


    return solver.model().evaluate(px + py + pz)


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()