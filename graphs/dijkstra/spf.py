###############################################################################################################
# Programming problem 10.8. Algorithms Illuminated. Part 2 by Tim Roughgarden
###############################################################################################################
from typing import List, Union


def dijkstra(graph: List[tuple], v: Union[int, str]) -> dict:
    def find_vertices(graph: List[tuple]) -> set:
        vertices = set()
        for v1, v2, _ in graph:
            vertices.add(v1)
            vertices.add(v2)
        return vertices

    _graph = graph.copy()

    current_vertex = v
    current_weight = 0
    v_seen = {v}
    v_unseen = find_vertices(_graph) - v_seen
    result = {current_vertex: (current_weight, None)}

    while len(v_unseen) > 0:
        for v1, v2, edge_weight in _graph:
            edge = {v1, v2}
            if current_vertex in edge:
                v_other = (edge - {current_vertex}).pop()
                v_other_weight = current_weight + edge_weight
                v_res_weight, v_res_prev = result.get(v_other, (None, None))
                if v_res_weight is not None:
                    if v_res_weight > v_other_weight:
                        result[v_other] = (v_other_weight, current_vertex)
                else:
                    result[v_other] = (v_other_weight, current_vertex)

        v_seen.add(current_vertex)

        candidate_vertex, candidate_weight = None, None
        for c_v in result.keys() - v_seen:  # find the next vertex to jump to
            c_w, c_b = result.get(c_v)
            if candidate_weight is None:
                candidate_vertex, candidate_weight = c_v, c_w
            else:
                if c_w < candidate_weight:
                    candidate_vertex, candidate_weight = c_v, c_w

        current_vertex, current_weight = candidate_vertex, candidate_weight

        v_unseen = v_unseen - v_seen

    return result


