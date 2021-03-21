"""
Easy
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

Accepted
779,178
Submissions
1,327,089
"""
"""
Runtime: 48 ms, faster than 63.58% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.4 MB, less than 91.79% of Python3 online submissions for Valid Anagram.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_dict = {}
        for char in s:
            try:
                char_dict[char] += 1
            except KeyError:
                char_dict[char] = 1
        
        for char in t:
            if char not in char_dict:
                return False
            
            char_dict[char] -= 1
            if char_dict[char] == 0:
                char_dict.pop(char)
        
        return True

