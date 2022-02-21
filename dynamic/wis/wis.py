###############################################################################################################
# Programming problem 16.6. Algorithms Illuminated. Part 2 by Tim Roughgarden
###############################################################################################################
from typing import Union


def weighted_independent_set(node_weights: list) -> (Union[int, float], tuple):
    """
    an algo that calculates max sum of all independent (not connected directly) nodes in path graph

    For example:
    Node 0: cost 3 -> Node 1: cost 2 - Node 2: cost 1 -> Node 3: cost 6 - Node 4: cost 4 - Node 5: cost 5
    max sum for this graph will be 3 + 6 + 5 = 14  and respective nodes list is [0, 3, 5]

    :param node_weights: a list that represents node costs in path graph
    :return: a tuple (max sum, node sequence)
    """
    if len(node_weights) == 0:
        return 0, []

    _agg_weights = node_weights.copy()
    _agg_weights.insert(0, 0)

    for i in range(2, len(_agg_weights)):
        independent_sum = _agg_weights[i - 2] + _agg_weights[i]
        if independent_sum > _agg_weights[i - 1]:
            _agg_weights[i] = independent_sum
        else:
            _agg_weights[i] = _agg_weights[i - 1]

    node_list = []
    i = len(_agg_weights) - 1

    while i >= 2:  # node index reconstruction O(n)
        if _agg_weights[i - 2] + node_weights[i - 1] <= _agg_weights[i - 1]:
            i -= 1
        else:
            node_list.append(i - 1)  # index corrected because length of _agg_weights is n+1 of node_weights
            i -= 2
    if i == 1:
        node_list.append(i - 1)  # index corrected because length of _agg_weights is n+1 of node_weights

    return _agg_weights[-1], tuple(reversed(node_list))
