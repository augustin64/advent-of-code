#!/usr/bin/python3
"""
Jour 05 du défi Advent Of Code pour l'année 2023
"""

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day05.txt', 'r') as f:
        sample = f.read().split('\n\n')
    sample = [ i for i in sample if i != '' ]
    return sample

def parse_sample(sample):
    data = []
    data.append(("seeds", [int(i) for i in sample[0].split(" ")[1:] if i != ""]))

    for subsample in sample[1:]:
        d = subsample.split("\n")
        name = d[0].split("-")[-1].split(" ")[0]
        maps = [[int(j) for j in i.split(" ") if i != ""] for i in d[1:] if i != ""]
        data.append((name, maps))
    return data


def get_locations(data, new_seed=False):
    if new_seed:
        # Nouvelle définition des range
        pos = []
        for i in range(int(len(data[0][1])/2)):
            pos.append((data[0][1][2*i], data[0][1][2*i+1]))
        # print(pos)
    else:
        # On considère des range de 1
        pos = [(i, 1) for i in data[0][1]]

    for converter in data[1:]:
        # On itère sur tous les changements de type de données
        new_pos = []
        for (source, rg) in pos:
            found = False # Il existe un converter ?
            min_dst = rg # Distance min à un converter
            for possible_dest in converter[1]:
                cv_dest, cv_source, cv_range = possible_dest 

                if source >= cv_source and source <= cv_source+cv_range:
                    # Un converter est disponible
                    treated_range = min(rg, cv_range - (source - cv_source))
                    if treated_range > 0: # Revoir la condition au dessus ? éviter de créer des élems 0 en tous cas
                        new_pos.append((source - (cv_source-cv_dest), treated_range))

                        #print(f"{converter[0]}: {source} -> {new_pos[-1]}")
                        if (rg > treated_range): # Partie non convertie
                            #print(f"using tr:", (source+treated_range, rg - treated_range))
                            pos.append((source+treated_range, rg - treated_range))
                        found = True
                        break

                elif cv_source > source:
                    min_dst = min(min_dst, cv_source-source)

            if not found:
                # On ajoute jusqu'au prochain converter
                new_pos.append((source, min_dst))
                if min_dst < rg:
                    pos.append((source+min_dst, rg-min_dst))
                #print(f"{converter[0]}: {source} -> {new_pos[-1]} (auto)")
        pos = new_pos
    return pos



def part1(sample):
    """Partie 1 du défi"""
    data = parse_sample(sample)
    return min(get_locations(data))[0]

def part2(sample):
    """Partie 2 du défi"""
    data = parse_sample(sample)
    return min(get_locations(data, new_seed=True))[0]


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()