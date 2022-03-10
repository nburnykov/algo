from dynamic.opt_bst.opt_bst import index_list


def test_index_list():
    assert index_list(5, 0) == [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (0, 1), (1, 2), (2, 3), (3, 4), (0, 2),
                                (1, 3), (2, 4), (0, 3), (1, 4), (0, 4)]

    assert index_list(5, 1) == [(0, 1), (1, 2), (2, 3), (3, 4), (0, 2), (1, 3), (2, 4), (0, 3), (1, 4), (0, 4)]

    assert index_list(1, 0) == [(0, 0)]
