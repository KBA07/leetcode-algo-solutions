"""
58. Length of Last Word
Easy
3.7K
190
Companies
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
Accepted
1.3M
Submissions
2.8M
Acceptance Rate
45.1%
"""

"""
Runtime: Beats 49.15% of users with Python3
Memory Usage: Beats 57.95% of users with Python3
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_len = 0
        word_len = 0

        for char in s:
            if char == ' ':
                last_len = word_len if word_len else last_len
                word_len = 0
                
            else:
                word_len += 1

        return word_len if word_len else last_len


"""
Runtime: 46ms, Beats 49.15%of users with Python3
Memory Usage: 16.39mb, Beats 57.95%of users with Python3
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_len = 0

        for index in range(len(s) - 1, -1, -1):
            if s[index] == ' ' and word_len:
                break
            
            if s[index] == ' ':
                continue
            
            word_len += 1

        return word_len