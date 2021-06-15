"""
Share
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

 

Example 1:


Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
Example 2:

Input: root1 = [1], root2 = [1,2]
Output: [2,2]
 

Constraints:

The number of nodes in both trees is in the range [0, 2000].
-104 <= Node.val <= 104
Accepted
402,697
Submissions
530,609
"""
"""
Runtime: 72 ms, faster than 90.92% of Python online submissions for Merge Two Binary Trees.
Memory Usage: 14.5 MB, less than 61.14% of Python online submissions for Merge Two Binary Trees.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        
        if not root1:
            return root2
        
        if not root2:
            return root1
        
        root1.val += root2.val
        
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1

"""
Iterative approach
Runtime: 76 ms, faster than 76.03% of Python online submissions for Merge Two Binary Trees.
Memory Usage: 14.6 MB, less than 41.40% of Python online submissions for Merge Two Binary Trees.
"""

class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if not root1:
            return root2
        
        stack = []
        stack.append((root1, root2))
        
        while len(stack) != 0:
            node1, node2 = stack.pop()
            
            if not node1 or not node2:
                continue
                
            node1.val += node2.val
                
            if not node1.left:
                node1.left = node2.left
            else:
                stack.append((node1.left, node2.left))
                
            
            if not node1.right:
                node1.right = node2.right
            else:
                stack.append((node1.right, node2.right))
        
        return root1
