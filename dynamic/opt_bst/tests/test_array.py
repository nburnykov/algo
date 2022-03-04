from dynamic.opt_bst.opt_bst import Symmetric2DArray


def test_array():
    a = Symmetric2DArray(5)
    a.set_element(4, 0, 1)

    assert a.get_element(4, 0) == 1 and a.get_element(0, 4) == 1

    a.set_element(2, 3, 5)

    assert a.get_element(2, 3) == 5 and a.get_element(3, 2) == 5

    a.set_element(4, 4, 5)

    assert a.get_element(4, 4) == 5
    assert a.get_element(4, 0) == 1 and a.get_element(0, 4) == 1
