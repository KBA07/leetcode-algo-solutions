"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""
"""
Runtime: 72 ms, faster than 33.43% of Python online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 17 MB, less than 49.97% of Python online submissions for Convert Sorted Array to Binary Search Tree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        start = 0
        end = len(nums) - 1

        def insert(left, right):

            if left > right:
                return

            mid = (left + right) // 2

            node = TreeNode(nums[mid])

            node.left = insert(left, mid - 1)
            node.right = insert(mid+1, right)

            return node

        return insert(start, end)
