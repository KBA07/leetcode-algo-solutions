"""
167. Two Sum II - Input array is sorted
Easy

3030

759

Add to List

Share
Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
Accepted
614,312
Submissions
1,089,839
"""

"""
Runtime: 92 ms, faster than 20.16% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 14.6 MB, less than 62.42% of Python3 online submissions for Two Sum II - Input array is sorted.
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def findNumber(low, high, number):
            while low < high:
                mid = (low + high) // 2
                if number > numbers[mid]:
                    low = mid + 1
                else:
                    high = mid
            return low
            
            
        for index, num in enumerate(numbers):
            required = target - numbers[index]
            
            idx = findNumber(index + 1, len(numbers) - 1, required)
            if idx < len(numbers) and numbers[idx] == required:
                return[index+1, idx+1]      
