from problems.array_problems import *


class TestSumOfThree:
    def test_existing_sums(self):
        assert contains_sum_of_3(9, [1, 2, 3, 5, 3, 1, 3])
        assert contains_sum_of_3(9, [1, 2, 3, 5, 3, 1, 3])
        assert contains_sum_of_3(5, [1, 2, 3, 5, 3, 1, 3])

    def test_non_existing_sums(self):
        assert not contains_sum_of_3(10, [1, 2, 3, 5, 3, 1, 3])
        assert not contains_sum_of_3(12, [1, 2, 3, 5, 3, 1, 3])
