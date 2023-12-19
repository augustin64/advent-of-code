#!/usr/bin/python3
"""
Jour 19 du défi Advent Of Code pour l'année 2023
"""
import os

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    filename = os.path.join(os.path.dirname(__file__ ), "inputs", "day19.txt")
    with open(filename, 'r') as f:
        sample = f.read()
    return sample

def parse_sample(sample):
    def parse_wf(wf):
        name = wf.split("{")[0]
        content = wf.split("{")[1].split("}")[0].split(",")
        return name, content

    def parse_part(part):
        content = part.split("{")[1].split("}")[0].split(",")
        dico = {p.split("=")[0]: int(p.split("=")[1]) for p in content}
        return dico

    workflows, parts, = sample.split("\n\n")
    workflows = [parse_wf(i) for i in workflows.split("\n") if i != '']
    workflows = {i[0]: i[1] for i in workflows}
    parts = [parse_part(i) for i in parts.split("\n") if i != '']
    return workflows, parts


def process(part, workflows, start="in"):
    def goto(instr):
        if instr == "A":
            return True
        if instr == "R":
            return False
        return process(part, workflows, start=instr)

    def ceval(expr):
        if '>' in expr:
            a, b, = expr.split('>')
            return part[a] > int(b)
        if '<' in expr:
            a, b, = expr.split('<')
            return part[a] < int(b)

    for instr in workflows[start]:
        if ':' in instr:
            if ceval(instr.split(":")[0]):
                return goto(instr.split(":")[1])
        else:
            return goto(instr)
    return goto("R")


def process2(part, workflows, start="in"):
    def sizeof(part):
        prod = 1
        for i in part.values():
            prod *= i[1]-i[0]+1
        return prod

    def goto(instr, part):
        if instr == "A":
            return sizeof(part) # taille de l'instance
        if instr == "R":
            return 0
        return process2(part, workflows, start=instr)

    def apply_flows(part, flows):
        if not flows:
            raise NotImplementedError
        instr, *next_flows = flows

        if ":" not in instr:
            return goto(instr, part)

        expr = instr.split(":")[0]
        action = instr.split(":")[1]
        if '>' in expr:
            a, b, = expr.split('>')
            if part[a][0] > int(b):
                return goto(action, part)
            if part[a][1] <= int(b):
                return apply_flows(part, next_flows)

            left = part.copy()
            right = part.copy()
            left[a] = (part[a][0], int(b))
            right[a] = (int(b)+1, part[a][1])
            return goto(action, right)+apply_flows(left, next_flows)
        
        if '<' in expr:
            a, b, = expr.split('<')
            if part[a][1] < int(b):
                return goto(action, part)
            if part[a][0] >= int(b):
                return apply_flows(part, next_flows)

            left = part.copy()
            right = part.copy()
            left[a] = (part[a][0], int(b)-1)
            right[a] = (int(b), part[a][1])
            return goto(action, left)+apply_flows(right, next_flows)

    return apply_flows(part, workflows[start])
            


def part1(sample):
    """Partie 1 du défi"""
    workflows, parts = parse_sample(sample)
    somme = 0
    for part in parts:
        if process(part, workflows):
            somme += part["x"]+part["m"]+part["a"]+part["s"]
    return somme


def part2(sample):
    """Partie 2 du défi"""
    workflows, _ = parse_sample(sample)

    return process2({"x":(1, 4000), "m":(1, 4000), "a":(1, 4000), "s":(1, 4000)}, workflows)


def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(sample)}")

if __name__ == "__main__":
    main()