#!/usr/bin/python3
"""
Jour 03 du défi Advent Of Code pour l'année 2023
"""

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day03.txt', 'r') as f:
        sample = f.read().split('\n')
    sample = [ i for i in sample if i != '' ]
    return sample

def get_numbers(sample):
    numbers = []
    cur_number = 0
    cur_number_start = -1
    for i in range(len(sample)):
        if (cur_number_start != -1):
            numbers.append((cur_number, i-1, cur_number_start, len(sample[0])))
            cur_number = 0
            cur_number_start = -1
        for j in range(len(sample[i])):
            if (sample[i][j] <= '9' and sample[i][j] >= '0'):
                if cur_number_start == -1:
                    cur_number_start = j
                cur_number = cur_number*10 + int(sample[i][j])
            elif cur_number_start != -1:
                numbers.append((cur_number, i, cur_number_start, j-1))
                cur_number = 0
                cur_number_start = -1
    return numbers

def is_symbol_adjacent(number, sample):
    for i in range(max(0, number[1]-1), min(number[1]+2, len(sample)-1)):
        for j in range(max(0, number[2]-1), min(len(sample[0])-1, number[3]+2)):
            if sample[i][j] != '.' and not (sample[i][j] <= '9' and sample[i][j] >= '0'):
                return True, (sample[i][j], i, j)
    return False, ('.', 0, 0)

def part1(sample):
    """Partie 1 du défi"""
    numbers = get_numbers(sample)
    not_adj = []
    for number in numbers:
        if is_symbol_adjacent(number, sample)[0]:
            not_adj.append(number[0])
    return sum(not_adj)



def part2(sample):
    """Partie 2 du défi"""
    numbers = get_numbers(sample)
    geared = {}
    for number in numbers:
        val, symb = is_symbol_adjacent(number, sample)
        if symb[0] == '*':
            if (symb[1], symb[2]) not in geared.keys():
                geared[(symb[1], symb[2])] = []
            geared[(symb[1], symb[2])].append(number[0])
            
    mults = []
    for key in geared.keys():
        if len(geared[key]) >= 2:
            mults.append(geared[key][0]*geared[key][1])
            
    return sum(mults)


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()