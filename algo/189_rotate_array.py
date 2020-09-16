"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?


Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 2 * 10^4
It's guaranteed that nums[i] fits in a 32 bit-signed integer.
k >= 0
"""

"""
Runtime: 52 ms, faster than 66.94% of Python online submissions for Rotate Array.
Memory Usage: 13 MB, less than 69.81% of Python online submissions for Rotate Array.
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        k = k % nums_len
        rotate_start = nums_len - k

        rotate_list = []
        for index in range(rotate_start, nums_len):
            rotate_list.append(nums[index])

        last = nums_len - 1
        for index in range(rotate_start - 1, -1, -1):
            nums[last] = nums[index]
            last -= 1

        for index in range(len(rotate_list) -1, -1, -1):
            nums[last] = rotate_list[index]
            last -= 1


"""
Runtime: 60 ms, faster than 48.10% of Python online submissions for Rotate Array.
Memory Usage: 13.1 MB, less than 52.64% of Python online submissions for Rotate Array.
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverse(left, right):
            while left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        nums_len = len(nums)
        k = k % nums_len
        reverse(0, nums_len - 1)
        reverse(0, k-1)
        reverse(k, nums_len - 1)