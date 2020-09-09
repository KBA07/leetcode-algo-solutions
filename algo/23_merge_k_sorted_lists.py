"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
Accepted
696,693
Submissions
1,714,784
"""

"""
Runtime: 4472 ms, faster than 5.04% of Python online submissions for Merge k Sorted Lists.
Memory Usage: 18.7 MB, less than 95.81% of Python online submissions for Merge k Sorted Lists.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        if not lists:
            return

        def mergeList(fp, sp):
            current_pointer = ListNode(-1)
            head = current_pointer

            while fp and sp:

                if sp.val < fp.val:
                    current_pointer.next = sp
                    sp = sp.next

                else:
                    current_pointer.next = fp
                    fp = fp.next
                current_pointer = current_pointer.next

            if fp:
                current_pointer.next = fp
            else:
                current_pointer.next = sp

            return head.next

        first = lists[0]
        for index in range(1, len(lists)):
            first = mergeList(first, lists[index])

        return first
