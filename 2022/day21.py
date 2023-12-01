#!/usr/bin/python3
"""
Jour 21 du défi Advent Of Code pour l'année 2022
"""
from tqdm import tqdm

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day21.txt', 'r') as f:
    #with open('test.txt', 'r') as f:
        sample = f.read().split('\n')
    sample = [ Monkey(i) for i in sample if i != '' ]
    return sample



class Monkey():
    def __init__(self, data):
        self.name = data.split(": ")[0]
        self.has_yelled = False
        self.value = -1
        if len(data.split(": ")[1].split(" ")) == 1:
            self.dependencies = []
            self.operation = lambda x : int(data.split(": ")[1])
        
        else:
            self.dependencies = [data.split(": ")[1].split(" ")[0], data.split(": ")[1].split(" ")[2]]
            self.operator = data.split(': ')[1].split(' ')[1]
            self.operation = lambda deps: eval(f"deps[0] {data.split(': ')[1].split(' ')[1]} deps[1]")

    def evaluate(self, data):
        if len(self.dependencies) == 0:
            self.has_yelled = True
            self.value = self.operation(0)
            return

        for name in self.dependencies:
            monkey = data[name]
            if not monkey.has_yelled:
                monkey.evaluate(data)
            
        self.has_yelled = True
        self.value = self.operation((data[self.dependencies[0]].value, data[self.dependencies[1]].value))

    def get_recursive_dependencies(self, data):
        if len(self.dependencies) == 0:
            return [self.name]

        return data[self.dependencies[0]].get_recursive_dependencies(data) + data[self.dependencies[1]].get_recursive_dependencies(data) + [self.name]

    def find_value(self, value, name, data):
        if self.name == name:
            return int(value)

        if name in data[data[self.name].dependencies[0]].get_recursive_dependencies(data):
            change_me = data[data[self.name].dependencies[0]]
            other = data[data[self.name].dependencies[1]]
        else:
            change_me = data[data[self.name].dependencies[1]]
            other = data[data[self.name].dependencies[0]]

        other.evaluate(data)
        if self.operator == '*':
            return int(change_me.find_value(value/other.value, name, data))
        if self.operator == '+':
            return int(change_me.find_value(value-other.value, name, data))

        if change_me.name == data[data[self.name].dependencies[1]]:
            if self.operator == '/':
                return int(change_me.find_value(other.value/value, name, data))
            if self.operator == '-':
                return int(change_me.find_value(other.value-value, name, data))
        
        if self.operator == '/':
            return int(change_me.find_value(other.value*value, name, data)) # Not really)
        if self.operator == '-':
            return int(change_me.find_value(other.value+value, name, data))
        


def part1(sample):
    """Partie 1 du défi"""
    data = {}
    for monkey in sample:
        data[monkey.name] = monkey

    data["root"].evaluate(data)
    return data["root"].value

    

def part2_brute():
    """Partie 2 du défi"""
    """Relativement lent, mais l'approche par brute force finit par fonctionner"""
    for i in tqdm(range(3876907167494-5, 3876907167494+5)):
        sample = read_sample()
        data = {}
        for monkey in sample:
            data[monkey.name] = monkey

        data["humn"].value = i
        data["humn"].has_yelled = True

        data[data["root"].dependencies[0]].evaluate(data)
        data[data["root"].dependencies[1]].evaluate(data)
        if data[data["root"].dependencies[0]].value == data[data["root"].dependencies[1]].value:
            return i
            
    return NotImplementedError

def part2(sample):
    """Partie 2 du défi"""
    """Ne fonctionne pas"""

    data = {}
    for monkey in sample:
        data[monkey.name] = monkey


    if "humn" in data[data["root"].dependencies[0]].get_recursive_dependencies(data):
        humn = data[data["root"].dependencies[0]]
        other = data[data["root"].dependencies[1]]
    else:
        humn = data[data["root"].dependencies[1]]
        other = data[data["root"].dependencies[0]]

    other.evaluate(data)
    return humn.find_value(other.value, "humn", data)



def main():
    """Fonction principale"""
    sample = read_sample()
    print(f"part1: {part1(sample)}")
    print(f"part2: {part2(read_sample())}")
    print(f"part2 bruteforce: {part2_brute()}")

if __name__ == "__main__":
    main()