from mst.kruskal.kruskal import UnionFind


def test_union_find_1():

    test_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    uf = UnionFind(test_list)

    assert not uf.is_same_root('a', 'b')

    uf.union('a', 'b')

    assert uf.is_same_root('a', 'b')

    uf.union('a', 'c')
    uf.union('b', 'd')
    uf.union('e', 'f')
    uf.union('f', 'g')

    assert uf.is_same_root('a', 'd')
    assert not uf.is_same_root('c', 'e')


def test_union_find_2():

    test_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    uf = UnionFind(test_list)

    uf.union('a', 'b')
    uf.union('b', 'c')
    uf.union('d', 'c')
    uf.union('d', 'e')
    uf.union('f', 'e')
    uf.union('f', 'g')

    for item in test_list:
        assert uf.get_root(item)[0] == 'a'

