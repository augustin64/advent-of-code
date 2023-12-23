#!/usr/bin/python3
"""
Jour 16 du défi Advent Of Code pour l'année 2023
"""
import os
from tqdm import tqdm
from aoc_utils.decorators import timeit

def read_sample() -> list[str]:
    """récupère les entrées depuis le fichier texte correspondant"""
    filename = os.path.join(os.path.dirname(__file__ ), "inputs", "day16.txt")
    with open(filename, 'r') as f:
        sample = f.read().split('\n')
    sample = [ i for i in sample if i != '' ]
    return sample


def diff(l1: set, l2: set) -> bool:
    return len(l1 ^ l2) > 0

def energize(sample: list[str], initial: tuple[tuple[int, int], tuple[int, int]]=((0, 0), (0, 1))) -> set[tuple[tuple[int, int], tuple[int, int]]]:
    def step(position: tuple[int, int], direction: tuple[int, int]):
        match sample[position[0]][position[1]]:
            case '\\':
                return [(direction[1], direction[0])]
            case '/':
                return [(-direction[1], -direction[0])]
            case '.':
                return [direction]
            case '-':
                if direction[0] != 0:
                    return [(0, 1), (0, -1)]
                return [direction]
            case '|':
                if direction[1] != 0:
                    return [(1, 0), (-1, 0)]
                return [direction]

    directions = set([initial]) # List[positions, directions]
    modif = True
    while modif:
        new_directions = set([initial])
        for pos, direction in directions:
            new = step(pos, direction)
            for dir_t in new:
                pos_t = (pos[0]+dir_t[0], pos[1]+dir_t[1])
                if pos_t[0] >= 0 and pos_t[1] >= 0 and pos_t[0] < len(sample) and pos_t[1] < len(sample[0]):
                    new_directions.add(( pos_t, dir_t ))

        modif = diff(directions, new_directions)
        directions = new_directions
        #print(new_directions)

    return directions


@timeit
def part1(sample: list[str]) -> int:
    """Partie 1 du défi"""
    dir_pos = energize(sample)
    energized = {i[0] for i in dir_pos}
    return len(energized)

@timeit
def part2(sample: list[str]) -> int:
    """Partie 2 du défi"""
    best = 0
    for i in tqdm(range(len(sample))):
        dir_pos = energize(sample, initial=((i, 0), (0, 1)))
        energized = {i[0] for i in dir_pos}
        best = max(len(energized), best)

        dir_pos = energize(sample, initial=((i, len(sample)-1), (0, -1)))
        energized = {i[0] for i in dir_pos}
        best = max(len(energized), best)

    for j in tqdm(range(len(sample[0]))):
        dir_pos = energize(sample, initial=((0, j), (1, 0)))
        energized = {i[0] for i in dir_pos}
        best = max(len(energized), best)

        dir_pos = energize(sample, initial=(((len(sample[0])-1, j)), (-1, 0)))
        energized = {i[0] for i in dir_pos}
        best = max(len(energized), best)

    return best


def main() -> None:
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()