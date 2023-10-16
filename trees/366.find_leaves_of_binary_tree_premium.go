"""
366. Find Leaves of Binary Tree
Medium
3.1K
53
company
Google
company
LinkedIn
company
Amazon
Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.
 

Example 1:


Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
Example 2:

Input: root = [1]
Output: [[1]]
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
Accepted
244.6K
Submissions
304.3K
Acceptance Rate
80.4%
"""

"""
Runtime: 1ms Beats 70.59%of users with Go
Memory Usage: 2.09MB Beats 61.76%of users with Go
"""

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 var result [][] int

 func max(a, b int)int{
	 return int(math.Max(float64(a), float64(b)))
 }
 
 
 func helper(node *TreeNode) int {
	 if node == nil {
		 return -1
	 }
 
	 left := helper(node.Left)
	 right := helper(node.Right)
 
	 height := 1 + max(left, right)
 
	 if height == len(result) {
		 result = append(result, []int{})
	 }
 
	 result[height] = append(result[height], node.Val)
	 return height
 }
 
 func findLeaves(root *TreeNode) [][]int {
	 result = [][]int{}
	 helper(root)
	 return result    
 }