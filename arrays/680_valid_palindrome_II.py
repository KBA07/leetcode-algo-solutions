"""
680. Valid Palindrome II
Easy

2861

182

Add to List

Share
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
Accepted
287,874
Submissions
769,807
"""

"""
Runtime: 236 ms, faster than 17.55% of Python3 online submissions for Valid Palindrome II.
Memory Usage: 14.7 MB, less than 40.35% of Python3 online submissions for Valid Palindrome II.
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        start = 0
        end = len(s) - 1
        
        lifeline = True
        while start < end:
            if s[start] != s[end]:
                return isPalindrome(s, start + 1, end) or isPalindrome(s, start, end - 1)
            
            start += 1
            end -= 1
        
        return True
