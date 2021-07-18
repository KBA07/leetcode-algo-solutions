"""
Share
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
Accepted
508,681
Submissions
1,149,259
"""

"""
Runtime: 28 ms, faster than 88.13% of Python online submissions for Find Peak Element.
Memory Usage: 13.5 MB, less than 69.90% of Python online submissions for Find Peak Element.
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(nums) - 1
        
        while(left < right):
            
            mid = left + (right - left)/2
            
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        
        return left

"""
Runtime: 36 ms, faster than 98.58% of Python3 online submissions for Find Peak Element.
Memory Usage: 14.3 MB, less than 72.43% of Python3 online submissions for Find Peak Element.
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        def helper(array, start, end):
            if start == end:
                return start
            
            mid = (start + end) // 2
            
            if array[mid] < array[mid + 1]:
                return helper(array, mid + 1, end)
            
            return helper(array, start, mid)
        
        return helper(nums, 0, len(nums) - 1)
        