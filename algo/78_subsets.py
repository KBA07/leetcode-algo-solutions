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

"""
Runtime: 84 ms, faster than 6.33% of Python3 online submissions for Subsets.
Memory Usage: 14.5 MB, less than 49.90% of Python3 online submissions for Subsets.
"""
class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        # answer.append(nums)
        
        def helper(subsets, answer, index, nums):
            subsets.append(answer[:])

            for i in range(index, len(nums)):
                answer.append(nums[i])
                helper(subsets, answer, i + 1, nums)
                answer.pop()
        
        helper(subsets, [], 0, nums)
        return subsets


"""
Runtime: 60 ms, faster than 6.33% of Python3 online submissions for Subsets.
Memory Usage: 14.6 MB, less than 18.43% of Python3 online submissions for Subsets.
"""
class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        # answer.append(nums)
        
        for num in nums:
            subsets += [subset + [num] for subset in subsets]
        
        return subsets