"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

"""
Runtime: 32 ms, faster than 89.46% of Python online submissions for Validate Binary Search Tree.
Memory Usage: 17.5 MB, less than 41.14% of Python online submissions for Validate Binary Search Tree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        left = float('-inf')
        right = float('+inf')

        def bstChecker(left_extreme, right_extreme, node):

            if not node:
                return True

            return left_extreme < node.val < right_extreme and bstChecker(left_extreme, node.val, node.left) and bstChecker(node.val, right_extreme, node.right)

        return bstChecker(left, right, root)

