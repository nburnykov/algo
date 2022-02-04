###############################################################################################################
# Programming problem 15.9. Algorithms Illuminated. Part 2 by Tim Roughgarden
###############################################################################################################

from typing import List


def mst_prim_basic(edge_list: List[tuple], start_vertex: str) -> list:
    """
    Basic implementation of Prim minimum spanning tree algorithm
    Complexity is the sum of the main part and initial sorting mn + nlog(n) = n(m+log(n))

    :param edge_list: list of graph edges with every item as tuple (edge_cost, vertex_a, vertex_b)
    :param start_vertex: start vertex id
    :return: mst as list of edges
    """

    el = edge_list.copy()
    el = sorted(el, key=lambda x: x[0])  # this optimisation doesn't hurt anybody but speeds up the search

    vertices_left = set([x for item in edge_list for x in item[1:]])
    vertices_left.remove(start_vertex)

    vertices_processed = {start_vertex}

    mst_edge_list = []

    while len(vertices_left) > 0:  # complexity is O(m)
        for cost, v_a, v_b in el:  # complexity is O(n)
            vertices_diff = {v_a, v_b} - vertices_processed

            if len(vertices_diff) == 1:
                # this means that we found an edge with one vertex that isn't processed yet,
                # but the other one is processed

                v = vertices_diff.pop()  # O(1)
                vertices_processed.add(v)  # O(1)
                vertices_left.remove(v)  # O(1)
                mst_edge_list.append((cost, v_a, v_b))  # list.pop has O(n) complexity, so we don't use it here
                break

    return mst_edge_list