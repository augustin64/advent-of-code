#!/usr/bin/python3
"""
Jour 07 du défi Advent Of Code pour l'année 2022
"""

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day07.txt', 'r') as f:
    #with open('ex.txt', 'r') as f:
        sample = f.read().split('\n')
    sample = [ i for i in sample if i != '' ]
    return sample

def change_dir(current_dir, args):
    if args[0] == "/":
        return args
    if args == "..":
        return "/".join(current_dir.split("/")[:-1])
    return current_dir + "/" + args

def create_dir(dir, filesystem):
    liste = dir.split("/")[1:]
    base = filesystem
    for e in liste:
        if e not in base.keys():
            base[e] = {}
        base = base[e]

def add_file(file, filesystem, current_dir):
    if file[0:3] == "dir":
        return

    liste = current_dir.split("/")[1:]
    base = filesystem
    for e in liste:
        base = base[e]

    size, name = int(file.split(" ")[0]), file.split(" ")[1]
    base[name] = size

def create_filesystem(sample):
    filesystem = {"":{}}
    current_dir = "/"
    for line in sample:
        if line == "$ ls":
            pass
        elif line[0] == "$": # cd
            current_dir = change_dir(current_dir, line[5:])
            create_dir(current_dir, filesystem)
        else:
            add_file(line, filesystem, current_dir)

    return filesystem

def part1(sample):
    """Partie 1 du défi"""
    fs = create_filesystem(sample)
    upper = []
    def compute_sizes(base):
        if type(base) == type(1):
            return base
        if type(base) == type({}):
            sum = 0
            for i in base.keys():
                sum += compute_sizes(base[i])

            if sum <= 100000:
                upper.append(sum)
            return sum

    total = compute_sizes(fs)
    return sum(upper)

def part2(sample):
    """Partie 2 du défi"""
    fs = create_filesystem(sample)
    upper = []
    def compute_sizes(base):
        if type(base) == type(1):
            return base
        if type(base) == type({}):
            sum = 0
            for i in base.keys():
                sum += compute_sizes(base[i])
            upper.append(sum)
            return sum

    total = compute_sizes(fs)
    upper.sort()
    return [i for i in upper if i > total-40000000][0]


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()