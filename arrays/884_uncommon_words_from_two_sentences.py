"""
Easy

679

112

Add to List

Share
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]
 

Constraints:

1 <= s1.length, s2.length <= 200
s1 and s2 consist of lowercase English letters and spaces.
s1 and s2 do not have leading or trailing spaces.
All the words in s1 and s2 are separated by a single space.
Accepted
79,125
Submissions
122,475
"""

"""
Runtime: 28 ms, faster than 86.97% of Python3 online submissions for Uncommon Words from Two Sentences.
Memory Usage: 14.2 MB, less than 82.62% of Python3 online submissions for Uncommon Words from Two Sentences.
"""

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word_map = collections.defaultdict(int)
        
        for word in s1.split(" "):
            word_map[word] += 1
        
        for word in s2.split(" "):
            word_map[word] += 1
        
        result = []
        for word in word_map:
            if word_map[word] == 1:
                result.append(word)
        
        return result
