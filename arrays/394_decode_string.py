"""
394. Decode String
Medium

5501

252

Add to List

Share
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
Accepted
352,207
Submissions
654,435
"""

"""
Runtime: 20 ms, faster than 99.17% of Python3 online submissions for Decode String.
Memory Usage: 14.4 MB, less than 20.34% of Python3 online submissions for Decode String.
"""

class Solution:
    def decodeString(self, s: str) -> str:
        
        def get_times_and_index(s, start_index):
            digit_start_index = start_index - 1
            while s[digit_start_index].isdigit():
                digit_start_index -= 1
            
            return digit_start_index + 1, int(''.join(s[digit_start_index + 1: start_index]))
            
            
        stack = []
        
        s = list(s)
        str_len = len(s)
        index = 0
        
        while index < str_len:
            if s[index] == '[':
                stack.append(index)
            
            if s[index] == ']':
                start_index = stack.pop()
                
                replace_start, times = get_times_and_index(s, start_index)
                word = s[start_index + 1: index] if index > start_index + 1 else ''
                s = s[:replace_start] + (times * word) + s[index+1:]
                str_len = len(s)
                index = replace_start + (times * len(word)) - 1
            
            index += 1
        
        return ''.join(s)


"""
Runtime: 28 ms, faster than 81.80% of Python3 online submissions for Decode String.
Memory Usage: 14.2 MB, less than 52.56% of Python3 online submissions for Decode String.
"""
class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        currentWord = ''
        k = 0
        for char in s:
            
            if char == '[':
                stack.append([k, currentWord])
                k = 0
                currentWord = ''     
            elif char == ']':
                k, lastWord = stack.pop()
                currentWord = lastWord + (k * currentWord)
                k = 0
            elif char.isdigit():
                k = k * 10 + int(char)
            else:
                currentWord += char
        
        return currentWord

"""
Didn't work
"""

class Solution:
    def decodeString(self, s: str) -> str:
        
        def helper(s, index):
            result = ''
            while index < len(s) and s[index] != ']':
                if not s[index].isdigit():
                    result += s[index]
                else:
                    k = 0
                    
                    while index < len(s) and s[index].isdigit():
                        k = k * 10 + int(s[index])
                        index += 1
                        
                    index += 1 # skip [
                    decodedString = helper(s, index)
                    index += 1 # skip ]
                    
                    while k > 0:
                        result += decodedString
                        k -= 1
                        
                index += 1
            
            return result
                
        return helper(s, 0)

