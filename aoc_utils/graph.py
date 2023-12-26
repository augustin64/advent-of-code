from collections.abc import Mapping
from typing import TypeVar, Optional, Iterator, Generic
import networkx as nx
import matplotlib.pyplot as plt


T = TypeVar("T")


class Graph(Mapping, Generic[T]):
    """Non oriented graph"""
    def __init__(self) -> None:
        self._edges: dict = {}

    def __str__(self) -> str:
        return "\n".join(
            (f"{key} -> {self._edges[key]}" for key in self._edges)
        )

    def __len__(self) -> int:
        return len(self._edges)

    def __getitem__(self, e) -> list[tuple[T, int]]:
        return self._edges[e]

    def __iter__(self) -> Iterator[object]:
        return iter(self._edges)

    def __contains__(self, item: object) -> bool:
        return item in self._edges.keys()

    def add_node(self, u: T) -> None:
        if u in self._edges.keys():
            raise IndexError

        self._edges[u] = set()

    def add_edge(self, source: T, target: T, weight=None) -> None:
        if source not in self._edges:
            self.add_node(source)

        if target not in self._edges:
            self.add_node(target)

        if weight is None:
            weight = 1

        self._edges[source].add((target, weight))
        self._edges[target].add((source, weight))


    def remove_edges(self, source: T, target: T) -> None:
        for vertice in frozenset(self._edges[source]):
            if vertice[0] == target:
                self._edges[source] -= {vertice}

        for vertice in frozenset(self._edges[target]):
            if vertice[0] == source:
                self._edges[target] -= {vertice}


    def remove_node(self, u: T) -> None:
        if u not in self:
            raise IndexError
        
        for node in self:
            self.remove_edges(u, node)

        self._edges.pop(u, None)

    def compress(self) -> None:
        """Remove nodes that have only 2 edges to get a minimal representation"""
        initial_size = len(self)
        for node in self._edges.copy():
            if len(self[node]) == 2:
                weight = sum((edge[1] for edge in self[node]))
                self.add_edge(list(self[node])[0][0], list(self[node])[1][0], weight=weight)
                self.remove_node(node)

        return len(self)/initial_size


    def bellman_ford(self, source: T) -> \
            tuple[dict[T, int], dict[T, Optional[T]]]:
        # Initialize distances and predecessors
        dist_max = len(self)*max(
            {max({j[1] for j in i}) for i in self._edges.values()}
        )
        distances = {node: dist_max for node in self._edges}
        predecessors = {
            node: None for node in self._edges
        }  # ! The only problem is here for the typing system
        distances[source] = 0

        # Relax edges repeatedly to find the shortest paths
        for _ in range(len(self._edges) - 1):
            for u in self._edges:
                for v, weight in self._edges[u]:
                    if distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight
                        predecessors[v] = u

        # Check for negative cycles
        for u in self._edges:
            for v, weight in self._edges[u]:
                if distances[u] + weight < distances[v]:
                    raise ValueError("Graph contains a negative cycle")

        return distances, predecessors

    def networkx(self):
        g = nx.Graph()
        g.add_nodes_from(self)
        for node in self:
            for dest, _ in self[node]:
                g.add_edge(node, dest)

        return g

    def dfs(self, node, views=None):
        if views is None:
            views = set()

        views.add(node)
        if node in self:
            for v, _ in self[node]:
                if v not in views:
                    views = views | self.dfs(v, views=views)
        return views

    def connexes(self):
        views = set()

        ccs = []
        for node in self:
            if node not in views:
                cur_views = self.dfs(node)
                ccs.append(cur_views)
                views = views | cur_views

        return ccs