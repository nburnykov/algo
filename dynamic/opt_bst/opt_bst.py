from typing import List, Dict


class Symmetric2DArray:
    """
    A structure that emulates square 2D array which is symmetric but makes this in optimal way
    """

    def __init__(self, width_height: int):
        self.offsets: Dict[int, int] = dict()
        lng = 0
        for i in range(width_height, -1, -1):
            self.offsets[width_height - i] = lng
            lng += i

        self.data = [None] * lng
        self.width_height = width_height

    def set_element(self, i: int, j: int, value: float):
        if j < i:
            i, j = j, i
        j = j - i

        self.data[self.offsets[i] + j] = value

    def get_element(self, i: int, j: int) -> float:
        if j < i:
            i, j = j, i
        j = j - i

        return self.data[self.offsets[i] + j]


def opt_bst(data: List[tuple]) -> object:
    pass
