"""
Easy
Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
Accepted
711,383
Submissions
1,320,714
"""

"""
Runtime: 116 ms, faster than 79.91% of Python online submissions for First Unique Character in a String.
Memory Usage: 13.6 MB, less than 88.32% of Python online submissions for First Unique Character in a String.
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_dict = {}
        for char in s:
            try:
                char_dict[char] += 1
            except KeyError:
                char_dict[char] = 1
                
        for index, char in enumerate(s):
            if char_dict.get(char) == 1:
                return index
            
        return -1
        