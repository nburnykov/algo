from random import random, shuffle
from typing import List

from graphs.bfs.bfs import bfs


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


def test_bfs_single():
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
    bfs_result_1 = bfs(adj_list_mixed, 1)
    bfs_result_9 = bfs(adj_list_mixed, 9)
    bfs_result_2 = bfs(adj_list_mixed, 2)

    bfs_1_vertex = set([v for v_pair in bfs_result_1 for v in v_pair])
    bfs_9_vertex = set([v for v_pair in bfs_result_9 for v in v_pair])
    bfs_2_vertex = set([v for v_pair in bfs_result_2 for v in v_pair])

    assert bfs_1_vertex == set(vertex) and bfs_2_vertex == set(vertex) and bfs_9_vertex == set(vertex)


def test_bfs_multiple():
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

    bfs_result_1 = bfs(adj_list_mixed, 1)
    bfs_result_9 = bfs(adj_list_mixed, 9)
    bfs_result_2 = bfs(adj_list_mixed, 2)

    bfs_1_vertex = set([v for v_pair in bfs_result_1 for v in v_pair])
    bfs_9_vertex = set([v for v_pair in bfs_result_9 for v in v_pair])
    bfs_2_vertex = set([v for v_pair in bfs_result_2 for v in v_pair])

    assert bfs_1_vertex == vertex_1
    assert bfs_9_vertex == vertex_1
    assert bfs_2_vertex == vertex_2


def test_empty_bfs():
    result = bfs([], 1)
    assert len(result) == 0


def test_single_node_bfs():
    result = bfs([(1, 1)], 1)
    assert result == [(1, 1)]

