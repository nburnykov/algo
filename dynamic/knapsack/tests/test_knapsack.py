from dynamic.knapsack.knapsack import knapsack


def test_knapsack():
    items = [
        (1, 3),
        (2, 6),
        (2, 1),
        (3, 2),
        (4, 1),
        (1, 5),
        (6, 3),
    ]

    assert knapsack(7, items) == (16, (0, 1, 3, 5))

    items = [
        (1, 5),
        (2, 1),
        (2, 7),
        (3, 4),
        (4, 2),
    ]

    assert knapsack(5, items) == (13, (0, 1, 2))
