"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

"""
Runtime: 20 ms, faster than 97% of Python online submissions for Reverse Linked List.
Memory Usage: 14.8 MB, less than 50% of Python online submissions for Reverse Linked List.
"""

class Solution(object):
    def reverseList(self, head):
        previous = None
        current = head

        while current:
            head = current.next
            current.next = previous
            previous = current
            current = head

        return previous

"""
Runtime: 16 ms, faster than 98.58% of Python online submissions for Reverse Linked List.
Memory Usage: 19.5 MB, less than 5.05% of Python online submissions for Reverse Linked List.
"""
class Solution(object):

    def reverseList(self, head):

        def helper(right, current):

            if not right:
                return current

            temp = right.next
            right.next = current


            return helper(temp, right)

        return helper(head, None)
