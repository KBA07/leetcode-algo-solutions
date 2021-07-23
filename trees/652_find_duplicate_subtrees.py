"""
652. Find Duplicate Subtrees
Medium

2276

255

Add to List

Share
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

 

Example 1:


Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]
Example 2:


Input: root = [2,1,1]
Output: [[1]]
Example 3:


Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]
 

Constraints:

The number of the nodes in the tree will be in the range [1, 10^4]
-200 <= Node.val <= 200
Accepted
105,131
Submissions
194,799
"""

"""
Runtime: 64 ms, faster than 64.92% of Python3 online submissions for Find Duplicate Subtrees.
Memory Usage: 23.5 MB, less than 44.86% of Python3 online submissions for Find Duplicate Subtrees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        trees = {}
        
        def dfs(root, trees):
            if not root: return '!'
            
            tree = f"{str(root.val)},{dfs(root.left, trees)},{dfs(root.right, trees)}"

            trees[tree].append(root)
            return tree
        
        trees = collections.defaultdict(list)
        dfs(root, trees)
        
        return [trees[tree][0] for tree in trees if len(trees[tree]) > 1]
