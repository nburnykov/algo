from mst.prim.prim import mst_prim_basic


def test_prim_1():
    edges = [
        (4, 'a', 'b'),
        (2, 'a', 'd'),
        (3, 'b', 'd'),
        (1, 'a', 'c'),
        (5, 'c', 'd'),
    ]
    mst = mst_prim_basic(edges, 'a')

    assert mst == [(1, 'a', 'c'), (2, 'a', 'd'), (3, 'b', 'd')]

    edges = [
        (1, 'a', 'b'),
        (1, 'b', 'c'),
        (4, 'c', 'd'),
        (1, 'd', 'e'),
        (3, 'e', 'f'),
        (2, 'c', 'e'),
        (5, 'c', 'f'),
        (6, 'a', 'e'),
    ]
    mst = mst_prim_basic(edges, 'd')

    assert mst == [(1, 'd', 'e'), (2, 'c', 'e'), (1, 'b', 'c'), (1, 'a', 'b'), (3, 'e', 'f')]
