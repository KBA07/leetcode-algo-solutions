"""
412. Fizz Buzz
Easy

1470

1662

Add to List

Share
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i if non of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
 

Constraints:

1 <= n <= 104
Accepted
496,798
Submissions
769,659
"""

"""
Runtime: 44 ms, faster than 61.60% of Python3 online submissions for Fizz Buzz.
Memory Usage: 14.9 MB, less than 88.43% of Python3 online submissions for Fizz Buzz.
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for index in range(1, n + 1):
            sub_str = ''
            
            if index % 3 == 0:
                sub_str += 'Fizz'
            
            if index % 5 == 0:
                sub_str += 'Buzz'
                
            if not sub_str:
                sub_str = str(index)
            
            answer.append(sub_str)
        
        return answer
