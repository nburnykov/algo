###############################################################################################################
# Programming problem 18.8. Algorithms Illuminated. Part 3 by Tim Roughgarden
###############################################################################################################
from typing import List, Tuple, Optional


def bellman_ford(adjacency_list: List[Tuple[int, int, int]], vertex: int) -> Optional[List[List[int]]]:
    """
    Bellman-Ford algo implementation

    :param adjacency_list: A list that contains tuples with start vertex index, end vertex index and path weight
    :param vertex: An index of the vertex to calculate all possible paths started with this
    :return: A list with all possible paths, in case of negative cycle - None
    """
    _vertices = set()
    _adj_list = adjacency_list.copy()
    _weight_map = dict()
    for vertex_a, vertex_b, weight in _adj_list:
        _vertices.add(vertex_a)
        _vertices.add(vertex_b)
        _weight_map.setdefault(vertex_b, []).append((vertex_a, weight))
    _weights = [[None] * len(_vertices) for _ in range(len(_vertices) + 1)]
    _vertex_hop = [None] * len(_vertices)
    _weights[0][vertex] = 0
    is_stable = True
    for i in range(1, len(_weights)):
        is_stable = True
        for j in range(len(_vertices)):
            weight_current = _weights[i - 1][j], j
            weight_candidates = []
            for v, w in _weight_map.get(j, []):
                weight_cand = _weights[i - 1][v]
                if weight_cand is not None:
                    weight_candidates.append((weight_cand + w, v))
            if weight_current[0] is not None:
                weight_candidates.append(weight_current)
            if len(weight_candidates) > 0:
                weight_best, v_best = min(weight_candidates, key=lambda x: x[0])
                _weights[i][j] = weight_best
                _vertex_hop[j] = v_best
        if _weights[i] == _weights[i - 1]:
            break  # early stopping
        else:
            is_stable = False

    if not is_stable:  # path weights changed all the time to the last iteration -> negative cycle
        return

    result = []
    for i in range(len(_vertex_hop)):  # reconstruction part
        hop_list = [i]
        hop = _vertex_hop[i]
        if hop is None:
            result.append(hop_list)
            continue
        while hop != vertex:
            hop_list.append(hop)
            hop = _vertex_hop[hop]
        hop_list.append(vertex)
        result.append(hop_list[::-1])

    return result
