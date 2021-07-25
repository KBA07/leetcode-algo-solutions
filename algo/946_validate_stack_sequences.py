"""
946. Validate Stack Sequences
Medium

1917

36

Add to List

Share
Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

 

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
 

Constraints:

0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed is a permutation of popped.
pushed and popped have distinct values.
Accepted
111,106
Submissions
172,165
"""

"""
Runtime: 72 ms, faster than 64.77% of Python3 online submissions for Validate Stack Sequences.
Memory Usage: 14.6 MB, less than 27.99% of Python3 online submissions for Validate Stack Sequences.
"""

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = [] 
        i = j = 0
        m, n = len(pushed), len(pushed)
        while i < m and j < n:
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            
            stack.append(pushed[i])
            i += 1
        
        while j < n and stack[-1] == popped[j]:
            stack.pop()
            j += 1
        
        return i == m and j == n


"""
Runtime: 72 ms, faster than 64.77% of Python3 online submissions for Validate Stack Sequences.
Memory Usage: 14.5 MB, less than 58.67% of Python3 online submissions for Validate Stack Sequences.
"""
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = [] 
        j = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        
        return not stack

"""
Runtime: 68 ms, faster than 84.78% of Python3 online submissions for Validate Stack Sequences.
Memory Usage: 14.6 MB, less than 27.99% of Python3 online submissions for Validate Stack Sequences.
"""
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        i = j = 0
        for num in pushed:
            pushed[i] = num
            while i >= 0 and pushed[i] == popped[j]:
                i -= 1
                j += 1
            i += 1
        
        return i == 0