#!/usr/bin/python3
"""
Jour 14 du défi Advent Of Code pour l'année 2022
"""

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day14.txt', 'r') as f:
        sample = f.read().split('\n')
    sample = [ [eval(j) for j in i.split(" -> ")] for i in sample if i != '' ]
    return [[(j[1], j[0]) for j in i] for i in sample]

def create_map(sample):
    maxi_0 = max([max([j[0] for j in i]) for i in sample])+1
    maxi_1 = max([max([j[1] for j in i]) for i in sample])+120

    map_ = [['.' for _ in range(maxi_1)] for _ in range(maxi_0)]
    for line in sample:
        for i in range(len(line)-1):
            if line[i][0] == line[i+1][0]:
                for j in range(min(line[i][1], line[i+1][1]), max(line[i][1], line[i+1][1])+1):
                    map_[line[i][0]][j] = '#'
            else:
                for j in range(min(line[i][0], line[i+1][0]), max(line[i][0], line[i+1][0])+1):
                    map_[j][line[i][1]] = '#'
    return map_

def print_map(map_, sample):
    mini = min([min([j[1] for j in i]) for i in sample])-15
    for i in range(len(map_)):
        print(i, "".join(map_[i][mini:]))

def make_sand_fall(map_, sand_source):
    sand_pos = sand_source
    while(sand_pos[0] >= 0 and sand_pos[0] < len(map_) and sand_pos[1] >= 0 and sand_pos[1] < len(map_[0])):
        try:
            if map_[sand_pos[0]+1][sand_pos[1]] == '.':
                sand_pos = (sand_pos[0]+1, sand_pos[1])
            elif map_[sand_pos[0]+1][sand_pos[1]-1] == '.':
                sand_pos = (sand_pos[0]+1, sand_pos[1]-1)
            elif map_[sand_pos[0]+1][sand_pos[1]+1] == '.':
                sand_pos = (sand_pos[0]+1, sand_pos[1]+1)
            else:
                map_[sand_pos[0]][sand_pos[1]] = 'o'
                return True
        except:
            return False

    return False


def part1(sample):
    """Partie 1 du défi"""
    map_ = create_map(sample)
    sand_source = (0,500)
    
    test = True
    while (test):
        test = make_sand_fall(map_, sand_source)
    
    #print_map(map_, sample)

    cpt = 0
    for k in map_:
        for j in k:
            if j == 'o':
                cpt += 1
    return cpt


def create_map2(sample):
    maxi_0 = max([max([j[0] for j in i]) for i in sample])+3
    maxi_1 = max([max([j[1] for j in i]) for i in sample])+1+maxi_0 # +maxi0 car put tomber sur les bords
    
    map_ = [['.' for _ in range(maxi_1)] for _ in range(maxi_0)]
    for line in sample:
        for i in range(len(line)-1):
            if line[i][0] == line[i+1][0]:
                for j in range(min(line[i][1], line[i+1][1]), max(line[i][1], line[i+1][1])+1):
                    map_[line[i][0]][j] = '#'
            else:
                for j in range(min(line[i][0], line[i+1][0]), max(line[i][0], line[i+1][0])+1):
                    map_[j][line[i][1]] = '#'

    for i in range(len(map_[0])):
        map_[-1][i] = '#'
    return map_


def part2(sample):
    """Partie 2 du défi"""
    map_ = create_map2(sample)
    
    sand_source = (0,500)
    test = True
    while (test and  map_[sand_source[0]][sand_source[1]] == '.'):
        test = make_sand_fall(map_, sand_source)
    
    print_map(map_, sample)

    cpt = 0
    for k in map_:
        for j in k:
            if j == 'o':
                cpt += 1
    return cpt


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")# 1409 too low # 1515 too high
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()