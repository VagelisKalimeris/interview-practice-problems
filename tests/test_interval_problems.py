from problems.data_structures.interval import Interval
from problems.interval_problems import merge_overlapping_intervals


class TestOverlapMerge:
    def test_with_overlapping_merges(self):
        assert merge_overlapping_intervals(
            [Interval(10, 12), Interval(12, 15)]
        ) == [Interval(10, 15)]
        assert merge_overlapping_intervals(
            [Interval(1, 5), Interval(3, 7), Interval(4, 6), Interval(6, 8)]
        ) == [Interval(1, 8)]
        assert merge_overlapping_intervals(
            [Interval(1, 5), Interval(3, 7), Interval(8, 9), Interval(8, 12)]
        ) == [Interval(1, 7), Interval(8, 12)]
        assert merge_overlapping_intervals(
            [Interval(1, 5), Interval(3, 7), Interval(8, 9), Interval(10, 12)]
        ) == [Interval(1, 7), Interval(8, 9), Interval(10, 12)]
        assert merge_overlapping_intervals(
            [Interval(1, 5), Interval(3, 7), Interval(8, 9), Interval(9, 10),
             Interval(10, 11), Interval(11, 12)]
        ) == [Interval(1, 7), Interval(8, 12)]

    def test_edge_intervals(self):
        assert merge_overlapping_intervals(
            [Interval(13, 15)]
        ) == [Interval(13, 15)]
        assert merge_overlapping_intervals(
            []
        ) == []

    def test_with_no_overlapping_merges(self):
        assert merge_overlapping_intervals(
            [Interval(10, 12), Interval(13, 15)]
        ) == [Interval(10, 12), Interval(13, 15)]
        assert merge_overlapping_intervals(
            [Interval(1, 2), Interval(3, 7), Interval(8, 9), Interval(10, 12)]
        ) == [Interval(1, 2), Interval(3, 7), Interval(8, 9), Interval(10, 12)]
