"""
226. Invert Binary Tree
Easy

5768

82

Add to List

Share
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
Accepted
746,613
Submissions
1,091,169
"""

"""
Runtime: 28 ms, faster than 87.73% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 14.1 MB, less than 73.59% of Python3 online submissions for Invert Binary Tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        
        root.left = right
        root.right = left
        
        return root

"""
Runtime: 28 ms, faster than 87.73% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 14.2 MB, less than 44.33% of Python3 online submissions for Invert Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        queue = []
        queue.append(root)
        
        while queue:
            node = queue.pop()
            
            node.left, node.right = node.right, node.left
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        return root