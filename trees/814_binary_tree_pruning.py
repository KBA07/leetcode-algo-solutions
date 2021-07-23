"""
814. Binary Tree Pruning
Medium

1796

59

Add to List

Share
Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.

 

Example 1:


Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.
Example 2:


Input: root = [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]
Example 3:


Input: root = [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]
 

Constraints:

The number of nodes in the tree is in the range [1, 200].
Node.val is either 0 or 1.
Accepted
106,066
Submissions
148,081
"""

"""
Runtime: 32 ms, faster than 63.33% of Python3 online submissions for Binary Tree Pruning.
Memory Usage: 14.3 MB, less than 57.04% of Python3 online submissions for Binary Tree Pruning.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        def dfs(node):
            if not node:
                return False
            
            contains_left = dfs(node.left)
            contains_right = dfs(node.right)
            
            if not contains_left:
                node.left = None
            
            if not contains_right:
                node.right = None
              
            return node.val or contains_left or contains_right
        
        return root if dfs(root) else None
        