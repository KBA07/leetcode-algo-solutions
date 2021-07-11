"""
101. Symmetric Tree
Easy

6664

175

Add to List

Share
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?
Accepted
938,384
Submissions
1,905,298
"""

# DFS
"""
Runtime: 32 ms, faster than 82.21% of Python3 online submissions for Symmetric Tree.
Memory Usage: 14.2 MB, less than 92.14% of Python3 online submissions for Symmetric Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return 0
        
        return self.helper(root.left, root.right)
        
    
    def helper(self, first, second):
        if not first or not second:
            return first == second
        
        if first.val != second.val:
            return False
        
        return self.helper(first.left, second.right) and self.helper(first.right, second.left)

# BFS
"""
Runtime: 52 ms, faster than 9.32% of Python3 online submissions for Symmetric Tree.
Memory Usage: 14.2 MB, less than 77.87% of Python3 online submissions for Symmetric Tree.
""" 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return 0
        
        queue = [(root.left, root.right)]
        
        while queue:
            p, q = queue.pop(0)
            
            if not p and not q:
                continue
            
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            queue.append((p.left, q.right))
            queue.append((p.right, q.left))
        
        return True
        