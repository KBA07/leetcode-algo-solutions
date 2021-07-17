"""
231. Power of Two
Easy

1543

228

Add to List

Share
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
Example 4:

Input: n = 4
Output: true
Example 5:

Input: n = 5
Output: false
 

Constraints:

-231 <= n <= 231 - 1
 

Follow up: Could you solve it without loops/recursion?
Accepted
435,744
Submissions
994,326
"""

"""
Runtime: 28 ms, faster than 89.72% of Python3 online submissions for Power of Two.
Memory Usage: 14.2 MB, less than 40.06% of Python3 online submissions for Power of Two.
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n <= 0:
            return False
        
        while n > 1:
            if n % 2 != 0:
                return False
            
            n = n / 2
        
        return True
