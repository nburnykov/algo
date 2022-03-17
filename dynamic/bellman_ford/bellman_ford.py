from typing import List, Tuple


def bellman_ford(adjacency_list: List[Tuple[int, int, int]], vertex: int) -> List[List[int]]:
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
    for i in range(1, len(_weights)):
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
