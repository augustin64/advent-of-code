#!/usr/bin/python3
"""
Jour 25 du défi Advent Of Code pour l'année 2023
"""
import os

import networkx as nx
import matplotlib.pyplot as plt

from aoc_utils import graph

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    filename = os.path.join(os.path.dirname(__file__ ), "inputs", "day25.txt")
    with open(filename, 'r') as f:
        sample = f.read().split('\n')
    sample = [ i for i in sample if i != '' ]
    return sample

def create_graph(sample):
    g = graph.Graph()
    for line in sample:
        node = line.split(": ")[0]
        dests = line.split(": ")[1].split()
        if node not in g:
            g.add_node(node)

        for dest in dests:
            if dest not in [i[0] for i in g[node]]:
                g.add_edge(node, dest)

    return g



def part1(sample):
    """Partie 1 du défi"""
    g = create_graph(sample)
    
    ng = g.networkx()
    cut, parts = nx.stoer_wagner(ng)

    assert cut == 3
    assert len(parts) == 2

    return len(parts[0])*len(parts[1])

    #* Initial code:
    """
    ng = g.networkx()
    nx.draw(ng, with_labels=True)
    plt.savefig("path.png")

    to_delete = [("vqj", "szh"), ("jbx", "sml"), ("zhb", "vxr")]
    #to_delete = [("hfx", "pzl"), ("bvb", "cmg"), ("nvd", "jqt")]
    for edge in to_delete:
        g.remove_edges(*edge)


    ccs = g.connexes()
    print([len(i) for i in ccs])
    return len(ccs[0])*len(ccs[1])
    """

def part2(sample):
    """Partie 2 du défi"""
    return "Go push the big red button"


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()