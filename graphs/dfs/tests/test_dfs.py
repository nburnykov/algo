from random import random, shuffle
from typing import List

from graphs.dfs.dfs import dfs_iter


def mixer(data: List[tuple]) -> List[tuple]:
    """
    mixes vertex list
    :param data:
    :return:
    """
    _data = []
    for d0, d1 in data:
        if random() > 0.5:
            _data.append((d1, d0))  # swaps elements in tuple
        else:
            _data.append((d0, d1))

    shuffle(_data)

    return _data


def test_dfs_single():
    vertex = list(range(1, 14))
    adj_list = [
        (1, 4),
        (5, 4),
        (4, 3),
        (4, 8),
        (3, 2),
        (3, 6),
        (6, 7),
        (2, 7),
        (8, 13),
        (13, 9),
        (2, 10),
        (10, 12),
        (10, 11)
    ]

    adj_list_mixed = mixer(adj_list)
    dfs_result_1 = dfs_iter(adj_list_mixed, 1)
    dfs_result_9 = dfs_iter(adj_list_mixed, 9)
    dfs_result_2 = dfs_iter(adj_list_mixed, 2)

    dfs_1_vertex = set([v for v_pair in dfs_result_1 for v in v_pair])
    dfs_9_vertex = set([v for v_pair in dfs_result_9 for v in v_pair])
    dfs_2_vertex = set([v for v_pair in dfs_result_2 for v in v_pair])



    assert dfs_1_vertex == set(vertex) and dfs_2_vertex == set(vertex) and dfs_9_vertex == set(vertex)


def test_dfs_multiple():
    adj_list_1 = [
        (1, 4),
        (5, 4),
        (4, 8),
        (8, 13),
        (13, 9)
    ]

    adj_list_2 = [
        (3, 2),
        (3, 6),
        (6, 7),
        (2, 7),
        (2, 10),
        (10, 12),
        (10, 11)
    ]

    vertex_1 = set([v for v_pair in adj_list_1 for v in v_pair])
    vertex_2 = set([v for v_pair in adj_list_2 for v in v_pair])
    adj_list_mixed = mixer(adj_list_1 + adj_list_2)

    dfs_result_1 = dfs_iter(adj_list_mixed, 1)
    dfs_result_9 = dfs_iter(adj_list_mixed, 9)
    dfs_result_2 = dfs_iter(adj_list_mixed, 2)

    dfs_1_vertex = set([v for v_pair in dfs_result_1 for v in v_pair])
    dfs_9_vertex = set([v for v_pair in dfs_result_9 for v in v_pair])
    dfs_2_vertex = set([v for v_pair in dfs_result_2 for v in v_pair])

    assert dfs_1_vertex == vertex_1
    assert dfs_9_vertex == vertex_1
    assert dfs_2_vertex == vertex_2


def test_empty_dfs():
    result = dfs_iter([], 1)
    assert len(result) == 0


def test_single_node_dfs():
    result = dfs_iter([(1, 1)], 1)
    assert result == [(1, 1)]

