"""
Easy

2473

3312

Add to List

Share
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Example 3:

Input: digits = [0]
Output: [1]
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
Accepted
863,252
Submissions
2,048,186
"""

"""
Runtime: 28 ms, faster than 88.93% of Python3 online submissions for Plus One.
Memory Usage: 14.3 MB, less than 44.36% of Python3 online submissions for Plus One.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for index in range(len(digits) - 1, -1, -1):
            
            if digits[index] == 9:
                digits[index] = 0
            else:
                digits[index] += 1
                break
                
        
        if digits[0] == 0:
            digits = [1] + digits
        return digits
        