package main

/*
Runtime: 0ms Beats 100% of users with GoLang
Memory Usage: 4.14 MB Beats 35.39% of users with GoLang
*/
func invertTree(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}

	left := invertTree(root.Left)
	right := invertTree(root.Right)

	root.Left = right
	root.Right = left

	return root
}
