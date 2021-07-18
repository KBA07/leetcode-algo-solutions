"""
Share
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99
 

Constraints:

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.
Accepted
298,228
Submissions
544,382
"""

"""
Runtime: 52 ms, faster than 92.30% of Python3 online submissions for Single Number II.
Memory Usage: 16.2 MB, less than 30.41% of Python3 online submissions for Single Number II.
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_map = {}
        
        for num in nums:
            if num in nums_map and nums_map[num] == 2:
                nums_map.pop(num)
            else:
                try:
                    nums_map[num] += 1
                except KeyError:
                    nums_map[num] = 1
            
        for key in nums_map:
            return key

"""
Runtime: 56 ms, faster than 80.14% of Python3 online submissions for Single Number II.
Memory Usage: 15.8 MB, less than 82.12% of Python3 online submissions for Single Number II.
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        # print(nums)
        for index in range(0, len(nums), 3):
            # print(index)
            first = nums[index]
            second = nums[index + 1] if index + 1 < len(nums) else 0
            third = nums[index + 2] if index + 2 < len(nums) else 0
    
            if not first == second == third:
                # print(first, second, third)
                return first ^ second ^ third


"""
Won't work for negative
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        result = 0
        for index in range(32): # 32 bits
            sum_bits = 0
            
            for inner_index in range(len(nums)):
                sum_bits += nums[inner_index] % 2
                nums[inner_index] = nums[inner_index] // 2
                
            
            result = result | sum_bits % 3 << index
        
        return result