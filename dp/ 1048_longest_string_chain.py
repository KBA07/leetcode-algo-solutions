"""
1048. Longest String Chain
Medium

2227

117

Add to List

Share
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

 

Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of lowercase English letters.
Accepted
129,689
Submissions
230,172
"""

"""
Runtime: 160 ms, faster than 59.69% of Python3 online submissions for Longest String Chain.
Memory Usage: 16.2 MB, less than 20.44% of Python3 online submissions for Longest String Chain.
"""

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_set = set()
        for word in words:
            word_set.add(word)
        
        self.cache = {}
            
        def dfs(word, word_set, count):
            if word in self.cache:
                return self.cache[word]
            
            max_len = 1
            curr_count = 0
            for index in range(len(word)):
                new_word = word[:index] + word[index + 1:]

                if new_word in word_set:
                    curr_count = 1 + dfs(new_word, word_set, count)

                max_len = max(max_len, curr_count)
                
            self.cache[word] = max_len

            return max_len
        
        result = 0
        for word in word_set:
            result = max(result, dfs(word, word_set, count))
                         
        return result