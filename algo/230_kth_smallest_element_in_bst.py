"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.



Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""
"""
Runtime: 48 ms, faster than 61.65% of Python online submissions for Kth Smallest Element in a BST.
Memory Usage: 20.8 MB, less than 9.10% of Python online submissions for Kth Smallest Element in a BST.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        val = []
        def visit(node):
            if not node:
                return

            visit(node.left)
            val.append(node.val)
            visit(node.right)

        visit(root)
        return val[k-1]

"""
Runtime: 52 ms, faster than 47.78% of Python online submissions for Kth Smallest Element in a BST.
Memory Usage: 20.6 MB, less than 75.36% of Python online submissions for Kth Smallest Element in a BST.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.val = None
        self.k = k

        def visit(node):
            if not node:
                return

            visit(node.left)
            if self.k == 1:
                self.val = node.val
            self.k -= 1
            visit(node.right)

        visit(root)
        return self.val

