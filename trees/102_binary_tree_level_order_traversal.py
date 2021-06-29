"""
102. Binary Tree Level Order Traversal
Medium

5125

111

Add to List

Share
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
Accepted
890,456
Submissions
1,536,115
"""

"""
Runtime: 36 ms, faster than 61.52% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 14.3 MB, less than 99.56% of Python3 online submissions for Binary Tree Level Order Traversal.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        stack = [root]
        result = []
        
        if not root:
            return result
        
        while len(stack) > 0:
            stack_len = len(stack)
            temp_result = []
            for index in range(stack_len):
                node = stack.pop(0)
                
                temp_result.append(node.val)
                
                if node.left:
                    stack.append(node.left)
                    
                if node.right:
                    stack.append(node.right)
            
            result.append(temp_result)
        
        return result