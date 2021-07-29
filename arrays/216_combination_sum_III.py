"""
216. Combination Sum III
Medium

2064

67

Add to List

Share
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
Example 4:

Input: k = 3, n = 2
Output: []
Explanation: There are no valid combinations.
Example 5:

Input: k = 9, n = 45
Output: [[1,2,3,4,5,6,7,8,9]]
Explanation:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
There are no other valid combinations.
 

Constraints:

2 <= k <= 9
1 <= n <= 60
Accepted
240,511
Submissions
389,840
"""

"""
4 / 18 test cases passed
Time Limit Exceeded
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        seen = set()
        answer = []
        def dfs(curr_list, seen, answer):
            
            word = ''.join(str(num) for num in curr_list)
            if word in seen:
                return
             
            for num in curr_list:
                if num < 1:
                    return
            
            # print(curr_list)
            if sum(curr_list) == n and len(set(curr_list)) == k:
                # print(curr_list)
                seen.add(word)
                answer.append(curr_list[:])
                # print(answer)
                    
            for i in range(k):
                curr_list[i] -= 1
                dfs(curr_list[:], seen,answer)
        
        dfs([9]*k, seen, answer)
        # print(answer)
        return answer
            
"""
Runtime: 28 ms, faster than 90.65% of Python3 online submissions for Combination Sum III.
Memory Usage: 14.3 MB, less than 27.69% of Python3 online submissions for Combination Sum III.
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        answer = []
        def dfs(n, curr_list, start):
            
            if n < 0 or len(curr_list) > k:
                return
            
            if n == 0 and len(curr_list) == k:
                answer.append(curr_list[:])
                return
             
            for num in range(start, 10):
                curr_list.append(num)
                dfs(n - num, curr_list[:], num + 1)
                curr_list.pop()
        
        dfs(n, [], 1)
        return answer