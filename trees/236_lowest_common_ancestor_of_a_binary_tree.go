"""
236. Lowest Common Ancestor of a Binary Tree
Medium
15.3K
353
company
Facebook
company
Bloomberg
company
Amazon
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
Accepted
1.4M
Submissions
2.3M
Acceptance Rate
60.4%
"""

// Wrong Answer 12 / 31 testcases passed

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 var result *TreeNode

 func helper(node, p, q *TreeNode) int {
    if node == nil {
        return 0
    }
    left := helper(node.Left, p, q)
    right := helper(node.Right, p, q)

    mid := (p == node) || (q == node)
    midInt := 0 
    if mid {
        midInt = 1
    }

    if (midInt + left + right) > 1 {
        result = node
    }
    return midInt
 }
 func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
    helper(root, p, q)
    return result
}

"""
Runtime: 6ms Beats 93.59%of users with Go
Memory Usage: 7.15MB Beats 72.34%of users with Go
"""

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
    if root == nil {
        return nil
    }

    if (root == p) || (root == q) {
        return root
    }

    left := lowestCommonAncestor(root.Left, p, q)
    right := lowestCommonAncestor(root.Right, p, q)

    if left != nil && right != nil {
        return root
    }

    if left != nil {
        return left
    }
    return right
}

