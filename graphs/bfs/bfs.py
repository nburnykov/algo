from typing import List


def bfs(adj_list: List[tuple], start_vertex: int) -> List[tuple]:
    adj_list_copy = adj_list.copy()
    vertex_list = [start_vertex]
    result = []
    while len(vertex_list) > 0:
        vertex = vertex_list.pop(-1)
        indexes = []
        for i, adj in enumerate(adj_list_copy):
            if vertex in adj:
                indexes.append(i)

                v1, v2 = adj
                other = v2 if vertex == v1 else v1
                vertex_list.insert(0, other)
                result.append((vertex, other))

        for i in indexes[::-1]:
            adj_list_copy.pop(i)

    return result


