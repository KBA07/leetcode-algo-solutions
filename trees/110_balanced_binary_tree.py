"""
110. Balanced Binary Tree
Easy
9.8K
560
Companies
Given a binary tree, determine if it is 
height-balanced
.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
Accepted
1.2M
Submissions
2.4M
Acceptance Rate
50.3%
"""

"""
Runtime: 61ms Beats 34.86% of users with Python3
Memory Usage: 21.00MB Beats 94.71% of users with Python3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(node):
            if not node: return 0

            left, right = helper(node.left), helper(node.right)

            if abs(left - right) > 1 or left < 0 or right < 0: return -1

            return max(left, right) + 1

        return helper(root) > -1
        