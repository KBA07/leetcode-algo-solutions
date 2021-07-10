"""
49. Group Anagrams
Medium

5937

240

Add to List

Share
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
Accepted
970,780
Submissions
1,599,037
"""

"""
Runtime: 88 ms, faster than 96.62% of Python3 online submissions for Group Anagrams.
Memory Usage: 17.2 MB, less than 77.32% of Python3 online submissions for Group Anagrams.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
        
        return list(anagram_dict.values())
