# Fiche de solutions/ astuces fréquentes pour AoC

Si on cherche à savoir quand qqchose va arriver et que ça arrive à la conjonction de plusieurs évènements
```python
math.lcm(*[_, _, ...])
```

quand on calcule les mêmes choses plein de fois (mais VRAIMENT les mêmes choses, pas un chouïa différent)
```python
from functools import cache

@cache
def ma_fonction(*args)
```

quand on doit calculer un truc très grand et que c'est un nb d'états finis (qui se répètent potentiellement)
détection de cycle

quand on doit calculer un truc très grand et que c'est un nb d'états infinis:
```python
snippets.lagrange_interpolation([(x1, y1), (x2, y2), ...], x0)
```

quand on doit calculer l'aire d'un polygone
```python
snippets.area([(x1, y1), (x2, y2), ...], count_border=True)
```

trop d'éléments en entrée: les considérer par ensembles si possible (genre séquences d'entiers)
```python
a = intervals.Interval(0, 5)
b = intervals.Interval(10, 15)

a.intersection(b) # None
a.intersect(b) # False

a = intervals.Interval(0, 5)
b = intervals.Interval(4, 15)

a.intersection(b) # [4, 5]
a.intersect(b) # True
```

quand on a un parcours de graphe, utiliser Graph, et le compresser si nécessaire (attention, que non-orienté !)

Trouver une instance qui satisfait plein de trucs et ça paraît impossible ? z3 ! `pip install z3-solver`
```python
px, py, pz, dx, dy, dz = z3.Ints("px py pz dx dy dz")
collision = [z3.Int("t"+str(i)) for i in range(len(hailstones))]
solver = z3.Solver()
for i in range(len(hailstones)):
    h = hailstones[i]
    solver.add(px + dx*collision[i] == h.px + h.dx*collision[i])
    solver.add(py + dy*collision[i] == h.py + h.dy*collision[i])
    solver.add(pz + dz*collision[i] == h.pz + h.dz*collision[i])

solver.check()

return solver.model().evaluate(px + py + pz)
```