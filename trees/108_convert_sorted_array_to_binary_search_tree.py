"""
Easy

4113

290

Add to List

Share
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

 

Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
Accepted
549,492
Submissions
888,973
"""
"""
Runtime: 52 ms, faster than 96.66% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 15.6 MB, less than 85.71% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def helper(start, end):
            if start > end: return
            mid = (start + end) // 2
            node = TreeNode(nums[mid])
            node.left = helper(start, mid - 1)
            node.right = helper(mid + 1, end)
            return node
        return helper(0, len(nums) - 1)