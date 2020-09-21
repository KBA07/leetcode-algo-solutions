"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
"""
Runtime: 20 ms, faster than 80.43% of Python online submissions for Subsets.
Memory Usage: 12.8 MB, less than 56.66% of Python online submissions for Subsets.
"""

class Solution(object):
    def subsets(self, nums):
        global recDepth
        recDepth = len(nums)

        answer = []

        def helper(array, iteration, answer):
            global recDepth

            if iteration == recDepth:
                answer.append(array)
                return

            number = nums[iteration]
            ind = array.index(number)

            helper(array[:ind] + array[ind+1:] , iteration+1, answer)
            helper(array[:], iteration+1, answer)

        helper(nums[:], 0, answer)
        return answer
