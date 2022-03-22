###############################################################################################################
# Programming problem 18.8. Algorithms Illuminated. Part 3 by Tim Roughgarden
###############################################################################################################
from typing import List, Tuple, Optional
from itertools import permutations


def floyd_warshall(adjacency_list: List[Tuple[int, int, int]]) -> List[Tuple[int]]:

    vertices = set()
    for v1, v2, _ in adjacency_list:
        vertices.add(v1)
        vertices.add(v2)

    graph = [[None] * len(vertices) for _ in vertices]  # preparing matrix graph representation
    next_hop = [[None] * len(vertices) for _ in vertices]  # next hop matrix for path reconstruction

    for v1, v2, w in adjacency_list:
        graph[v1][v2] = w
        next_hop[v1][v2] = v2

    for v in vertices:
        if graph[v][v] is None:
            graph[v][v] = 0  # every vertex has zero weight path to itself

    for k in vertices:
        for i in vertices:
            for j in vertices:
                if (graph[i][k] is not None) and (graph[k][j] is not None) and (graph[i][j] is not None):
                    if (graph[i][k] + graph[k][j]) < graph[i][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]
                        next_hop[i][j] = next_hop[i][k]
                if (graph[i][j] is None) and (graph[i][k] is not None) and (graph[k][j] is not None):
                    graph[i][j] = graph[i][k] + graph[k][j]
                    next_hop[i][j] = next_hop[i][k]

    for k in vertices:  # search for negative cycles
        for i in vertices:
            for j in vertices:
                if (graph[i][k] is not None) and (graph[k][j] is not None) and (graph[i][j] is not None):
                    if (graph[i][k] + graph[k][j]) < graph[i][j]:
                        graph[i][j] = -1e7
                        next_hop[i][j] = -1
                if (graph[i][j] is None) and (graph[i][k] is not None) and (graph[k][j] is not None):
                    graph[i][j] = -1e7
                    next_hop[i][j] = -1

    vertex_pairs = permutations(vertices, 2)

    result = []
    for v1, v2 in vertex_pairs:
        if graph[v1][v2] is None:  # path does not exist
            continue
        next_v = v1
        path = [next_v]
        while next_v is not v2:
            if next_v == -1:
                path = []  # includes negative cycle
                break
            next_v = next_hop[next_v][v2]
            path.append(next_v)

        if len(path) > 0:
            result.append(tuple(path))

    return result









