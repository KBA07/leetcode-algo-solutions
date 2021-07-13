"""
Share
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
Accepted
1,511,526
Submissions
2,643,481
"""

"""
Runtime: 52 ms, faster than 13.85% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14.2 MB, less than 84.47% of Python3 online submissions for Merge Two Sorted Lists.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        point = head = ListNode()
        while l1 and l2:
            if l2.val < l1.val:
                point.next = l2
                l2 = l2.next
            else:
                point.next = l1
                l1 = l1.next
        
            point = point.next
        
        if l1:
            point.next = l1
        elif l2:
            point.next = l2
        else:
            point.next = None
        
        return head.next
        