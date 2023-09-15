"""
2396. Strictly Palindromic Number
Medium
483
1.3K
Companies
An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive), the string representation of the integer n in base b is palindromic.

Given an integer n, return true if n is strictly palindromic and false otherwise.

A string is palindromic if it reads the same forward and backward.

 

Example 1:

Input: n = 9
Output: false
Explanation: In base 2: 9 = 1001 (base 2), which is palindromic.
In base 3: 9 = 100 (base 3), which is not palindromic.
Therefore, 9 is not strictly palindromic so we return false.
Note that in bases 4, 5, 6, and 7, n = 9 is also not palindromic.
Example 2:

Input: n = 4
Output: false
Explanation: We only consider base 2: 4 = 100 (base 2), which is not palindromic.
Therefore, we return false.

 

Constraints:

4 <= n <= 105
Accepted
63.3K
Submissions
72.5K
Acceptance Rate
87.4%
"""

"""
Runtime: 37ms Beats 69.55% of users with Python3
Memory Usage: 16.22MB Beats 61.80% of users with Python3
"""

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:

        def basePalindrome(n, b):
            ans = ''

            while n:
                remainder = n % b
                ans += str(remainder)
                n = n // b
            
            return ans[::-1] == ans

        for b in range(2, n-1):
            if not basePalindrome(n, b):
                return False

        return True 
