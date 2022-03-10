###############################################################################################################
# Programming problem 17.8. Algorithms Illuminated. Part 3 by Tim Roughgarden
###############################################################################################################
from typing import List, Dict


class Symmetric2DArray:
    """
    A structure that emulates square 2D array which is symmetric and makes this in optimal way in terms of space
    """

    def __init__(self, width_height: int):
        self.offsets: Dict[int, int] = dict()
        lng = 0
        for i in range(width_height, -1, -1):
            self.offsets[width_height - i] = lng
            lng += i

        self.data = [None] * lng  # a single array to store the data
        self.width_height = width_height

    def set(self, i: int, j: int, value: float):
        self.data[self._get_offset(i, j)] = value

    def get(self, i: int, j: int) -> float:
        return self.data[self._get_offset(i, j)]

    def _get_offset(self, i: int, j: int) -> int:
        if j < i:
            i, j = j, i
        j = j - i
        o = self.offsets[i] + j
        return o


def index_list(width_height: int, offset: int) -> List[tuple]:
    """
    Right order of weight and root matrix indexes to calculate

    :param width_height: dimensions of square matrix
    :param offset: offset to start
    :return: list of indices
    """
    i = 0
    j = offset
    result = []
    while not (i == 0 and j == width_height):
        result.append((i, j))
        j += 1
        i += 1
        if j == width_height:
            offset += 1
            i = 0
            j = offset
    return result


def opt_bst(data: List[tuple]) -> List[tuple]:
    """
    Optimal binary search tree algorithm

    :param data: list of nodes in sorted order with their respective probabilities
    :return: list of the tree nodes in format [(root, left, right), ]
    """
    probabilities = Symmetric2DArray(len(data) + 1)
    weights = Symmetric2DArray(len(data) + 1)
    roots = Symmetric2DArray(len(data) + 1)

    for t in [probabilities, weights, roots]:  # zeroize the diagonals
        for i in range(t.width_height):
            t.set(i, i, 0)

    for i, (key, p) in enumerate(data):
        probabilities.set(i, i + 1, p)
        weights.set(i, i + 1, p)
        roots.set(i, i + 1, key)

    for i in range(0, probabilities.width_height - 2):  # fill the probabilities
        for j in range(i + 2, probabilities.width_height):
            p_a = probabilities.get(i, j - 1)
            p_b = probabilities.get(j - 1, j)
            probabilities.set(i, j, p_b + p_a)

    indices = index_list(weights.width_height, 2)

    for i, j in indices:
        weight_candidates = [
            (weights.get(i, i + k) + weights.get(i + k + 1, j), roots.get(i + k, i + k + 1))
            for k in range(j - i)]

        min_weight, min_root = min(weight_candidates, key=lambda x: x[0])

        weights.set(i, j, probabilities.get(i, j) + min_weight)
        roots.set(i, j, min_root)

    # reconstruction part
    discovery_queue = [(roots.get(0, roots.width_height - 1), 0, roots.width_height - 1)]
    discovered_nodes = {roots.get(0, roots.width_height - 1)}

    discovered_list = []

    while len(discovery_queue) > 0:

        current_left = None
        current_right = None

        current_node, node_i, node_j = discovery_queue.pop(-1)
        current_i = node_i
        current_j = node_j

        # discovery left
        while True:
            search_failed = False
            while current_j > current_i:
                discovered_node = roots.get(current_i, current_j)
                if discovered_node != current_node:
                    if discovered_node in discovered_nodes:
                        search_failed = True
                    else:
                        discovery_queue.append((discovered_node, current_i, current_j))
                        discovered_nodes.add(discovered_node)
                        current_left = discovered_node
                    break
                current_j -= 1

            if search_failed:
                current_i += 1  # shift to the left
                current_j = node_j
            else:
                break

        # discovery right
        current_i = node_i
        current_j = node_j
        while True:
            search_failed = False
            while current_j > current_i:
                discovered_node = roots.get(current_i, current_j)
                if discovered_node != current_node:
                    if discovered_node in discovered_nodes:
                        search_failed = True
                    else:
                        discovery_queue.append((discovered_node, current_i, current_j))
                        discovered_nodes.add(discovered_node)
                        current_right = discovered_node
                    break
                current_i += 1

            if search_failed:
                current_j -= 1  # shift to the right
                current_i = node_i
            else:
                break

        discovered_list.append((current_node, current_left, current_right))

    return discovered_list

