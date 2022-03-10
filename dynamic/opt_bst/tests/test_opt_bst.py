from dynamic.opt_bst.opt_bst import opt_bst


def test_opt_bst_one():
    array = [('a', 5), ('b', 10), ('c', 2), ('d', 3), ('e', 4)]
    assert set(opt_bst(array)) == \
           {('b', 'a', 'd'), ('d', 'c', 'e'), ('e', None, None), ('c', None, None), ('a', None, None)}


def test_opt_bst_two():
    array = [('a', 5), ('b', 10), ('c', 2), ('d', 3), ('e', 4), ('f', 15), ('g', 1)]
    assert set(opt_bst(array)) == \
           {('f', 'b', 'g'), ('g', None, None), ('b', 'a', 'd'), ('d', 'c', 'e'), ('e', None, None), ('c', None, None),
            ('a', None, None)}


def test_opt_bst_three():
    array = [('a', 5), ('b', 10), ('c', 2), ('d', 3), ('e', 4), ('f', 15)]
    assert set(opt_bst(array)) == \
           {('b', 'a', 'f'), ('f', 'd', None), ('d', 'c', 'e'), ('e', None, None), ('c', None, None), ('a', None, None)}
