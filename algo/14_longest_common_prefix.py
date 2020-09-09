"""
14. Longest Common Prefix
Easy

2908

1942

Add to List

Share
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
"""
Runtime: 52 ms, faster than 5.54% of Python online submissions for Longest Common Prefix.
Memory Usage: 12.8 MB, less than 74.05% of Python online submissions for Longest Common Prefix.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or not strs[0]:
            return ""

        count_dict = {}
        count_list = [1] * len(strs[0])
        for index, char in enumerate(strs[0]):
            try:
                count_dict[char].append(index)
            except KeyError:
                count_dict[char] = [index]

        for index in range(1, len(strs)):
            for inner_index, char in enumerate(strs[index]):
                if char in count_dict and inner_index in count_dict[char]:
                    count_list[inner_index] += 1

        value = count_list[0]
        pref = ""
        if value == len(strs):
            pref = strs[0][0]
            for index in range(1, len(count_list)):
                value = count_list[index]
                if value == len(strs):
                    pref += strs[0][index]
                else:
                    break

        return pref

"""
Runtime: 16 ms, faster than 96.36% of Python online submissions for Longest Common Prefix.
Memory Usage: 12.7 MB, less than 80.23% of Python online submissions for Longest Common Prefix.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest = ""

        if not strs:
            return longest

        current_pointer = 0
        first_word = strs[0]

        for letter in first_word:

            for index in range(1, len(strs)):
                current_word = strs[index]
                if current_pointer > len(current_word) - 1:
                    return longest

                comp_letter = current_word[current_pointer]

                if comp_letter != letter:
                    return longest

            longest += letter
            current_pointer += 1

        return longest