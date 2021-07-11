"""
104. Maximum Depth of Binary Tree
Easy

4319

102

Add to List

Share
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
Example 3:

Input: root = []
Output: 0
Example 4:

Input: root = [0]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
Accepted
1,200,414
Submissions
1,736,140
"""

# BFS
"""
Runtime: 64 ms, faster than 7.64% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 15.4 MB, less than 82.35% of Python3 online submissions for Maximum Depth of Binary Tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        
        queue = [root]
        depth = 0
        remaining_level_nodes = 1
        
        while queue:
            node = queue.pop(0)
            remaining_level_nodes -= 1
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
            
            if remaining_level_nodes == 0:
                depth += 1
                remaining_level_nodes = len(queue)
        
        return depth
        