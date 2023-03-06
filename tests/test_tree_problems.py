from problems.data_structures.binary_tree import TreeNode
from problems.tree_problems import *


class TestIdenticalTree:
    def test_identical_trees(self):
        assert identical_trees(
            TreeNode().insert_multiple([27, 14, 35, 10, 19, 31, 42]),
            TreeNode().insert_multiple([27, 14, 35, 10, 19, 31, 42])
        )
        assert identical_trees(
            TreeNode().insert(555),
            TreeNode().insert(555)
        )

    def test_differing_trees(self):
        assert not identical_trees(
            TreeNode().insert(555),
            TreeNode().insert(333)
        )
        assert not identical_trees(
            TreeNode().insert_multiple([27, 14, 35, 10, 19, 31, 42]),
            TreeNode().insert_multiple([27, 14, 35, 10, 19, 31])
        )
        assert not identical_trees(
            TreeNode().insert_multiple([27, 14, 35, 11, 19, 31, 42]),
            TreeNode().insert_multiple([29, 14, 35, 10, 19, 31, 52])
        )
