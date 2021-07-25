"""
15. 3Sum
Medium

11956

1170

Add to List

Share
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
Accepted
1,397,464
Submissions
4,824,727
"""

"""
Runtime: 652 ms, faster than 95.76% of Python3 online submissions for 3Sum.
Memory Usage: 17.4 MB, less than 73.76% of Python3 online submissions for 3Sum.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        if not nums:
            return nums
        
        nums.sort()
        
        def twoSum(low, high, num):
            while low < high:
                cur_sum = num + nums[low] + nums[high]
                if cur_sum < 0:
                    low += 1
                elif cur_sum > 0:
                    high -= 1
                else:
                    # sum == 0
                    result.append([num, nums[low], nums[high]])
                    low += 1
                    high -= 1

                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
        
        high = len(nums) - 1
        for index, num in enumerate(nums):
            
            if num > 0:
                # This means that we have reached a positive side, and can't get 0
                break
            
            if index == 0 or nums[index - 1] != nums[index]:
                twoSum(index + 1, high, num)
            
        return result
       