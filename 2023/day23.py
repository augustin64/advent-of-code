#!/usr/bin/python3
"""
Jour 23 du défi Advent Of Code pour l'année 2023
"""
import os
import heapq

from aoc_utils import graph, constants, decorators


def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    filename = os.path.join(os.path.dirname(__file__ ), "inputs", "day23.txt")
    with open(filename, 'r') as f:
        sample = f.read().split('\n')
    sample = [ [j for j in i] for i in sample if i != '' ]
    return sample

def find_start(sample):
    """Départ du puzzle"""
    for i in range(len(sample[0])):
        if sample[0][i] == '.':
            return (0, i)
    raise NotImplementedError

def find_end(sample):
    """Arrivée du puzzle"""
    for i in range(len(sample[-1])):
        if sample[-1][i] == '.':
            return (len(sample)-1, i)
    raise NotImplementedError

def valid(pos, sample):
    """La position est bien dans la grille"""
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(sample) and pos[1] < len(sample[0])


def not_intersect(l1, l2):
    """L'intersection de l1 et l2 est bien vide"""
    return len(set(l1)&set(l2)) == 0

def added_elems(pos, npos):
    """Éléments vus en passant de pos à npos"""
    if abs(npos[0]-pos[0])+abs(npos[1]-pos[1]) == 1:
        return [npos]
    p0 = (min(pos[0], npos[0]), min(pos[1], npos[1]))
    p1 = (max(pos[0], npos[0]), max(pos[1], npos[1]))
    elems = set()
    for i in range(p1[0]-p0[0]+1):
        for j in range(p1[1]-p0[1]+1):
            elems.add((p0[0]+i, p0[1]+j))
    return list(elems-{pos})


def find_next(sample, i, j):
    """Pourquoi en double ? je ne suis pas sûr duquel est exécuté donc je touche pas pour le moment"""
    symb = sample[i][j]
    dirt = constants.arrows_dir[symb]
    i, j = i+dirt[0], j+dirt[1]
    i, j = i+dirt[0], j+dirt[1]

    return (i, j)

def compress_voisins(i, j, sample, symbols={'.'}):
    """Prochains voisins en sautant les longs tunnels"""
    def two_dirs(pi, pj):
        return len([(a, b) for a, b in constants.cardinal_dir if valid((pi+a, pj+b), sample) and sample[pi+a][pj+b] in symbols]) <= 2

    v = set()
    for d in constants.cardinal_dir:
        pi, pj = i+d[0], j+d[1]
        if valid((pi, pj), sample) and sample[pi][pj] in symbols:
            while valid((pi, pj), sample) and sample[pi][pj] in symbols and two_dirs(pi, pj):
                pi, pj = pi+d[0], pj+d[1]
            if not two_dirs(pi, pj):
                pi, pj = pi+d[0], pj+d[1]
            v.add((pi-d[0], pj-d[1]))
    return v

def longest_hike(sample, start, end, part=1):
    def find_next(sample, i, j): # Globalement inutile, je n'avais pas compris la question comme ça initialement
        """Renvoie la position après avoir marché sur i, j"""
        symb = sample[i][j]
        dirt = constants.arrows_dir[symb]
        i, j = i+dirt[0], j+dirt[1]
        while valid((i, j), sample) and sample[i][j] != '#':
            i, j = i+dirt[0], j+dirt[1]
        i, j = i-dirt[0], j-dirt[1]
        return (i, j)

    def voisins(pos):
        """Renvoie les "voisins" de pos, via compress_voisins notamment qui renvoie ~les voisins les plus loins~"""
        v = set()
        if part == 2:
            return compress_voisins(pos[0], pos[1], sample, symbols={'^', 'v', '<', '>', '.'})-{pos}

        potentials = [(pos[0]+1, pos[1]), (pos[0]-1, pos[1]), (pos[0], pos[1]+1), (pos[0], pos[1]-1)]
        for i, j in potentials:
            if valid((i, j), sample):
                if sample[i][j] in {'^', 'v', '<', '>'}:
                    nx = find_next(sample, i, j)
                    v.add(nx)
                
        return (v|compress_voisins(pos[0], pos[1], sample)) -{pos}

    # Cache voisins
    pre_voisins = {}
    for i in range(len(sample)):
        for j in range(len(sample[0])):
            if sample[i][j] in {'^', 'v', '<', '>', '.'}:
                pre_voisins[(i, j)] = voisins((i, j))


    to_end = []
    current_max = 0

    priority_queue = [(0, (start, [start]))]
    while priority_queue:
        popped = heapq.heappop(priority_queue)
        dist, data = popped
        pos, prev = data

        for npos in pre_voisins[pos]:
            if npos == end:
                to_end.append((dist+abs(npos[0]-pos[0])+abs(npos[1]-pos[1]), [])) #! Faster to return [] but will loose the "good" return path
                current_max = max(current_max, dist+abs(npos[0]-pos[0])+abs(npos[1]-pos[1]))

            added = added_elems(pos, npos)
            assert len(added) > 0
            if not_intersect(added, prev) and valid(npos, sample):
                heapq.heappush(priority_queue, (dist+abs(npos[0]-pos[0])+abs(npos[1]-pos[1]), (npos, prev+added)))

    return max(to_end)


def print_sol(solt, sample):
    """Afficher une solution"""
    for i in range(len(sample)):
        for j in range(len(sample[0])):
            if (i, j) in solt:
                print('O', end='')
            else:
                print(sample[i][j], end='')
        print()


def graph_longest_hike(g, start, end):
    to_end = set()

    priority_queue = [(0, (start, [start]))]
    while priority_queue:
        popped = heapq.heappop(priority_queue)
        dist, data = popped
        pos, prev = data

        for voisin, local_dist in g[pos]:
            if voisin == end:
                if dist+local_dist not in to_end:
                    print(f"\rMaximum actuel: {dist+local_dist}", end="")
                    to_end.add(dist+local_dist)

            if voisin not in prev:
                heapq.heappush(priority_queue, (dist+local_dist, (voisin, prev+[voisin])))

    print()
    return max(to_end)

def print_sol(solt, sample):
    """Afficher une solution"""
    for i in range(len(sample)):
        for j in range(len(sample[0])):
            if (i, j) in solt:
                print('O', end='')
            else:
                print(sample[i][j], end='')
        print()

def create_graph(sample, symbols={'.'}):
    def get_voisins(i, j):
        potentials = [(i+a, j+b) for a, b in constants.cardinal_dir]
        v = set()
        for a, b in potentials:
            if valid((a, b), sample) and sample[a][b] in symbols:
                v.add(((a, b), 1))
            elif valid((a, b), sample) and sample[a][b] in constants.arrows_dir.keys():
                direction = constants.arrows_dir[sample[a][b]]
                if valid((a+direction[0], b+direction[1]), sample) and sample[a+direction[0]][b+direction[1]] in symbols:
                    v.add(((a+direction[0], b+direction[1]), 2))

        return {(voisin, cout) for voisin, cout in v if voisin != (i, j)}

    g = graph.Graph()
    for i in range(len(sample)):
        for j in range(len(sample[0])):
            if sample[i][j] in symbols:
                g.add_node((i, j))

    for node in g:
        for voisin, cost in get_voisins(*node):
            g.add_edge(node, voisin, weight=cost)

    return g

@decorators.timeit
def part1(sample):
    """Partie 1 du défi"""
    # On ne peut pas utiliser la méthode du graphe car
    # on compresse les graphes non orientés seulement

    # Attention: ne donne pas le bon résultat sur les tests
    start, end = find_start(sample), find_end(sample)
    value, points = longest_hike(sample, start, end)
    return value

@decorators.timeit
def part2(sample):
    """Partie 2 du défi"""
    # au bout de 1h20, 2378 seulement avec l'ancienne méthode
    # 4mn pour tout faire avec un graphe "compressé"
    g = create_graph(sample, symbols={'.', '<', '>', '^', 'v'})
    ratio = g.compress()

    start, end = find_start(sample), find_end(sample)
    return graph_longest_hike(g, start, end)


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()
