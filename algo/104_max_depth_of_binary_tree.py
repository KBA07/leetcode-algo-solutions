"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""

"""
Runtime: 28 ms, faster than 87.74% of Python online submissions for Maximum Depth of Binary Tree.
Memory Usage: 15.8 MB, less than 12.60% of Python online submissions for Maximum Depth of Binary Tree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(node, sum):
            if not node:
                return sum
            return max(depth(node.left, sum+1), depth(node.right, sum+1))

        return depth(root, 0)

