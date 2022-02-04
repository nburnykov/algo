from random import shuffle

from graphs.toposort.toposort import topsort, dfs_sort


def test_dfs_sort():
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
        (10, 11),
        (4, 14),
        (14, 8),
        (4, 15),
        (15, 8),
        (4, 16),
        (16, 3)
    ]
    shuffle(adj_list)
    print(adj_list)
    # adj_list = [(2, 10), (2, 7), (5, 4), (3, 6), (4, 15), (14, 8), (4, 14), (13, 9), (4, 3), (1, 4), (15, 8), (4, 8), (3, 2), (6, 7), (10, 11), (4, 16), (16, 3), (10, 12), (8, 13)]

    print(dfs_sort(adj_list, 1))

    adj_list = [
        (1, 5),
        (1, 3),
        (1, 4),
        (5, 4),
        (5, 2),
        (2, 3),
        (4, 3)
    ]

    print(dfs_sort(adj_list, 1))


def test_toposort_single():
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
        (10, 11),
        (4, 14),
        (14, 8),
        (4, 15),
        (15, 8),
        (4, 16),
        (16, 3),
        (8, 2)
    ]

    shuffle(adj_list)

    result = topsort(adj_list)

    print(result)
