from dynamic.bellman_ford.bellman_ford import bellman_ford


def test_bellman_ford():
    adjacencies = [
        (0, 1, 2),
        (0, 2, 3),
        (1, 2, -7),
        (1, 3, 6),
        (2, 4, 4),
        (4, 3, -8),
        (3, 5, 2),
        (4, 5, -1),
    ]
    assert bellman_ford(adjacencies, 0) == [[0, 0], [0, 1], [0, 1, 2], [0, 1, 2, 4, 3], [0, 1, 2, 4], [0, 1, 2, 4, 3, 5]]
    assert bellman_ford(adjacencies, 2) == [[0], [1], [2, 2], [2, 4, 3], [2, 4], [2, 4, 3, 5]]
