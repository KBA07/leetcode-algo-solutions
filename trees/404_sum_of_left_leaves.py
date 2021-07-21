"""
404. Sum of Left Leaves
Easy

2060

192

Add to List

Share
Given the root of a binary tree, return the sum of all left leaves.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000
Accepted
260,029
Submissions
492,780
"""

"""
Runtime: 28 ms, faster than 90.22% of Python3 online submissions for Sum of Left Leaves.
Memory Usage: 14.4 MB, less than 93.69% of Python3 online submissions for Sum of Left Leaves.
"""

# BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        queue = [root]
        answer = 0
        while queue:
            
            queue_size = len(queue)
            
            for _ in range(queue_size):
                node = queue.pop(0)
                
                if node.left:
                    if not node.left.left and not node.left.right: # this is a leaf node
                        answer += node.left.val
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
        
        return answer

# DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
    
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
