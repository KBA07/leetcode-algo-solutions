"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
"""
Runtime: 24 ms, faster than 91.48% of Python online submissions for Permutations.
Memory Usage: 12.7 MB, less than 72.69% of Python online submissions for Permutations.
"""


class Solution(object):
    def permute(self, nums):

        def helper(remNumber, formedNumber, answer):

            if not remNumber:
                answer.append(formedNumber)
                return

            for index in xrange(0, len(remNumber)):
                # Beware of python object reference because at each recursive call we have to pass a new list
                helper(remNumber[:index] + remNumber[index+1:], formedNumber + [remNumber[index]], answer)

        answer = []
        helper(nums, [],  answer)
        return answer
