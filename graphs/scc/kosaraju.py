###############################################################################################################
# Programming problem 8.10. Algorithms Illuminated. Part 2 by Tim Roughgarden
###############################################################################################################

from typing import List
from graphs.toposort.toposort import topsort, dfs_sort


def reverse_graph(adj_list: List[tuple]) -> List[tuple]:
    return [(v2, v1) for v1, v2 in adj_list]


def kosaraju(adj_list: List[tuple]) -> List[tuple]:  # vertex - scc
    """

    :param adj_list:
    :return: list of tuples: vertex - respective scc
    """
    vertices_ordered = topsort(adj_list)
    reversed_graph = reverse_graph(adj_list)

    scc_count = 0
    result = []

    while len(vertices_ordered) > 0:
        v = vertices_ordered[0]
        vertices_scc = dfs_sort(reversed_graph, v)
        vertices_scc_correct = set(vertices_ordered) & set(vertices_scc)
        for v_scc in vertices_scc_correct:
            result.append((v_scc, scc_count))
            vertices_ordered.remove(v_scc)
        scc_count += 1

    return result