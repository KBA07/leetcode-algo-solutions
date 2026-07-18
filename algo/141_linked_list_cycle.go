package main

/*
Runtime: 3ms Beats 93.82% of users with GoLang
Memory Usage: 6.18 MB Beats 80.47% of users with GoLang
*/
func hasCycle(head *ListNode) bool {
	for head == nil || head.Next == nil {
		return false
	}

	slow := head
	fast := head

	for fast != nil && fast.Next != nil {

		slow = slow.Next
		fast = fast.Next.Next

		if slow == fast {
			return true
		}
	}

	return false
}
