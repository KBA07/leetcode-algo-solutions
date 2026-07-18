package main

type ListNode struct {
	Val  int
	Next *ListNode
}

/*
Runtime: 0ms Beats 100% of users with GoLang
Memory Usage: 4.35 MB Beats 83.03% of users with GoLang
*/
func reverseList(head *ListNode) *ListNode {
	var current *ListNode
	next := head

	for next != nil {
		tmp := next.Next
		next.Next = current

		current = next
		next = tmp
	}

	return current
}
