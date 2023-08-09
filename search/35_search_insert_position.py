"""
35. Search Insert Position
Easy
14.2K
614
Companies
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
Accepted
2.3M
Submissions
5.3M
Acceptance Rate
44.1%
"""

"""
Runtime: Beats 94.07% of users with Python3
Memory Usage: Beats 87.46% of users with Python3
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)

        while (low < high):

            mid = (low + high) // 2

            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid

        return low