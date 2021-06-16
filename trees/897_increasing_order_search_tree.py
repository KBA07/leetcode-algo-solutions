"""
897. Increasing Order Search Tree
Easy

1516

539

Add to List

Share
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

 

Example 1:


Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
Example 2:


Input: root = [5,1,7]
Output: [1,null,5,null,7]
 

Constraints:

The number of nodes in the given tree will be in the range [1, 100].
0 <= Node.val <= 1000
Accepted
130,047
Submissions
173,563
"""

"""
Runtime: 24 ms, faster than 37.06% of Python online submissions for Increasing Order Search Tree.
Memory Usage: 13.6 MB, less than 21.68% of Python online submissions for Increasing Order Search Tree.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    treenode = None
    head = None
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return

        self.increasingBST(root.left)

        node = TreeNode(root.val)
        if not self.treenode:
            self.treenode = node
            self.head = self.treenode
        else: 
            self.treenode.right = node
            self.treenode = self.treenode.right

        self.increasingBST(root.right)
        
        return self.head

"""
Runtime: 24 ms, faster than 37.06% of Python online submissions for Increasing Order Search Tree.
Memory Usage: 13.9 MB, less than 6.29% of Python online submissions for Increasing Order Search Tree.
"""

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        self.current = TreeNode()
        curr = self.current

        def ibst(node):
            
            if not node: return
            
            ibst(node.left)
            
            node.left = None
            self.current.right = node
            self.current = self.current.right
            
            ibst(node.right)
        
        ibst(root)

        return curr.right
