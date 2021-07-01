"""
Share
Given a string s, sort it in decreasing order based on the frequency of characters, and return the sorted string.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
 

Constraints:

1 <= s.length <= 5 * 105
s consists of English letters and digits.
Accepted
265,523
Submissions
407,501
"""

"""
Runtime: 64 ms, faster than 28.68% of Python3 online submissions for Sort Characters By Frequency.
Memory Usage: 15.2 MB, less than 91.17% of Python3 online submissions for Sort Characters By Frequency.
"""

class Solution:
    def frequencySort(self, s: str) -> str:
        
        char_dict = {}
        max_len = 0
        for char in s:
            try:
                char_dict[char] += 1
            except KeyError:
                char_dict[char] = 1
            
            if char_dict[char] > max_len:
                max_len = char_dict[char]
        
        rev_map = [''] * max_len
        
        for char in char_dict:
            val = char_dict[char]
            
            try:
                rev_map[val - 1].append(char)
            except AttributeError:
                rev_map[val - 1] = [char]
        
        ret_string = ''
        for index in range(max_len - 1, -1, -1):
            for char in rev_map[index]:
                ret_string += char * (index + 1)
        
        return ret_string
