#!/usr/bin/python3
"""
Jour 20 du défi Advent Of Code pour l'année 2023
"""
import os
import heapq
import math

FLIP_FLOP=0
BROADCAST=1
CONJUNCTION=2

class Module:
    def __init__(self, text, inputs = None):
        self.status = {}
        self.dest = text.split(" -> ")[1].strip().split(", ")
        if inputs is not None:
            self.inputs = inputs
        else:
            self.inputs = []

        match (text[0]):
            case '%':
                self.type = FLIP_FLOP
                self.status["flip-flopped"] = False
            case '&':
                self.type = CONJUNCTION
                self.status["received"] = {i: "-low" for i in self.inputs}
            case 'b':
                self.type = BROADCAST

        if self.type == BROADCAST:
            self.name = "broadcaster"
        else:
            self.name = text.split(" -> ")[0][1:]
        

    def __repr__(self):
        if self.type == BROADCAST:
            return f"{self.name} -> {''.join(self.dest)}"
        if self.type == CONJUNCTION:
            return f"&{self.name} -> {''.join(self.dest)} [{self.status['received']}]"
        if self.type == FLIP_FLOP:
            return f"%{self.name} -> {''.join(self.dest)}"
        raise NotImplementedError


    def get_signals(self, signal):
        if self.type == FLIP_FLOP:
            if signal[1] == "-high":
                return []
            if self.status["flip-flopped"]: # Is on ?
                next = "-low"
            else:
                next = "-high"
            self.status["flip-flopped"] = not self.status["flip-flopped"]
            return [(dest, next) for dest in self.dest]

        if self.type == CONJUNCTION:
            self.status["received"][signal[2]] = signal[1]
            #print({i for i in self.status["received"].values()}, self.status["received"])
            if "-low" not in {i for i in self.status["received"].values()}:
                return [(dest, "-low") for dest in self.dest]
            return [(dest, "-high") for dest in self.dest]

        if self.type == BROADCAST:
            return [(dest, signal[1]) for dest in self.dest]

        raise NotImplementedError
                



def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    filename = os.path.join(os.path.dirname(__file__ ), "inputs", "day20.txt")
    with open(filename, 'r') as f:
        sample = f.read().split('\n')
    sample = [ i for i in sample if i != '' ]
    return sample

def propagate(modules, signal=("broadcaster", "-low")):
    low_pulses, high_pulses = 0, 0
    priority_queue = [(0, (signal[0], signal[1], "button"))]
    while priority_queue:
        dist, signal = heapq.heappop(priority_queue)
        if signal[1] == "-low":
            low_pulses += 1
        else:
            high_pulses += 1

        if signal[0] in modules.keys():
            next_messages = modules[signal[0]].get_signals(signal)
            for message in next_messages:
                #print(f"{signal[0]} received {signal[1]}: {message[1]} -> {message[0]}")
                msg = (message[0], message[1], signal[0])
                heapq.heappush(priority_queue, (dist+1, msg))
        elif signal[1] == "-low":
            return low_pulses, high_pulses, True

    return low_pulses, high_pulses, False


def get_modules(sample):
    modules = { i.name: Module(i) for i in sample }

    for m in modules.values():
        for d in m.dest:
            if d in modules.keys():
                modules[d].inputs.append(m.name)
                if modules[d].type == CONJUNCTION:
                    modules[d].status["received"][m.name] = "-low"
    return modules


def part1(sample, times=1000):
    """Partie 1 du défi"""
    modules = get_modules(sample)

    #print(modules)
    somme = (0, 0)
    for i in range(times):
        res = propagate(modules)
        somme = (somme[0]+res[0], somme[1]+res[1])
    return somme[0]*somme[1], somme


def part2(sample):
    """Partie 1 du défi"""
    modules = get_modules(sample)

    min_high = {}
    pre = [m for m in modules if "rx" in m.dest][0]
    for key in pre.status["received"].keys():
        min_high[key] = -1
            
    #print(modules)
    activations = 0
    while True:
        activations+=1
        res = propagate(modules)
        pre = [m for m in modules if "rx" in m.dest][0]
        for key in pre.status["received"].keys():
            if pre.status["received"]["key"] == "-high" and min_high[key] == -1:
                min_high[key] = activations

        if -1 not in min_high.values():
            return math.lcm(*min_high.values())


def main():
    """Fonction principale"""
    print(f"part1: {part1(read_sample())}")
    print(f"part2: {part2(read_sample())}")

if __name__ == "__main__":
    main()