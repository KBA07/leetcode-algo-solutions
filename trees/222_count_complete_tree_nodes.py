"""
222. Count Complete Tree Nodes
Easy
8.1K
450
Companies
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
Accepted
607.2K
Submissions
969.6K
Acceptance Rate
62.6%
"""

"""
Runtime: 74ms Beats 60.92% of users with Python3
Memory Usage: 23.59MB Beats 97.46% of users with Python3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

## Level Order

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        queue = [root]
        count = 0
        while queue:
            node = queue.pop(0)
            if node: 
                count += 1 

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return count

         