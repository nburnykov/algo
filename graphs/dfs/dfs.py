from typing import List


def dfs_iter(adjacency_list: List[tuple], vertex: int) -> List[tuple]:
    """
    Iterative DFS implementation

    :param adjacency_list:
    :param vertex:
    :return:
    """
    _adjacency_list = adjacency_list.copy()
    vertexes = [vertex]
    result = []
    _iter = 0
    while len(vertexes) > 0:
        v = vertexes.pop(-1)
        _iter += 1
        indexes = []
        for i, (v1, v2) in enumerate(_adjacency_list):
            if v in (v1, v2):
                if v == v1:
                    vertexes.append(v2)
                    result.append((v, v2))
                else:
                    vertexes.append(v1)
                    result.append((v, v1))
                indexes.append(i)
        for i in indexes[::-1]:
            _adjacency_list.pop(i)

    return result


