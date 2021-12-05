#!/usr/bin/python3
"""
Jour 05 du défi Advent Of Code pour l'année 2021
"""

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day05.txt', 'r') as file:
        sample = file.read().split('\n')
    sample = [ i for i in sample if i != '' ]
    parsed_sample = []
    for i in sample:
        elem1, elem2 = i.split(' -> ')
        elem11, elem12 = elem1.split(',')
        elem21, elem22 = elem2.split(',')
        parsed_sample.append(
            ((int(elem11), int(elem12)),(int(elem21), int(elem22)))
        )
    return parsed_sample

def filter1(sample):
    """filtre les données pour la première partie du challenge (ligne verticales et horizontales)"""
    filtered_sample = []
    for i in sample:
        if i[0][0] == i[1][0] or i[0][1] == i[1][1]:
            filtered_sample.append(i)
    return filtered_sample

def filter2(sample):
    """filtre les données pour la seconde partie du challenge (lignes à 45°)"""
    filtered_sample = filter1(sample)
    for i in sample:
        if abs(i[0][0]-i[1][0]) == abs(i[0][1]-i[1][1]):
            filtered_sample.append(i)
    return filtered_sample

def dimensions(sample):
    """renvoie les dimensions nécessaires pour la création du canvas"""
    min_x = min(min([i[0][0] for i in sample]), min([i[1][0] for i in sample]))
    max_x = max(max([i[0][0] for i in sample]), max([i[1][0] for i in sample]))
    min_y = min(min([i[0][1] for i in sample]), min([i[1][1] for i in sample]))
    max_y = max(max([i[0][1] for i in sample]), max([i[1][1] for i in sample]))
    return ((min_x, max_x+2), (min_y, max_y+2))

def add_line(coordinates, canvas):
    """rajoute une ligne à l'espace de travail"""
    (x_cord1, y_cord1), (x_cord2, y_cord2) = coordinates
    if x_cord1 == x_cord2:
        if y_cord1 > y_cord2:
            y_cord1, y_cord2 = y_cord2, y_cord1
        for i in range(y_cord1, y_cord2+1):
            canvas[x_cord1][i] += 1
    elif y_cord1 == y_cord2:
        if x_cord1 > x_cord2:
            x_cord1, x_cord2 = x_cord2, x_cord1
        for i in range(x_cord1, x_cord2+1):
            canvas[i][y_cord1] += 1
    else:
        if x_cord1 > x_cord2:
            (x_cord1, y_cord1), (x_cord2, y_cord2) = (x_cord2, y_cord2), (x_cord1, y_cord1)
        for i in range(x_cord2-x_cord1+1):
            if y_cord1 > y_cord2:
                canvas[x_cord1+i][y_cord1-i] += 1
            else:
                canvas[x_cord1+i][y_cord1+i] += 1
    return canvas

def count_overlaps(canvas):
    """compte le nombre de points où deux lignes minimum se chevauchent"""
    cpt = 0
    for i in canvas:
        for j in i:
            if j > 1:
                cpt += 1
    return cpt

def print_canvas(canvas):
    """Affiche le canvas"""
    for i, _ in enumerate(canvas[0]):
        text = ""
        for j, _ in enumerate(canvas):
            k = canvas[j][i]
            if k==0:
                text += "."
            else:
                text += str(k)
        print(text)

def part1(sample):
    """Partie 1 du défi"""
    fsample = filter1(sample)
    (_, max_x), (_, max_y) = dimensions(sample)
    canvas = [[0 for i in range(max_x)] for j in range(max_y)]
    for i in fsample:
        canvas = add_line(i, canvas)
    return count_overlaps(canvas)

def part2(sample):
    """Partie 2 du défi"""
    fsample = filter2(sample)
    (_, max_x), (_, max_y) = dimensions(sample)
    canvas = [[0 for i in range(max_x)] for j in range(max_y)]
    for i in fsample:
        canvas = add_line(i, canvas)
    return count_overlaps(canvas)


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")
