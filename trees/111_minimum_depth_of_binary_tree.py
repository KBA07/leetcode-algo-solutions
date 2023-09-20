"""
111. Minimum Depth of Binary Tree
Easy
6.9K
1.2K
Companies
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
 

Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
Accepted
1.1M
Submissions
2.3M
Acceptance Rate
46.5%
"""

"""
Runtime: 412ms Beats 64.30% of users with Python3.
Memory Usage: 57.96MB Beats 69.14% of users with Python3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ld = self.minDepth(root.left)
        rd = self.minDepth(root.right)

        if not root.left and not root.right:
            return 1
        
        if not root.left:
            return 1 + rd
        
        if not root.right:
            return 1 + ld

        return 1 + min(ld, rd)
        