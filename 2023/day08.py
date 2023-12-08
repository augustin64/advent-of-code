#!/usr/bin/python3
"""
Jour 08 du défi Advent Of Code pour l'année 2023
"""

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def lcm_of_list(numbers):
    result = 1
    for num in numbers:
        result = lcm(result, num)
    return result



def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day08.txt', 'r') as f:
        sample = f.read().split('\n')
    sample = [ i for i in sample if i != '' ]
    return sample

def parse_sample(sample):
    instructions = sample[0]
    mappings = {
        i.split(" = ")[0]: (i.split(" = ")[1].split(", ")[0].replace("(", ""), i.split(" = ")[1].split(", ")[1].replace(")", ""))
        for i in (sample[1:]) if i != ""
    }
    return instructions, mappings

def number_steps(instructions, mappings, pos, untilZZZ=True):
    step = 0
    instr = {
        "R": 1, "L": 0
    }
    while (pos[-1] != 'Z') or (untilZZZ and pos != "ZZZ"):
        pos = mappings[pos][instr[instructions[step%len(instructions)]]]
        step += 1
    return step

def part1(sample):
    """Partie 1 du défi"""
    instructions, mappings = parse_sample(sample)
    return number_steps(instructions, mappings, "AAA")

def part2(sample):
    """Partie 2 du défi"""
    instructions, mappings = parse_sample(sample)
    a_ending = [i for i in mappings.keys() if i[-1] == 'A']
    steps = [number_steps(instructions, mappings, i, untilZZZ=False) for i in a_ending]
    return lcm_of_list(steps)


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()