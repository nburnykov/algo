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
        v = vertexes.pop(0)
        _iter += 1
        indexes = []
        for i, (v1, v2) in enumerate(_adjacency_list):
            if v in (v1, v2):
                if v == v1:
                    vertexes.insert(0, v2)
                    result.append((v, v2))
                else:
                    vertexes.insert(0, v1)
                    result.append((v, v1))
                indexes.append(i)
        for i in indexes[::-1]:
            _adjacency_list.pop(i)

    return result


# def dfs_recursive(adjacency_list: List[tuple], vertex: int) -> List[tuple]:
#     """
#     Recursive DFS implementation
#     :param adjacency_list:
#     :param vertex:
#     :return:
#     """
#     result = []
#     indexes = []
#     for i, (v1, v2) in adjacency_list:
#         if vertex in (v1, v2):
#             if vertex == v1:
#                 dfs_recursive(adjacency_list, v2)
#             else:
#                 dfs_recursive(adjacency_list, v1)
#             indexes.append(i)
#     for i in indexes[::-1]:
#         adjacency_list.pop(i)
#
#     return result
