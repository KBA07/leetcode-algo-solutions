"""
98. Validate Binary Search Tree
Medium

6689

727

Add to List

Share
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
Accepted
1,044,858
Submissions
3,567,139
"""

"""
Runtime: 40 ms, faster than 89.87% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 16.2 MB, less than 99.48% of Python3 online submissions for Validate Binary Search Tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, max_value, min_value):
            if not root:
                return True
            
            if root.val >= max_value or root.val <= min_value:
                return False
            
            return helper(root.left, root.val, min_value) and helper(root.right, max_value, root.val)
        
        return helper(root, float('inf'), float('-inf'))
        