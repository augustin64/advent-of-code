#!/usr/bin/python3
"""
Jour 09 du défi Advent Of Code pour l'année 2022
"""

directions = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day09.txt', 'r') as f:
        sample = f.read().split('\n')
    sample = [ (i[0], int(i.split(" ")[1])) for i in sample if i != '' ]
    return sample

def unique(liste):
    liste2 = []
    for i in liste:
        if i not in liste2:
            liste2.append(i)

    return liste2

def print_vis(visited,  vis_2, head=None):
    max_i = max(i[0] for i in vis_2)
    max_j = max(i[1] for i in vis_2)
    for i in range(max_i):
        for j in range(max_j):
            if head is not None and head[0]==i and head[1]==j:
                print('H', end='')
            if f"{i}:{j}" in visited:
                print('#', end='')
            else:
                print(".", end='')
        print()
    print()

def part1(sample):
    """Partie 1 du défi"""
    visited = ['0:0']
    vis_2 = [(0,0)]
    pos_h = (0, 0)
    pos_t = (0, 0)
    for line in sample:
        for i in range(line[1]):
            if line[0] == "L":
                pos_h = (pos_h[0]-1, pos_h[1])
            elif line[0] == "R":
                pos_h = (pos_h[0]+1, pos_h[1])
            elif line[0] == "U":
                pos_h = (pos_h[0], pos_h[1]+1)
            elif line[0] == "D":
                pos_h = (pos_h[0], pos_h[1]-1)
    
            dx = abs(pos_h[0]-pos_t[0])
            dy = abs(pos_h[1]-pos_t[1])
            if (dx+dy==2 and dy != 1):
                if line[0] == "L":
                    pos_t = (pos_t[0]-1, pos_t[1])
                elif line[0] == "R":
                    pos_t = (pos_t[0]+1, pos_t[1])
                elif line[0] == "U":
                    pos_t = (pos_t[0], pos_t[1]+1)
                elif line[0] == "D":
                    pos_t = (pos_t[0], pos_t[1]-1)
            elif (dx==2 and dy==1):
                if line[0] == "L":
                    pos_t = (pos_t[0]-1, pos_t[1])
                elif line[0] == "R":
                    pos_t = (pos_t[0]+1, pos_t[1])
                elif line[0] == "U":
                    pos_t = (pos_t[0], pos_t[1]+1)
                elif line[0] == "D":
                    pos_t = (pos_t[0], pos_t[1]-1)
                pos_t = (pos_t[0], pos_h[1])
            elif (dx==1 and dy==2):
                if line[0] == "L":
                    pos_t = (pos_t[0]-1, pos_t[1])
                elif line[0] == "R":
                    pos_t = (pos_t[0]+1, pos_t[1])
                elif line[0] == "U":
                    pos_t = (pos_t[0], pos_t[1]+1)
                elif line[0] == "D":
                    pos_t = (pos_t[0], pos_t[1]-1)
                pos_t = (pos_h[0], pos_t[1])

            visited.append(f"{pos_t[0]}:{pos_t[1]}")
            vis_2.append(pos_t)

    return len(unique(visited))


def follow(pos, j):
    a = pos[j-1]
    b = pos[j]

    dx = abs(a[0]-b[0])
    dy = abs(a[1]-b[1])

    if dy <= 1 and dx <= 1:
        return # Rope already touching

    if dx == 0:
        if a[1] > b[1]:
            pos[j] = (b[0], b[1]+1)
            return
        pos[j] = (b[0], b[1]-1)
        return
    if dy == 0:
        if a[0] > b[0]:
            pos[j] = (b[0]+1, b[1])
            return
        pos[j] = (b[0]-1, b[1])
        return
    
    if a[0] > b[0] and a[1] > b[1]:
        pos[j] = (b[0] + 1, b[1] + 1)
        return
    if a[0] > b[0] and a[1] < b[1]:
        pos[j] = (b[0] + 1, b[1] - 1)
        return
    if a[0] < b[0] and a[1] > b[1]:
        pos[j] = (b[0] - 1, b[1] + 1)
        return
    if a[0] < b[0] and a[1] < b[1]:
        pos[j] = (b[0] - 1, b[1] - 1)
        return

    print(f"Situation non prise en compte: head:{a}, tail:{b}")




def part2(sample):
    """Partie 2 du défi"""
    visited = ['0:0']
    tail = 10
    positions = [(0, 0) for i in range(tail)]
    
    for line in sample:
        for i in range(line[1]):
            positions[0] = (positions[0][0]+directions[line[0]][0], positions[0][1]+directions[line[0]][1])

            for j in range(1, tail):
                follow(positions, j)

            if f"{positions[tail-1][0]}:{positions[tail-1][1]}" not in visited:
                visited.append(f"{positions[tail-1][0]}:{positions[tail-1][1]}")

    return len(visited)


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()