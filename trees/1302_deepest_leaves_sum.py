"""
1302. Deepest Leaves Sum
Medium

2057

67

Add to List

Share
Given the root of a binary tree, return the sum of values of its deepest leaves.
 

Example 1:


Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100
Accepted
148,633
Submissions
173,776
"""

"""
Runtime: 264 ms, faster than 24.37% of Python3 online submissions for Deepest Leaves Sum.
Memory Usage: 17.8 MB, less than 41.97% of Python3 online submissions for Deepest Leaves Sum.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        def getDepth(root):
            if not root:
                return 0
            
            left_depth = getDepth(root.left)
            right_depth = getDepth(root.right)
            
            return (1 + max(left_depth, right_depth))
        
        def getDeepestLeavesSum(root, current_depth, max_depth):
            if not root:
                return 0
            
            if current_depth == max_depth:
                return root.val
            
            return getDeepestLeavesSum(root.left, current_depth + 1, max_depth) + getDeepestLeavesSum(root.right, current_depth + 1, max_depth)
        
        max_depth = getDepth(root)
        return getDeepestLeavesSum(root, 1, max_depth)
        