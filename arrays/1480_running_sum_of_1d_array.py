"""
Easy
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
 

Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
Accepted
271,142
Submissions
305,199
"""

"""
Runtime: 36 ms, faster than 87.46% of Python3 online submissions for Running Sum of 1d Array.
Memory Usage: 14.4 MB, less than 74.14% of Python3 online submissions for Running Sum of 1d Array.
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        
        lastSum = 0
        
        for currentIndex, currentSum in enumerate(nums):
            currentSum = lastSum + currentSum
            lastSum = currentSum
            nums[currentIndex] = currentSum
        
        return nums
