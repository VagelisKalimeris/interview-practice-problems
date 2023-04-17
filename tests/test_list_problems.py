import pytest
from problems.list_problems import SingleListNode, merge_sorted_lists, \
    find_loop_in_list, add_inv_int_lists


class TestSortedListMerging:
    def test_sorted_list_merging(self):
        assert merge_sorted_lists(
                SingleListNode().append_multi([50, 70, 80, 110, 140]),
                SingleListNode().append_multi([60, 70, 120, 150, 160])
            ).list_is_identical_with(
            SingleListNode().append_multi([50, 60, 70, 70, 80, 110, 120, 140, 150, 160])
        )
        assert merge_sorted_lists(
                SingleListNode().append_multi([50, 70, 80, 110, 140]),
                SingleListNode().append_multi([10, 20, 120, 160])
            ).list_is_identical_with(
            SingleListNode().append_multi([10, 20, 50, 70, 80, 110, 120, 140, 160])
        )

    def test_edge_case_sorted_list_merging(self):
        assert merge_sorted_lists(
                SingleListNode().append_multi([50, 70, 80, 110, 140]),
                SingleListNode(0)
            ).list_is_identical_with(
            SingleListNode().append_multi([0, 50, 70, 80, 110, 140])
        )
        assert merge_sorted_lists(
                SingleListNode(55),
                SingleListNode().append_multi([10, 20, 120, 160])
            ).list_is_identical_with(
            SingleListNode().append_multi([10, 20, 55, 120, 160])
        )
        assert merge_sorted_lists(
                SingleListNode().append_multi([50, 70, 80, 110, 140]),
                SingleListNode().append_multi([0, 1000])
            ).list_is_identical_with(
            SingleListNode().append_multi([0, 50, 70, 80, 110, 140, 1000])
        )


class TestLoopFinding:
    @pytest.fixture
    def test_list(self):
        return SingleListNode().append_multi([15, 35, 55, 99, 12, 17, 52])

    def test_non_existing_loop(self, test_list):
        assert not find_loop_in_list(test_list)

    def test_existing_loop(self, test_list):
        test_list.create_loop_in_list(2, 5)
        assert find_loop_in_list(test_list)


class TestIntegerAddition:
    def test_add_inverted_integer_lists(self):
        # 9901 + 237 = 10138
        assert add_inv_int_lists(
                SingleListNode().append_multi(['1', '0', '9', '9']),
                SingleListNode().append_multi(['7', '3', '2'])
            ).get_int_in_inv_list() == 10138
        # 199 + 1 = 200
        assert add_inv_int_lists(
                SingleListNode().append_multi(['9', '9', '1']),
                SingleListNode().append_multi(['1'])
            ).get_int_in_inv_list() == 200
        # 45 + 20 = 65
        assert add_inv_int_lists(
                SingleListNode().append_multi(['5', '4', '0']),
                SingleListNode().append_multi(['0', '2', '0', '0'])
            ).get_int_in_inv_list() == 65
