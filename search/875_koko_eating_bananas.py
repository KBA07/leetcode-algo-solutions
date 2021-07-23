"""
875. Koko Eating Bananas
Medium

1791

102

Add to List

Share
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
Accepted
83,579
Submissions
155,235
"""


"""
Time limit exceeeded
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        
        k = piles[0] 
        hour = h
        
        # hour should match completely with k
        while hour:
            piles_copy = piles[:]
            
            while piles_copy and hour:
                piles_copy[-1] -= k
                hour -= 1
                
                if piles_copy[-1] <= 0:
                    piles_copy.pop()
                    
                    
            if piles_copy:
                hour = h
                k += 1
                
        return k

"""
Runtime: 448 ms, faster than 75.89% of Python3 online submissions for Koko Eating Bananas.
Memory Usage: 15.6 MB, less than 19.94% of Python3 online submissions for Koko Eating Bananas.
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # generate a number between 1 and max(piles)
        
        def possible(k):
            return sum(math.ceil(p/k) for p in piles) <= h
        
        low, high = 1, max(piles)
        
        while low < high:
            mid = (low + high) // 2
            
            if not possible(mid):
                low = mid + 1
            else:
                high = mid
        
        return low