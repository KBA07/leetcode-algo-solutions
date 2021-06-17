"""
Easy

4927

7484

Add to List

Share
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-231 <= x <= 231 - 1
Accepted
1,574,973
Submissions
6,046,894
"""

"""
Runtime: 24 ms
Memory Usage: 12.9 MB
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNegative = False
        
        if x < 0:
            isNegative = True
            x = 0 - x
        
        revNumber = 0
        while x:
            revNumber = revNumber*10 + x%10
            x = x//10
            
        pow231 = 2 ** 31
        if isNegative:
            if revNumber > pow231:
                return 0
            revNumber = 0 - revNumber
        else:
            if revNumber > pow231 - 1:
                return 0
            
            
        return revNumber
