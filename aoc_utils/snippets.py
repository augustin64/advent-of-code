from typing import TypeVar

Nb = TypeVar("Nb", int, float)


def lagrange_interpolation(points: list[tuple[Nb, Nb]], x0: Nb) -> int:
    result = 0
    for i in range(len(points)):
        temp = points[i][1]
        for j in range(len(points)):
            if j != i:
                temp *= (x0 - points[j][0]) / (points[i][0] - points[j][0])

        result += temp

    return int(result)



def area(points: list[tuple[Nb, Nb]], count_border: bool=True) -> int:
    def distance(p1: tuple[Nb, Nb], p2: tuple[Nb, Nb]) -> float:
        return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

    def get_info(x1: Nb, y1: Nb, x2: Nb, y2: Nb) -> Nb:
        return x1*y2 - y1*x2

    def inner_area() -> float:
        first_x, first_y = points[0]
        prev_x, prev_y = first_x, first_y
        res = 0

        for i in range(len(points)-1):
            next_x, next_y = points[i+1]
            res = res + get_info(prev_x, prev_y, next_x, next_y)
            prev_x = next_x
            prev_y = next_y
        res = res + get_info(prev_x, prev_y, first_x, first_y)
        return abs(res)/2.0

    def border() -> float:
        distances = [distance(points[i], points[i+1]) for i in range(len(points)-1)]
        distances.append(distance(points[-1], points[0]))
        return sum(distances)

    if count_border:
        return int(inner_area()+border()//2 +1)

    return int(inner_area())


def get8_adj(x, y, max_x, max_y):
    """
    Get 8 adjacent positions of a point in a grid
    """
    pos = [
        (x-1, y-1), (x-1, y), (x-1, y+1),
        (x, y-1),             (x, y+1),
        (x+1, y-1), (x+1, y), (x+1, y+1),
    ]
    return [
        (i, j) for (i, j) in pos
        if i >= 0 and j >= 0 and
        i < max_x and j < max_y
    ]
