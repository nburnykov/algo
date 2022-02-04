from typing import List


def dfs_sort(dag_adjacency_list: list, vertex: int) -> list:
    """
    Returns vertices in sorted order from first to last
    :param dag_adjacency_list: adjacency list that defines DAG
    :param vertex: vertex to start
    :return: vertices sorted from first to last
    """
    queue = [vertex]
    discovered = {vertex}
    result = []
    while len(queue) > 0:
        v = queue[0]
        new_adj_found = False
        index_to_pop = None
        for i, (v1, v2) in enumerate(dag_adjacency_list):
            if v == v1:
                new_adj_found = True
                if v2 not in discovered:
                    discovered.add(v2)
                    queue.insert(0, v2)
                index_to_pop = i
                break
        if not new_adj_found:
            result.insert(0, v)
            queue.pop(0)  # remove vertex only if there is no path to the new vertices from it
        if index_to_pop is not None:
            dag_adjacency_list.pop(index_to_pop)

    return result


def topsort(dag_adjacency_list: List[tuple]) -> list:
    """

    :param dag_adjacency_list:
    :return: vertex order from first to last
    """

    _dag_adjacency_list = dag_adjacency_list.copy()
    result = []
    result_set = set()
    while len(_dag_adjacency_list) > 0:
        v = _dag_adjacency_list[0][0]
        r = dfs_sort(_dag_adjacency_list, v)
        print(r, v)
        indexes = []
        for i, item in enumerate(r):
            if item in result_set:
                indexes.append(i)
        for i in indexes[::-1]:
            r.pop(i)
        result = r + result
        result_set.update(r)

    return result


