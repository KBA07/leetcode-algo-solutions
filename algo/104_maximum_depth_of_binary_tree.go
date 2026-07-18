package main

/*
Runtime: 0ms Beats 100% of users with GoLang
Memory Usage: 8.89 MB Beats 6.11% of users with GoLang
*/
func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}

	return 1 + max(maxDepth(root.Left), maxDepth(root.Right))
}

func maxDepthUsingQueue(root *TreeNode) int {
	if root == nil {
		return 0
	}

	queue := []*TreeNode{root}
	depth := 0

	for len(queue) != 0 {

		size := len(queue)

		for size > 0 {
			node := queue[0]
			queue = queue[1:]

			if node.Left != nil {
				queue = append(queue, node.Left)
			}

			if node.Right != nil {
				queue = append(queue, node.Right)
			}
			size--

		}

		depth++

	}

	return depth

}
