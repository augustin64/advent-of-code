#!/usr/bin/python3
"""
Jour 16 du défi Advent Of Code pour l'année 2022
"""
import copy

def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day16.txt', 'r') as f:
        sample = f.read().split('\n')
    sample = [ i for i in sample if i != '' ]
    data = []
    for line in sample:
        split = line.split(" ")
        "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB"
        valve_nb = split[1]
        flow_rate = int(split[4].split("=")[-1].split(";")[0])
        lead_to = " ".join(split[9:]).split(", ")
        data.append((valve_nb, flow_rate, lead_to))
    return data


def floyd_warshall(valves):
    dist = {v: {u: int(1e9) for u in valves} for v in valves}
    for v in valves:
        dist[v][v] = 0
        for u in valves[v]["lead_to"]:
            dist[v][u] = 1
    for k in valves:
        for i in valves:
            for j in valves:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


def part1(sample):
    """Partie 1 du défi"""
    data = {}
    for i in sample:
        data[i[0]] = {"enabled":False, "flow_rate": i[1], "lead_to": i[2]}

    distances = floyd_warshall(data)
    non_zero = [v for v in data if data[v]["flow_rate"] > 0]

    def generate_open_options(pos, opened, time_left):
        for next in non_zero:
            if next not in opened and distances[pos][next] <= time_left:
                opened.append(next)
                yield from generate_open_options(
                    next, opened, time_left - distances[pos][next] - 1
                )
                opened.pop()
        yield copy.copy(opened)

    def get_order_score(open_order, time_left):
        now, ans = "AA", 0
        for pos in open_order:
            time_left -= distances[now][pos] + 1
            ans += data[pos]["flow_rate"] * time_left
            now = pos
        return ans
    
    return max(get_order_score(ordre, 30) for ordre in generate_open_options("AA", [], 30))

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