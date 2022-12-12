#!/usr/bin/python3
"""
Jour 11 du défi Advent Of Code pour l'année 2022
"""
import math
import sys

sys.set_int_max_str_digits(10000)


def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day11.txt', 'r') as f:
        sample = f.read().split('\n\n')
    sample = [ Monkey(i) for i in sample if i != '' ]
    return sample



class Monkey():
    def __init__(self, data):
        data2 = data.split("\n")
        self.items = [int(i) for i in data2[1].strip().split(": ")[1].split(", ")]
        self.operation_type = data2[2].split(" ")[6]
        self.operation_elem = data2[2].split(" ")[7]
        self.test_divisible = int(data2[3].split(" ")[-1])
        self.next_monkey = {
            True: int(data2[4].split(" ")[-1]),
            False: int(data2[5].split(" ")[-1])
        }
        self.inspected_items = 0

    def inspect(self, item):
        worrying_level = item
        if self.operation_type == "+":
            worrying_level += int(self.operation_elem)
        elif self.operation_type == "*":
            if self.operation_elem == "old":
                worrying_level = worrying_level * worrying_level
            else:
                worrying_level = worrying_level * int(self.operation_elem)
        else:
            print(f"Unknown operation {self.operation_type}")

        # Lassitude
        worrying_level = math.floor((worrying_level/3))

        monkey_num = self.next_monkey[worrying_level % self.test_divisible == 0]
        self.inspected_items += 1
        return worrying_level, monkey_num

    def inspect2(self, item, modulo):
        worrying_level = item
        if self.operation_type == "+":
            worrying_level += int(self.operation_elem)
        elif self.operation_type == "*":
            if self.operation_elem == "old":
                worrying_level = worrying_level * worrying_level
            else:
                worrying_level = worrying_level * int(self.operation_elem)
        else:
            print(f"Unknown operation {self.operation_type}")

        # Lassitude
        worrying_level = worrying_level % modulo

        monkey_num = self.next_monkey[worrying_level % self.test_divisible == 0]
        self.inspected_items += 1
        return worrying_level, monkey_num

    def give_item(self, monkey, worrying_level):
        # Throw item
        self.items = self.items[1:]
        # Add item
        monkey.items.append(worrying_level)



def afficher_etat(sample):
    print("\n".join([f"Monkey {j}: {sample[j].items}" for j in range(len(sample))]))



def part1(sample):
    """Partie 1 du défi"""
    
    for round_ in range(20):
        for monkey in sample:
            for item in monkey.items:
                worr, next_monk = monkey.inspect(item)
                monkey.give_item(sample[next_monk], worr)
    
    most_active = [monkey.inspected_items for monkey in sample]
    most_active.sort()
    most_active.reverse()
    return most_active[0]*most_active[1]



def part2(sample):
    """Partie 2 du défi"""
    ppcm = math.lcm(*[i.test_divisible for i in sample])

    for round_ in range(10000):
        for monkey in sample:
            for item in monkey.items:
                worr, next_monk = monkey.inspect2(item, ppcm)
                monkey.give_item(sample[next_monk], worr)


    most_active = [monkey.inspected_items for monkey in sample]
    most_active.sort()
    most_active.reverse()
    return most_active[0]*most_active[1]


def main():
    """Fonction principale"""
    print(f"part1: {part1(read_sample())}")
    print(f"part2: {part2(read_sample())}")

if __name__ == "__main__":
    main()