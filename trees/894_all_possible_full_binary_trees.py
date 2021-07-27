"""
894. All Possible Full Binary Trees
Medium

1705

145

Add to List

Share
Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

 

Example 1:


Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Example 2:

Input: n = 3
Output: [[0,0,0]]
 

Constraints:

1 <= n <= 20
Accepted
59,132
Submissions
75,576
"""

"""
Runtime: 196 ms, faster than 60.68% of Python3 online submissions for All Possible Full Binary Trees.
Memory Usage: 16.8 MB, less than 95.02% of Python3 online submissions for All Possible Full Binary Trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    cache = {0:[], 1:[TreeNode(0)]}
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        
        if n not in self.cache:
            result = []
            
            for i in range(n):
                j = n - (i + 1) # since i starts at 0
                for left in self.allPossibleFBT(i):
                    for right in self.allPossibleFBT(j):
                        tree = TreeNode(0)
                        tree.left = left
                        tree.right = right

                        result.append(tree)
            self.cache[n] = result
        
        return self.cache[n]
