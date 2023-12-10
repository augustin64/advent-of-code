#!/usr/bin/python3
"""
Jour 20 du défi Advent Of Code pour l'année 2022
    <!-- NE FONCTIONNE PAS --!>
"""

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day20.txt', 'r') as f:
        sample = f.read().split('\n')
    sample = [ int(i) for i in sample if i != '' ]
    return sample

def grove_coordinates(decrypted_file):
    n = len(decrypted_file)
    index_z = decrypted_file.index(0)
    return (
        decrypted_file[(1000+index_z)%n],
        decrypted_file[(2000+index_z)%n],
        decrypted_file[(3000+index_z)%n]
    )

def move(sample, item):
    index = sample.index(item)
    new_index = (index+item)%(len(sample)-1)
    sample.remove(item)
    sample.insert(new_index, item)

def part1(sample):
    """Partie 1 du défi"""
    encrypted_file = sample.copy()
    for i in sample:
        move(encrypted_file, i)
    
    coords = grove_coordinates(encrypted_file)
    print(coords)
    return coords[0]+coords[1]+coords[2]

def part2(sample):
    """Partie 2 du défi"""
    return NotImplementedError


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()