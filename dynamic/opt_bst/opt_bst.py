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

    def set_element(self, i: int, j: int, value: float):
        self.data[self._get_offset(i, j)] = value

    def get_element(self, i: int, j: int) -> float:
        return self.data[self._get_offset(i, j)]

    def _get_offset(self, i: int, j: int) -> int:
        if j < i:
            i, j = j, i
        j = j - i
        o = self.offsets[i] + j
        return o


def opt_bst(data: List[tuple]) -> object:
    pass
