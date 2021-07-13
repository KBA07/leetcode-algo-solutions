"""
199. Binary Tree Right Side View
Medium

4365

234

Add to List

Share
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
Accepted
479,696
Submissions
837,929
"""

"""
Runtime: 36 ms, faster than 41.41% of Python3 online submissions for Binary Tree Right Side View.
Memory Usage: 14.3 MB, less than 52.30% of Python3 online submissions for Binary Tree Right Side View.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return root
        
        queue = [root]
        answer = [root.val]
        level_nodes = 1
        while queue:
            node = queue.pop(0)
            level_nodes -= 1
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
            if level_nodes == 0 and queue:
                level_nodes = len(queue)
                answer.append(queue[-1].val)
        
        return answer

"""
Runtime: 56 ms, faster than 6.45% of Python3 online submissions for Binary Tree Right Side View.
Memory Usage: 14 MB, less than 93.16% of Python3 online submissions for Binary Tree Right Side View.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return root
        
        queue = [root]
        answer = []
        while queue:
            size = len(queue)
            for index in range(size):
                node = queue.pop(0)
                
                if index == size - 1:
                    answer.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return answer
