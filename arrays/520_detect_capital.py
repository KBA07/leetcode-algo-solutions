"""
Easy

875

299

Add to List

Share
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

 

Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false
 

Constraints:

1 <= word.length <= 100
word consists of lowercase and uppercase English letters.
Accepted
197,524
Submissions
364,596
"""

"""
Runtime: 36 ms, faster than 18.90% of Python3 online submissions for Detect Capital.
Memory Usage: 14.4 MB, less than 13.89% of Python3 online submissions for Detect Capital.
"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        first_capital = word[0].isupper()
        
        for index in range(1, len(word)):
            if first_capital:
                small_dectected = False
                while index < len(word):
                    if word[index].islower():
                        if word[index - 1].isupper() and (index - 1) > 0:
                            return False
                        small_dectected = True
                    
                    print(word[index])
                    if first_capital and small_dectected and word[index].isupper():
                        return False
                    
                    index += 1
                        
            else:
                if word[index].isupper(): return False
                
        return True

"""
Runtime: 32 ms, faster than 60.06% of Python3 online submissions for Detect Capital.
Memory Usage: 14 MB, less than 90.98% of Python3 online submissions for Detect Capital.
"""
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital_count = 0
        
        for char in word:
            if char.isupper():
                capital_count += 1
        
        if capital_count == len(word) or not capital_count or (capital_count == 1 and word[0].isupper()):
            return True
        
        return False