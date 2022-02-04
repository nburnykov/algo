###############################################################################################################
# Programming problem 14.6. Algorithms Illuminated. Part 2 by Tim Roughgarden
###############################################################################################################

from __future__ import annotations
from typing import List, Tuple, Optional

import heapq


class TreeNode:
    node_counter = 0  # global node counter

    def __init__(self):
        self.is_leaf: Optional[float] = None
        self.parent: Optional[TreeNode] = None
        self.child_left: Optional[TreeNode] = None
        self.child_right: Optional[TreeNode] = None
        self._symbol: Optional[str] = None
        self._frequency: Optional[float] = None
        self.node_id = TreeNode.node_counter
        TreeNode.node_counter += 1

    def set_symbol(self, symbol: str, frequency: float):
        if self.is_leaf is not None:
            raise ValueError(f'This node is initialized already')

        self._symbol = symbol
        self._frequency = frequency
        self.is_leaf = True

    @property
    def symbol(self) -> str:
        return self._symbol

    def set_child(self, node: TreeNode):
        if self.is_leaf:
            raise ValueError(f'This node is initialized already as leaf')

        if self.child_left and self.child_right:
            raise ValueError(f'This node has both children already')

        node.parent = self

        if not self.child_left:
            self.child_left = node
            return
        else:
            if self.child_left.frequency < node.frequency:
                self.child_right, self.child_left = self.child_left, node  # swap children to achieve bigger frequency on the left
            else:
                self.child_right = node

        self.is_leaf = False

    @property
    def frequency(self) -> Optional[float]:
        if self._frequency is not None:
            return self._frequency

        if self.child_right and self.child_left:
            self._frequency = self.child_right.frequency + self.child_left.frequency
            return self._frequency

        if self.child_left:
            return self.child_right.frequency  # self._frequency is not modified because of absent child on the right

        return


# a class to compare speed of Huffman prefix-free tree creation
class Huffman:
    def __init__(self, alphabet: List[Tuple[str, float]], init_type: str = 'quadratic'):
        self.alphabet = alphabet.copy()
        self.init_type = init_type
        self.least_frequent_symbol = None

        if init_type == 'quadratic':
            self.least_frequent_symbol = self._get_lfs_quadratic
        if init_type == 'heap':
            self.alphabet_heap = [(f, s) for s, f in self.alphabet]
            heapq.heapify(self.alphabet_heap)
            self.least_frequent_symbol = self._get_lfs_heap
        if init_type == 'sort':
            self.alphabet.sort(key=lambda x: x[1])
            self.least_frequent_symbol = self._get_lfs_sort

        if not self.least_frequent_symbol:
            raise ValueError('Wrong init_type value. Possible types are "quadratic", "heap" or "sort"')

        self.tree = self._create_code_tree()

    def _get_lfs_quadratic(self) -> Optional[(str, float)]:
        if len(self.alphabet) > 1:
            min_index = 0
            for i in range(1, len(self.alphabet)):  # finding minimum in the most cumbersome way
                if self.alphabet[i][1] < self.alphabet[min_index][1]:
                    min_index = i
            return self.alphabet.pop(min_index)

        if len(self.alphabet) == 1:
            return self.alphabet.pop(0)

        return

    def _get_lfs_heap(self) -> Optional[(str, float)]:
        if len(self.alphabet_heap) > 0:
            f, s = heapq.heappop(self.alphabet_heap)
            return s, f

        return

    def _get_lfs_sort(self) -> Optional[(str, float)]:
        if len(self.alphabet) > 0:
            return self.alphabet.pop(0)

        return

    def _create_code_tree(self) -> Optional[TreeNode]:
        nodes_list = []
        while True:
            parent_node = TreeNode()
            for _ in range(2):
                candidate = self.least_frequent_symbol()
                if candidate:
                    n = TreeNode()
                    n.set_symbol(candidate[0], candidate[1])
                    nodes_list.append((n.frequency, n))
            if len(nodes_list) > 1:
                nodes_list.sort(key=lambda x: x[0])  # list contains 3 records at max
                parent_node.set_child(nodes_list.pop(0)[1])
                parent_node.set_child(nodes_list.pop(0)[1])
            elif len(nodes_list) == 1:
                return nodes_list.pop(0)[1]
            else:
                return
            nodes_list.append((parent_node.frequency, parent_node))

    @staticmethod
    def generate_code_map(tree: TreeNode) -> dict:
        result = dict()
        nodes_seen = set()
        node_queue = [tree]
        node_codes = dict()

        if not tree:
            return {}

        while len(node_queue) > 0:
            current_node = node_queue[0]

            if current_node.is_leaf:
                result[current_node.symbol] = ''.join(node_codes.get(current_node.node_id, '0'))

            else:
                if current_node.child_left.node_id not in nodes_seen:  # DFS jump to left
                    node_codes[current_node.child_left.node_id] = node_codes.get(current_node.node_id, []) + ['0']
                    node_queue.insert(0, current_node.child_left)
                    continue

                if current_node.child_right.node_id not in nodes_seen:  # DFS jump to right
                    node_codes[current_node.child_right.node_id] = node_codes.get(current_node.node_id, []) + ['1']
                    node_queue.insert(0, current_node.child_right)
                    continue

            nodes_seen.add(current_node.node_id)
            node_queue.pop(0)

        return result
