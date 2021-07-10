"""
Very good question
403. Frog Jump
Hard

1693

137

Add to List

Share
A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.

 

Example 1:

Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:

Input: stones = [0,1,2,3,4,8,9,11]
Output: false
Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.
 

Constraints:

2 <= stones.length <= 2000
0 <= stones[i] <= 231 - 1
stones[0] == 0
Accepted
126,383
Submissions
301,094
"""

"""
Runtime: 140 ms, faster than 82.51% of Python3 online submissions for Frog Jump.
Memory Usage: 19.2 MB, less than 47.40% of Python3 online submissions for Frog Jump.
"""

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        self.dead_end = set()
        self.stones = set(stones)
        self.target = stones[-1]
        
        return self.checkJump(1, 1)
    
    def checkJump(self, curr_stone, speed):
        # Frog has reached a dead end
        if (curr_stone, speed) in self.dead_end:
            return False
        
        # Frog is at the last stone
        if curr_stone == self.target:
            return True
        
        # Frog has over shot the rocks
        if curr_stone < 0 or curr_stone > self.target or curr_stone not in self.stones or speed <= 0:
            return False
        
        posibilities = [speed, speed - 1, speed + 1]
        
        for jump in posibilities:
            
            if curr_stone + jump in self.stones:
                if self.checkJump(curr_stone + jump, jump):
                    return True
        
        self.dead_end.add((curr_stone, speed))
        return False
