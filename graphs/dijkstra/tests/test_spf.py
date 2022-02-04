from graphs.dijkstra.spf import dijkstra


def test_spf_1():
    edge_list = [
        ("a", "b", 1),
        ("a", "c", 5),
        ("b", "d", 6),
        ("c", "d", 8),
        ("c", "b", 1),
        ("e", "c", 5),
        ("d", "e", 2),
    ]

    result = dijkstra(edge_list, "a")

    assert result == {'a': (0, None), 'b': (1, 'a'), 'c': (2, 'b'), 'd': (7, 'b'), 'e': (7, 'c')}


def test_spf_2():
    edge_list = [
        ("a", "b", 1),
        ("a", "c", 10),
        ("b", "d", 5),
        ("c", "d", 105),
        ("c", "b", 1),
        ("e", "c", 100),
        ("d", "e", 40),
    ]

    result = dijkstra(edge_list, "a")

    print(result)