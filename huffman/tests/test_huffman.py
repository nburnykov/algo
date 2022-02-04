from huffman.huffman import Huffman


def test_tree_create_1():
    alphabet = [('a', 0.5), ('b', 0.3), ('c', 0.2)]
    h = Huffman(alphabet)
    assert h.generate_code_map(h.tree) == {'b': '00', 'c': '01', 'a': '1'}

    alphabet = [('a', 0.16), ('b', 0.08), ('c', 0.35), ('d', 0.07), ('e', 0.34)]
    h = Huffman(alphabet)
    assert h.generate_code_map(h.tree) == {'e': '00', 'a': '010', 'b': '0110', 'd': '0111', 'c': '1'}

    alphabet = [('a', 1)]
    h = Huffman(alphabet)
    assert h.generate_code_map(h.tree) == {'a': '0'}

    alphabet = []
    h = Huffman(alphabet)
    assert h.generate_code_map(h.tree) == {}


def test_tree_create_2():
    alphabet = [('a', 0.16), ('b', 0.08), ('c', 0.35), ('d', 0.07), ('e', 0.34)]
    result_map = {'e': '00', 'a': '010', 'b': '0110', 'd': '0111', 'c': '1'}

    h1 = Huffman(alphabet, init_type='quadratic')
    assert h1.generate_code_map(h1.tree) == result_map
    h2 = Huffman(alphabet, init_type='sort')
    assert h2.generate_code_map(h2.tree) == result_map
    h3 = Huffman(alphabet, init_type='heap')
    assert h3.generate_code_map(h3.tree) == result_map
