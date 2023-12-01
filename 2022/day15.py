#!/usr/bin/python3
"""
Jour 15 du défi Advent Of Code pour l'année 2022
"""
from tqdm import tqdm

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day15.txt', 'r') as f:
        sample = f.read().split('\n')
    sample = [ i for i in sample if i != '' ]
    return sample


def parse_sample(sample):
    sensors = []
    for line in sample:
        spl = line.split(", ")
        tmp1 = int(spl[0].split("x=")[1])
        tmp2 = int(spl[1].split("y=")[1].split(":")[0])
        tmp3 = int(spl[1].split("x=")[1])
        tmp4 = int(spl[2].split("y=")[1].split(":")[0])
        sensors.append(((tmp1, tmp2), (tmp3, tmp4)))
    return sensors


def intersection(seg1, seg2):
    seg = []
    for line in seg1:
        added = False
        for line2 in seg2:
            if line[0] >= line2[0] and line[1] <= line2[1]:
                added = True
                seg.append(line)
                break
        if not added:
            for line2 in seg2:
                if line[0] <= line2[1]:
                    seg.append((max(line2[0], line[0]), min(line[1], line2[1])))
                elif line[1] >= line2[0]:
                    None#yet

    return seg

def overlapping_segment(a, b):
    x = max(a[0], b[0])
    y = min(a[1], b[1])
    return x,y


def find_overlaps(r, b):
    retVal = []
    ri = 0
    bi = 0
    while (ri < len(r)) and (bi < len(b)): 
        s = overlapping_segment(r[ri], b[bi])
        if s[0] < s[1]:
            retVal.append([ri, bi])
        if r[ri][1] == s[1]:
            ri += 1
        if b[bi][1] == s[1]:
            bi += bi + 1
    return retVal


def taille_seg(segment):
    taille = 0
    for i in segment:
        taille += i[1]-i[0]+1
    return taille

def manhattan(x, y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])

def create_map(sensors):
    maxi_x = max([x[0]+manhattan(x, y) for (x, y) in sensors])
    maxi_y = max([x[1]+manhattan(x, y) for (x, y) in sensors])
    
    map_ = [['.' for _ in range(maxi_y)] for _ in range(maxi_x)]
    for i in range(len(map_)):
        for j in range(len(map_[0])):
            for sensor in sensors:
                if manhattan(sensor[0], sensor[1]) > manhattan(sensor[0], (i, j)):
                    map_[i][j] = '#'

    return map_


def part1(sample):
    """Partie 1 du défi"""
    sensors = parse_sample(sample)

    maxi_y = max([x[1]+manhattan(x, y) for (x, y) in sensors])
    mini_y = min([x[1]-manhattan(x, y) for (x, y) in sensors])
    cpt = 0
    j = 10
    j=2000000
    seg = [(mini_y, maxi_y)]
    for sensor in sensors:
        d = manhattan(sensor[0], sensor[1])
        if d+sensor[0][0] >= j:
            a = sensor[0][0] - j + d
            print(seg)
            print([(mini_y, sensor[0][1]-a), (sensor[0][1]+a, maxi_y)])
            seg = find_overlaps(seg, [(mini_y, sensor[0][1]-a), (sensor[0][1]+a, maxi_y)])
            print("=>",seg)
        
        if sensor[0][0]-d <= j:
            a = -sensor[0][0] + j + d
            #print([(mini_y, sensor[0][1]-a), (sensor[0][1]+a, maxi_y)])
            seg = find_overlaps(seg, [(mini_y, sensor[0][1]-a), (sensor[0][1]+a, maxi_y)])

    print(seg, taille_seg(seg))
    taille = taille_seg(seg)


    """
    for i in range(mini_y, maxi_y):
        for sensor in sensors:
            if manhattan(sensor[0], sensor[1]) >= manhattan(sensor[0], (i, j)):
                if True not in [ a==i and b==j for ((_, _), (a, b)) in sensors ]:
                    cpt += 1
                    break
    """
    return (maxi_y-mini_y)-taille

def part2(sample):
    """Partie 2 du défi"""
    sensors = parse_sample(sample)

    maxi = 4000000
    #maxi = 20
    
    dists = {}
    for i in range(len(sensors)):
        dists[i] = manhattan(sensors[i][0], sensors[i][1])

    for i in tqdm(range(maxi)):
        for j in range(maxi):
            test = True
            for k in range(len(sensors)):
                if test:
                    if dists[k] >= manhattan(sensors[k][0], (i, j)):
                        test = False

            if test:
                return (i, j)
                    



def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(read_sample())}")

if __name__ == "__main__":
    main()