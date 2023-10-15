"""
2265. Count Nodes Equal to Average of Subtree
Medium
1.3K
24
company
Google
company
Amazon
company
Facebook
Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

Note:

The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
A subtree of root is a tree consisting of root and all of its descendants.
 

Example 1:


Input: root = [4,8,5,0,1,null,6]
Output: 5
Explanation: 
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
For the node with value 0: The average of its subtree is 0 / 1 = 0.
For the node with value 1: The average of its subtree is 1 / 1 = 1.
For the node with value 6: The average of its subtree is 6 / 1 = 6.
Example 2:


Input: root = [1]
Output: 1
Explanation: For the node with value 1: The average of its subtree is 1 / 1 = 1.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000
Accepted
47.1K
Submissions
55.5K
Acceptance Rate
84.8%
"""

"""
Runtime: 3ms Beats 93.48%of users with Go
Memory Usage: 4.68MB Beats 8.70%of users with Go
"""

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 var result int

 func helper(root *TreeNode)(int, int) {
	 if root == nil {
		 return 0, 0
	 }
 
	 leftNode, SumLeft := helper(root.Left)
	 rightNode, SumRight := helper(root.Right)
 
	 
	 average := (SumLeft + SumRight + root.Val) / (leftNode + rightNode + 1)
 
	 fmt.Println(root.Val, average)
 
	 if root.Val == average {
		 result += 1
	 }
	 return leftNode + rightNode + 1, SumLeft + SumRight + root.Val
 }
 
 func averageOfSubtree(root *TreeNode) int {
	 result = 0
	 helper(root)
 
	 return result
 }