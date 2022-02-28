from dynamic.needleman_wunsch.needleman_wunsch import needleman_wunsch


def test_alignment_1():
    str1, str2 = needleman_wunsch("ACATAG", "AGTACG")
    assert str1 == "ACATA-G" and str2 == "A-GTACG"

    str1, str2 = needleman_wunsch("ACGGCTC", "ATGGCCTC")
    assert str1 == "ACGGC-TC" and str2 == "ATGGCCTC"

    str1, str2 = needleman_wunsch("AGGTTCCA", "ATA")
    assert str1 == "AGGTTCCA" and str2 == "A--T---A"


def test_alignment_2():
    str1, str2 = needleman_wunsch("AGGTTCCA", "")
    assert str1 == "AGGTTCCA" and str2 == "--------"
