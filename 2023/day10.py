#!/usr/bin/python3
"""
Jour 10 du défi Advent Of Code pour l'année 2023
"""

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day10.txt', 'r') as f:
        sample = f.read().split('\n')
    sample = [ [j for j in i] for i in sample if i != '' ]
    return sample


directions = {
    "nw": "J",
    "ns": "|",
    "ne": "L",
    "ws": "7",
    "we": "-",
    "se": "F"
}

def find_S(sample):
    for i in range(len(sample)):
        for j in range(len(sample[0])):
            if sample[i][j] == 'S':
                return i, j
    raise NotImplementedError


def next_move(pos, sample, prev_move):
    match sample[pos[0]][pos[1]]:
        case '.':
            print("Out of circuit !", prev_move, pos)
            raise NotImplementedError
        case '|':
            return prev_move
        case '-':
            return prev_move
        case 'L':
            if prev_move == (1, 0):
                return (0, 1)
            elif prev_move == (0, -1):
                return (-1, 0)
            print("I am lost (0) !", prev_move, pos)
            raise NotImplementedError
        case 'J':
            if prev_move == (1, 0):
                return (0, -1)
            elif prev_move == (0, 1):
                return (-1, 0)
            print("I am lost (1) !", prev_move, pos)
            raise NotImplementedError
        case '7':
            if prev_move == (-1, 0):
                return (0, -1)
            elif prev_move == (0, 1):
                return (1, 0)
            print("I am lost (2) !", prev_move, pos)
            raise NotImplementedError
        case 'F':
            if prev_move == (-1, 0):
                return (0, 1)
            elif prev_move == (0, -1):
                return (1, 0)
            print("I am lost (3) !", prev_move, pos)
            raise NotImplementedError
        case 'S':
            if pos[0] > 0 and (sample[pos[0]-1][pos[1]] in ['|', 'F', '7']): # Up
                return (-1, 0)
            if pos[1] > 0 and (sample[pos[0]][pos[1]-1] in ['-', 'L', 'F']): # Left
                return (0, -1)
            if pos[0] < len(sample) and (sample[pos[0]+1][pos[1]] in ['|', 'L', 'J']): # Down
                return (1, 0)
            if pos[1] < len(sample[0]) and (sample[pos[0]][pos[1]+1] in ['-', '7', 'J']): # Right
                return (0, 1)
    print("I am lost (4) !", prev_move, pos)
    raise NotImplementedError
            

def find_circuit(starting_point, sample):
    elems = []
    pos = starting_point
    prev_move = None
    while pos not in elems:
        elems.append(pos)
        prev_move = next_move(pos, sample, prev_move)
        pos = (pos[0] + prev_move[0], pos[1] + prev_move[1])

    return elems


def simplify(sample, circuit):
    for i in range(len(sample)):
        for j in range(len(sample[0])):
            if (i, j) not in circuit:
                sample[i][j] = '.'
    return sample


def find_enclosed(sample):
    down = ['|', '7', 'F']
    enclosed = []

    for i in range(len(sample)):
        up = False
        for j in range(len(sample[0])):
            if sample[i][j] in down:
                up = not up
            if up and sample[i][j] == '.':
                enclosed.append((i, j))

    return enclosed


def find_s_type(sample, pos):
    it = []
    if pos[0] > 0 and (sample[pos[0]-1][pos[1]] in ['|', 'F', '7']): # Up
        it.append('n')
    if pos[1] > 0 and (sample[pos[0]][pos[1]-1] in ['-', 'L', 'F']): # Left
        it.append('w')
    if pos[0] < len(sample) and (sample[pos[0]+1][pos[1]] in ['|', 'L', 'J']): # Down
        it.append('s')
    if pos[1] < len(sample[0]) and (sample[pos[0]][pos[1]+1] in ['-', '7', 'J']): # Right
        it.append('e')

    return directions[it[0]+it[1]]


def part1(sample):
    """Partie 1 du défi"""
    pos_S = find_S(sample)
    circuit = find_circuit(pos_S, sample)
    
    return int(len(circuit)/2)


def part2(sample):
    """Partie 2 du défi"""
    pos_S = find_S(sample)
    circuit = find_circuit(pos_S, sample)

    S_type = find_s_type(sample, pos_S)
    sample[pos_S[0]][pos_S[1]] = S_type

    sample2 = simplify(sample, circuit)
    enclosed = find_enclosed(sample2)

    return len(enclosed)


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()