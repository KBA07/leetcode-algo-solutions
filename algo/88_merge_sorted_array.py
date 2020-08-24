"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]


Constraints:

-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n
"""

"""
Runtime: 24 ms, faster than 81.23% of Python online submissions for Merge Sorted Array.
Memory Usage: 12.7 MB, less than 46.62% of Python online submissions for Merge Sorted Array.
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        dummyPointer = m + n - 1
        firstPointer = m - 1
        secondPointer = n - 1

        while firstPointer >= 0 and secondPointer >=0:

            if nums1[firstPointer] >= nums2[secondPointer]:
                nums1[dummyPointer] = nums1[firstPointer]
                firstPointer -= 1
            else:
                nums1[dummyPointer] = nums2[secondPointer]
                secondPointer -= 1
            dummyPointer -= 1

        if not secondPointer < 0:
            for index in range(secondPointer, -1, -1):
                nums1[dummyPointer] = nums2[index]
                dummyPointer -= 1

        return nums1
