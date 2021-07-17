"""
767. Reorganize String
Medium

3224

151

Add to List

Share
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
Accepted
153,957
Submissions
303,424
"""

"""
Runtime: 40 ms, faster than 31.37% of Python3 online submissions for Reorganize String.
Memory Usage: 14.2 MB, less than 84.03% of Python3 online submissions for Reorganize String.
"""

class Solution:
    def reorganizeString(self, s: str) -> str:
        def nextKey(lastchar, char_map, max_char_list):
            for key in max_char_list:
                if key != lastchar and key in char_map:
                    return key
                
            return lastchar
        
        char_map = {}
        for char in s:
            try:
                char_map[char] += 1
            except KeyError:
                char_map[char] = 1
                
        max_char_list = sorted(char_map, key=char_map.get, reverse=True)
        res_string = ''
        last_char = ''
        while char_map:
            char = nextKey(last_char, char_map, max_char_list)
            
            if char == last_char:
                return ''
            
            res_string += char
            last_char = char
            
            
            char_map[char] -= 1
            if char_map[char] == 0:
                char_map.pop(char)
            max_char_list = sorted(char_map, key=char_map.get, reverse=True)

            
        return res_string
