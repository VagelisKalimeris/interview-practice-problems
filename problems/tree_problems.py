################################################################################
# Objective         : You are given the roots of two binary trees and must     #
#                     determine if these trees are identical. Identical trees  #
#                     have the same layout and data at each node.              #
# Time Complexity   : O(n)                                                     #
# Space Complexity  : O(n)                                                     #
################################################################################
def identical_trees(root_1, root_2):
    if root_1 and root_2:
        if root_1.data != root_2.data:
            return False
        return identical_trees(root_1.lc, root_2.lc) \
            and identical_trees(root_1.rc, root_2.rc)
    return not (root_1 or root_2)
