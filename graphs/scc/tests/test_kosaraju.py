from graphs.scc.kosaraju import kosaraju


def test_dfs_scc():
    adj_list = [
        (1, 7),
        (7, 6),
        (6, 1),
        (1, 4),
        (6, 9),
        (4, 9),
        (9, 10),
        (10, 4),
        (4, 3),
        (3, 10),
        (10, 2),
        (3, 2),
        (2, 12),
        (12, 11),
        (11, 2),
        (6, 5),
        (5, 8),
        (8, 11),
        (6, 2)
    ]

    print(kosaraju(adj_list))
