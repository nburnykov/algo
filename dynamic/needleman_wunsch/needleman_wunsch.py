###############################################################################################################
# Programming problem 17.8. Algorithms Illuminated. Part 2 by Tim Roughgarden
###############################################################################################################

def needleman_wunsch(sequence_one: str, sequence_two: str) -> (str, str):
    """
    Another famous example of dynamic programming
    An algo that performs an alignment of two sequences
    For example

    Before:       After:
    ACGGCTC    -> ACGGCT-C
    ATGGCCTC   -> ATGGCCTC

    AGGTTCCA   -> AGGTTCCA
    ATA        -> A--T---A

    :param sequence_one: first sequence
    :param sequence_two: second sequence
    :return: a tuple with two aligned sequences
    """
    _sequence_one = '-' + sequence_one
    _sequence_two = '-' + sequence_two

    mismatch_penalty = 2
    gap_penalty = 1

    matrix = [[0] * (len(_sequence_one)) for _ in range(len(_sequence_two))]

    for i in range(len(matrix[0])):
        matrix[0][i] = i * gap_penalty

    for i in range(len(matrix)):
        matrix[i][0] = i * gap_penalty

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if _sequence_two[i] != _sequence_one[j]:
                cost_direct = matrix[i - 1][j - 1] + mismatch_penalty
            else:
                cost_direct = matrix[i - 1][j - 1]

            cost_gap_1 = matrix[i - 1][j] + gap_penalty
            cost_gap_2 = matrix[i][j - 1] + gap_penalty

            matrix[i][j] = min([cost_direct, cost_gap_1, cost_gap_2])

    # reconstruction part
    i = len(matrix) - 1
    j = len(matrix[0]) - 1

    result_sequence_one = []
    result_sequence_two = []

    while i > 0 or j > 0:

        candidates = []
        if j > 0:
            candidates.append((matrix[i][j - 1], i, j - 1, _sequence_one[j], '-'))
        if i > 0:
            candidates.append((matrix[i - 1][j], i - 1, j, '-', _sequence_two[i]))
        if i > 0 and j > 0:
            candidates.append((matrix[i - 1][j - 1], i - 1, j - 1, _sequence_one[j], _sequence_two[i]))

        _, i, j, next_letter_seq_one, next_letter_seq_two = min(candidates, key=lambda x: x[0])

        result_sequence_one.append(next_letter_seq_one)
        result_sequence_two.append(next_letter_seq_two)

    return ''.join(reversed(result_sequence_one)), ''.join(reversed(result_sequence_two))
