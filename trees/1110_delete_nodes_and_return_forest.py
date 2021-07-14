"""
1110. Delete Nodes And Return Forest
Medium

2001

59

Add to List

Share
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

 

Example 1:


Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
Example 2:

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]
 

Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
Accepted
111,182
Submissions
162,896
"""

"""
Runtime: 60 ms, faster than 95.32% of Python3 online submissions for Delete Nodes And Return Forest.
Memory Usage: 15 MB, less than 23.25% of Python3 online submissions for Delete Nodes And Return Forest.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        answer = []
        to_delete = set(to_delete)
        def helper(answer, root, to_delete):
            if not root:
                return
            
            root.left = helper(answer, root.left, to_delete)
            root.right = helper(answer, root.right, to_delete)
            
            if root.val in to_delete:
                if root.left:
                    answer.append(root.left)
                
                if root.right:
                    answer.append(root.right)
                
                return 
            
            return root
        
        helper(answer, root, to_delete)
        if root.val not in to_delete:
            answer.append(root)
        return answer
