"""
482. License Key Formatting
Easy

626

914

Add to List

Share
You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.

 

Example 1:

Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
Example 2:

Input: s = "2-5g-3-J", k = 2
Output: "2-5G-3J"
Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
 

Constraints:

1 <= s.length <= 105
s consists of English letters, digits, and dashes '-'.
1 <= k <= 104
Accepted
172,895
Submissions
400,613
"""

"""
Runtime: 92 ms, faster than 28.02% of Python3 online submissions for License Key Formatting.
Memory Usage: 14.9 MB, less than 55.64% of Python3 online submissions for License Key Formatting.
"""

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        rev_result = ''
        
        counter = k
        for index in range(len(s) - 1, -1, -1):
            
            if s[index] == '-':
                continue
            
            if counter < 1:
                counter = k
                rev_result += '-'
            
            rev_result += s[index].upper()
            counter -= 1
        
        return rev_result[::-1]

"""
Runtime: 64 ms, faster than 46.85% of Python3 online submissions for License Key Formatting.
Memory Usage: 14.9 MB, less than 41.86% of Python3 online submissions for License Key Formatting.
"""    
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        rev_result = ''
        
        counter = 0
        for index in range(len(s) - 1, -1, -1):
            
            if s[index] == '-':
                continue
            
            if counter > k-1:
                counter = 0
                rev_result += '-'
            
            rev_result += s[index].upper()
            counter += 1
        
        return rev_result[::-1]
            