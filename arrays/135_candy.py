"""
135. Candy
Hard
7.1K
522
Companies
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
 

Constraints:

n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104
Accepted
411.6K
Submissions
950.6K
Acceptance Rate
43.3%    
"""

"""
Runtime: 136ms Beats 87.16% of users with Python3
Memory Usage: 19.22MB Beats 70.30% of users with Python3
"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies) 
        
"""
Runtime: 127ms Beats 98.55% of users with Python3
Memory Usage: 19.22MB Beats 60.07% of users with Python3
"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = 1
        up, down, peak = 0, 0, 0

        for i in range(1, len(ratings)):

            if ratings[i] > ratings[i-1]:
                up += 1
                down = 0
                peak = up + 1
                candies += peak
            elif ratings[i] == ratings[i-1]:
                up = 0
                down = 0
                peak = 0
                candies += 1
            else:
                up = 0
                down += 1
                candies += down + 1 - (peak > down)
        
        return candies

