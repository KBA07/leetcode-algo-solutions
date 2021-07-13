"""
Share
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
Accepted
1,097,955
Submissions
2,966,719
"""

"""
Runtime: 44 ms, faster than 21.30% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14.4 MB, less than 54.97% of Python3 online submissions for Longest Common Prefix.
Next challenges:
"""

class Solution:
    def longestCommonPrefix(self, strs):
        prefix = ''
        start = 0
        end = len(strs[0])
        
        while start < end:
            for word in strs[1:]:
                if start >= len(word) or strs[0][start] != word[start]:
                    return prefix
            
            prefix += strs[0][start]
            start += 1
        
        return prefix
                