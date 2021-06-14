"""
938. Range Sum of BST
Easy

2528

300

Add to List

Share
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

 

Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
 

Constraints:

The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.
Accepted
394,661
Submissions
472,665
"""

"""
Success
Details 
Runtime: 352 ms, faster than 18.18% of Python online submissions for Range Sum of BST.
Memory Usage: 29.5 MB, less than 90.12% of Python online submissions for Range Sum of BST.
Next challenges:
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    SUM = 0
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0
        
        if low <= root.val <= high:
            self.SUM += root.val
        
        self.rangeSumBST(root.left, low, high) 
        self.rangeSumBST(root.right, low, high) 
        
        return self.SUM

"""
Runtime: 244 ms, faster than 84.45% of Python online submissions for Range Sum of BST.
Memory Usage: 29.7 MB, less than 44.85% of Python online submissions for Range Sum of BST.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root: return 0
        
        if root.val < low: return self.rangeSumBST(root.right, low, high)
        if root.val > high: return self.rangeSumBST(root.left, low, high)
        
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high) 
