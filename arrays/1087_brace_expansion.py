"""
1087. Brace Expansion
Medium

376

35

Add to List

Share
You are given a string s representing a list of words. Each letter in the word has one or more options.

If there is one option, the letter is represented as is.
If there is more than one option, then curly braces delimit the options. For example, "{a,b,c}" represents options ["a", "b", "c"].
For example, if s = "a{b,c}", the first character is always 'a', but the second character can be 'b' or 'c'. The original list is ["ab", "ac"].

Return all words that can be formed in this manner, sorted in lexicographical order.

 

Example 1:

Input: s = "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]
Example 2:

Input: s = "abcd"
Output: ["abcd"]
 

Constraints:

1 <= s.length <= 50
s consists of curly brackets '{}', commas ',', and lowercase English letters.
s is guaranteed to be a valid input.
There are no nested curly brackets.
All characters inside a pair of consecutive opening and ending curly brackets are different.
Accepted
30,479
Submissions
47,948
"""

"""
Runtime: 36 ms, faster than 83.31% of Python3 online submissions for Brace Expansion.
Memory Usage: 14.9 MB, less than 16.84% of Python3 online submissions for Brace Expansion.
"""

class Solution:
    def expand(self, s: str) -> List[str]:
        result = []
#         multiplier = []
        
#         char = ''
#         i = 0
#         while i < len(s):
    
#             if s[i] == '{':
#                 if char:
#                     multiplier.append(char)
#                     char = ''
                
#                 while s[i] != '}':
#                     if s[i] not in ['{', ',']:
#                         result.append(s[i])
#                     i += 1
            
#                 if result and multiplier:
#                     for multi in multiplier:
#                         result = [res + multi for res in result]
                    
#                     multiplier = []
                
#                 print(multiplier, result)
                    
#             else:
#                 char += s[i]
            
#             i += 1

        def dfs(curr_word, index):
            if index == len(s):
                result.append(curr_word)
            else:
                if s[index] == '{':
                    j = index
                    while s[j] != '}':
                        j += 1
                    
                    for char in s[index + 1: j].split(','):
                        dfs(curr_word + char, j + 1)
                
                else:
                    dfs(curr_word + s[index], index + 1)
        
        dfs("", 0)
        result.sort()
        return result
            
        # print(result, multiplier)