from heaps.base.heap import Heap


def test_insert_items():
    h = Heap()

    h.add(4)
    h.add(8)

    assert h.items == [4, 8]

    h.add(2)

    assert h.items == [2, 8, 4]

    h.add(10)
    h.add(15)
    h.add(6, 'number six')
    h.add(9)
    h.add(9)

    assert h.items == [2, 8, 4, 9, 15, 6, 9, 10]

    h.add(1, 'number one')

    assert h.items == [1, 2, 4, 8, 15, 6, 9, 10, 9]
    assert h.objects == ['number one', None, None, None, None, 'number six', None, None, None]

    assert h.get_min() == (1, 'number one')
    assert h.get_value(5) == (6, 'number six')


def test_pop_items():
    h = Heap()

    h.add(4)
    h.add(8)
    h.add(2)
    h.add(10)
    h.add(15)
    h.add(6, 'number six')
    h.add(9)
    h.add(12)
    h.add(1, 'number one')

    assert h.pop_min() == (1, 'number one')
    assert h.items == [2, 8, 4, 10, 15, 6, 9, 12]

    assert h.pop_min() == (2, None)
    assert h.items == [4, 8, 6, 10, 15, 12, 9]