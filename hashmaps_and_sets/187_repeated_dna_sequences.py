"""
187. Repeated DNA Sequences
Medium

1307

343

Add to List

Share
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 

Constraints:

1 <= s.length <= 105
s[i] is either 'A', 'C', 'G', or 'T'.
Accepted
216,203
Submissions
512,249
"""

"""
Runtime: 72 ms, faster than 52.09% of Python3 online submissions for Repeated DNA Sequences.
Memory Usage: 27.9 MB, less than 10.48% of Python3 online submissions for Repeated DNA Sequences.
"""

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        
        word_map = {}
        
        for index in range(len(s) - 9):
            try:
                sub_str = s[index: index+10]
                word_map[sub_str] += 1
            except KeyError:
                word_map[sub_str] = 1
        
        res = []
        for key, value in word_map.items():
            if value > 1:
                res.append(key)
        
        return res
        