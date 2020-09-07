"""
2. Add Two Numbers
Medium

9106

2291

Add to List

Share
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
"""
Success
Details 
Runtime: 60 ms, faster than 81.86% of Python online submissions for Add Two Numbers.
Memory Usage: 12.7 MB, less than 54.09% of Python online submissions for Add Two Numbers.
Next challenges:
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    @staticmethod
    def add(val1, val2, val3):
        summed = val1 + val2 + val3
        return summed // 10, summed % 10

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        result_list = None
        pointer = None
        while l1 or l2:
            if not l1:
                l1.value = 0
            if not l2:
                l2.value = 0

            carry, value = Solution.add(l1.value, l2.value, carry)

            node = ListNode(value, None)
            if not pointer:
                result_list = node
                pointer = result_list
            else:
                pointer.next = node
                pointer = pointer.next

            l1 = l1.next
            l2 = l2.next

        return result_list
