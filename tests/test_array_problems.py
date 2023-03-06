from problems.array_problems import *


class TestSumOfThree:
    def test_existing_sums(self):
        assert contains_sum_of_3(9, [1, 2, 3, 5, 3, 1, 3])
        assert contains_sum_of_3(9, [1, 2, 3, 5, 3, 1, 3])
        assert contains_sum_of_3(5, [1, 2, 3, 5, 3, 1, 3])

    def test_non_existing_sums(self):
        assert not contains_sum_of_3(10, [1, 2, 3, 5, 3, 1, 3])
        assert not contains_sum_of_3(12, [1, 2, 3, 5, 3, 1, 3])


class TestFirstAndLast:
    def test_existing_occurrences(self):
        assert first_and_last([5, 6, 13, 4, 7, 7, 9, 46], 7) == (4, 5)
        assert first_and_last([1, 3, 5, 5, 5, 5, 67, 123, 125], 5) == (2, 5)
        assert first_and_last([123, 3, 5, 5, 5, 5, 67, 123, 125], 123) == (0, 7)

    def test_single_occurrence(self):
        assert first_and_last([5, 6, 13, 4, 7, 7, 9, 46], 13) == (2, 2)
        assert first_and_last([5, 6, 13, 4, 7, 7, 9, 46], 46) == (7, 7)

    def test_no_occurrence(self):
        assert first_and_last([5, 6, 13, 4, 7, 7, 9, 46], 256) == (None, None)

    def test_edge_cases(self):
        assert first_and_last([], 7) == (None, None)
        assert first_and_last([], None) == (None, None)
        assert first_and_last([7], 7) == (0, 0)
        assert first_and_last([7], 9) == (None, None)
