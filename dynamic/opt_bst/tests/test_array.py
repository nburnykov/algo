from dynamic.opt_bst.opt_bst import Symmetric2DArray


def test_array():
    a = Symmetric2DArray(5)
    a.set(4, 0, 1)

    assert a.get(4, 0) == 1 and a.get(0, 4) == 1

    a.set(2, 3, 5)

    assert a.get(2, 3) == 5 and a.get(3, 2) == 5

    a.set(4, 4, 5)

    assert a.get(4, 4) == 5
    assert a.get(4, 0) == 1 and a.get(0, 4) == 1
