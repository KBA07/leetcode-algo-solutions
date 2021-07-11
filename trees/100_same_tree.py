"""
100. Same Tree
Easy

3569

94

Add to List

Share
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
Accepted
759,897
Submissions
1,393,207
"""

"""
Runtime: 32 ms, faster than 60.25% of Python3 online submissions for Same Tree.
Memory Usage: 14.3 MB, less than 61.44% of Python3 online submissions for Same Tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        
        if (p and not q) or (q and not p) or (p.val != q.val):
            return False
             
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and True