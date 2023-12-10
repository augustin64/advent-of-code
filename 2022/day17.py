#!/usr/bin/python3
"""
Jour 17 du défi Advent Of Code pour l'année 2022
    <!-- NE FONCTIONNE PAS --!>
"""

PRINT = True
ROCKS = [
    [
        ["@", "@", "@", "@"]
    ],
    [
        [".", "@", "."],
        ["@", "@", "@"],
        [".", "@", "."]
    ],
    [
        [".", ".", "@"],
        [".", ".", "@"],
        ["@", "@", "@"]
    ],
    [
        ["@"],
        ["@"],
        ["@"],
        ["@"]
    ],
    [
        ["@", "@"],
        ["@", "@"],
    ]
]


def read_sample():
    """récupère les entrées depuis le fichier texte correspondant"""
    with open('inputs/day17.txt', 'r') as f:
        return f.read()


def print_puzzle(heights, rock, left_down_corner):
    if not PRINT:
        return
    for i in range(len(rock)):
        print("|"+"."*left_down_corner[1]+"".join(rock[i])+"."*(7-len(rock[i])-left_down_corner[1])+"|")
    for i in range(left_down_corner[0]-max(heights)):
        print("|"+"."*7+"|")
    for i in range(max(heights)):
        print("|", end="")
        for j in range(len(heights)):
            if heights[j] >= (max(heights)-i):
                print("#", end="")
            else:
                print(".", end="")
        print("|")
    print("+"+"-"*7+"+")
    print()


def gas_jet(direction, pos, rock, largeur):
    if direction == '>':
        if pos[1]+max([len(j) for j in rock]) < largeur: #Move
            pos = (pos[0], pos[1]+1)
            print("Move right:")
        else:
            print("Failed to move right:")
    else:
        if pos[1] > 0: #Move
            pos = (pos[0], pos[1]-1)
            print("Move left:")
        else:
            print("Failed to move left:")
    return pos

def part1(sample):
    """Partie 1 du défi"""
    largeur = 7
    heights = [0 for i in range(largeur)]
    stream_pos = 0
    for i in range(2022):
        print(f"rock {i}")
        rock = ROCKS[(i)%len(ROCKS)]
        
        left_down_corner = (max(heights)+3, 2)
        falling = True
        while falling:
            
            left_down_corner = gas_jet(sample[stream_pos%len(sample)], left_down_corner, rock, largeur)
            stream_pos += 1

            print_puzzle(heights, rock, left_down_corner)
            
            print("falls 1 unit:")
            left_down_corner = (left_down_corner[0]-1, left_down_corner[1])

            print_puzzle(heights, rock, left_down_corner)
            # Check si en bas
            if left_down_corner[0] <= 0:
                falling = False
            elif left_down_corner[0] <= max(heights)+1:
                print("Potentially blocked")
                for j in range(len(rock[0])):
                    print(f"trying on rock[*][{j}]")
                    if (len(rock)-1) - max([k for k in range(len(rock)) if rock[k][j] != '.']) + left_down_corner[0] == heights[j+left_down_corner[1]]:
                        falling = False
                        print("blocked")
                        break

            
            if falling:
                print_puzzle(heights, rock, left_down_corner)

        left_down_corner = gas_jet(sample[stream_pos%len(sample)], left_down_corner, rock, largeur)
        stream_pos += 1

        print_puzzle(heights, rock, left_down_corner)
        for j in range(len(rock[0])):
            (len(rock)-1) - max([k for k in range(len(rock)) if rock[k][j] != '.']) + left_down_corner[0]
            print(j+left_down_corner[1], left_down_corner[0], 1+min([k for k in range(len(rock)) if rock[k][j] != '.']))

            if heights[j+left_down_corner[1]] > left_down_corner[0] + len(rock)-(min([k for k in range(len(rock)) if rock[k][j] != '.'])):
                print(heights[j+left_down_corner[1]], left_down_corner[0] + len(rock)-(min([k for k in range(len(rock)) if rock[k][j] != '.'])), "Error!")
                print_puzzle(heights, rock, left_down_corner)
                print(heights)
                print(left_down_corner)
                print(len(rock))
                print(min([k for k in range(len(rock)) if rock[k][j] != '.']))
                raise Exception
            heights[j+left_down_corner[1]] = left_down_corner[0] + len(rock)-(min([k for k in range(len(rock)) if rock[k][j] != '.']))

    print("## ignore rock:")
    print_puzzle(heights, rock, left_down_corner)
    return max(heights)

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