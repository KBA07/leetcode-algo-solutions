"""
125. Valid Palindrome
Easy

2240

4081

Add to List

Share
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
Accepted
917,830
Submissions
2,339,503
"""

"""
Error
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_offset = 96 # char lies between 97 - 97 + 25
        num_offset = 47 # num lies between 48 - 48 + 9
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            # check if left is alphanumeric
            
            if not (num_offset < ord(s[left].lower()) < num_offset + 11 or char_offset < ord(s[left].lower()) < char_offset + 27):
                # not alpha numeric
                left += 1
                continue
            
            if not (num_offset < ord(s[right].lower()) < num_offset + 11 or char_offset < ord(s[left].lower()) < char_offset + 27):
                # not alpha numeric
                right -= 1
                continue
                
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
            
        return True

"""
Runtime: 52 ms, faster than 48.56% of Python3 online submissions for Valid Palindrome.
Memory Usage: 14.3 MB, less than 99.04% of Python3 online submissions for Valid Palindrome.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1
        # print("right is", right)
        
        while left < right:
            
            while left < right and not s[left].isalnum():
                left += 1
            
            while left < right and not s[right].isalnum():
                right -= 1
                
            
            if left < right and s[right].lower() != s[left].lower():
                return False
            
            left += 1
            right -= 1
            
        return True