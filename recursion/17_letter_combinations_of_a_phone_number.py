"""
Medium

6407

540

Add to List

Share
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""

"""
Runtime: 24 ms, faster than 96.05% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 14.2 MB, less than 60.56% of Python3 online submissions for Letter Combinations of a Phone Number.
"""

class Solution:
    result = []
    mappings = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    def letterCombinations(self, digits: str) -> List[str]:
        self.result = []
        if digits:
            self.addCombinations("", digits, 0)
        return self.result
    
    def addCombinations(self, curr_string, digits, digit_index):
        if len(curr_string) == len(digits):
            self.result.append(curr_string)
            return
        
        letters = self.mappings[ord(digits[digit_index]) - ord('0')]
        
        for letter in letters:
            self.addCombinations(curr_string + letter, digits, digit_index + 1)
