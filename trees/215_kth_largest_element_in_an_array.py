"""
Medium

6008

374

Add to List

Share
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104
Accepted
935,761
Submissions
1,565,343
"""

"""
Runtime: 64 ms, faster than 73.49% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 15.1 MB, less than 73.93% of Python3 online submissions for Kth Largest Element in an Array.
"""

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        
        return heapq.nlargest(k, nums)[-1]
