from typing import Tuple, Optional


class Heap:
    def __init__(self):
        self.items = []
        self.objects = []

    def add(self, item: int, linked_object: object = None):
        self.items.append(item)
        self.objects.append(linked_object)

        index = len(self.items) - 1
        parent_index = self.get_parent(index)

        while self.items[index] < self.items[parent_index]:
            self._swap(index, parent_index)
            index = parent_index
            parent_index = self.get_parent(index)

    def _swap(self, index_1: int, index_2: int):
        self.items[index_1], self.items[index_2] = self.items[index_2], self.items[index_1]
        self.objects[index_1], self.objects[index_2] = self.objects[index_2], self.objects[index_1]

    def get_parent(self, child_index: int) -> int:
        if child_index == 0:
            return 0
        else:
            return (child_index - 1) // 2

    def get_children(self, parent_index: int) -> tuple:
        result = []
        for i in range(1, 3):
            candidate_index = 2 * parent_index + i
            if candidate_index < len(self.items):
                result.append(candidate_index)

        return tuple(result)

    def get_value(self, index: int) -> (int, object):
        return self.items[index], self.objects[index]

    def get_min(self) -> (int, object):
        return self.items[0], self.objects[0]

    def _get_smaller_child(self, index: int) -> Optional[int]:
        # given the index of current element return index of smaller child or None if no children are presented
        children_indexes = self.get_children(index)
        if len(children_indexes) == 0:
            return
        elif len(children_indexes) == 1:
            return children_indexes[0]
        else:
            index_1, index_2 = children_indexes
            return index_1 if self.items[index_1] <= self.items[index_2] else index_2

    def pop_min(self) -> (int, object):
        _min_item = self.items[0]
        _min_object = self.objects[0]
        self.items[0] = self.items.pop(len(self.items) - 1)
        self.objects[0] = self.objects.pop(len(self.items) - 1)
        inserted = False
        index = 0
        while not inserted:
            new_index = index
            smaller_child_index = self._get_smaller_child(index)
            if smaller_child_index:
                if self.items[index] > self.items[smaller_child_index]:
                    self._swap(smaller_child_index, index)
                    new_index = smaller_child_index
            inserted = new_index == index
            index = new_index
        return _min_item, _min_object
