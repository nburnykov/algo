###############################################################################################################
# Programming problem 16.7. Algorithms Illuminated. Part 3 by Tim Roughgarden
###############################################################################################################

from typing import Union, Tuple, List


def knapsack(max_weight: int, items: List[Tuple[int, int]]) -> (int, Tuple[int]):
    """
    Another implementation of well known knapsack problem.
    Given a set of items each with its own weight and value fill the weight limited knapsack maximizing the overall
    value
    For the simplicity all the parameters such as max weight, item weight and item value are integers
    :param max_weight:
    :param items:
    :return:
    """

    # max value part
    value_matrix = [[0] * (max_weight + 1) for _ in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        current_weight, current_value = items[i - 1]
        for w in range(max_weight + 1):
            if current_weight > w:
                value_matrix[i][w] = value_matrix[i - 1][w]
            else:
                added_value = value_matrix[i - 1][w - current_weight] + current_value
                if added_value > value_matrix[i - 1][w]:
                    value_matrix[i][w] = added_value
                else:
                    value_matrix[i][w] = value_matrix[i - 1][w]

    max_value = value_matrix[-1][-1]

    # items indexes reconstruction part
    indexes = []
    i_weight = max_weight

    for i in range(len(items) - 1, -1, -1):
        current_weight, current_value = items[i]
        if current_weight <= i_weight:
            added_value = value_matrix[i][i_weight - current_weight] + current_value
            if added_value >= value_matrix[i][i_weight]:
                indexes.append(i)
                i_weight -= current_weight

    return max_value, tuple(sorted(indexes))




