"""
904. Fruit Into Baskets
Medium

1287

1803

Add to List

Share
You have a row of trees. You are given an integer array fruits where fruits[i] is the type of fruits the ith tree produces.

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets. If you cannot, stop.
Move to the next tree to the right of the current tree. If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
Example 4:

Input: fruits = [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.
 

Constraints:

1 <= fruits.length <= 105
0 <= fruits[i] <= fruits.length
Accepted
139,885
Submissions
324,007
"""

"""
Runtime: 768 ms, faster than 72.69% of Python3 online submissions for Fruit Into Baskets.
Memory Usage: 20.2 MB, less than 24.17% of Python3 online submissions for Fruit Into Baskets.
"""

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_dict = {}
        count = 0
        i = 0
        j = 0
        
        while j < len(fruits):
            if len(fruit_dict) <= 2:
                # will run 3 time, at 0, 1, 2
                # fruit dicts is less than 2 then add the starting value fruit into the dict
                fruit_dict[fruits[j]] = j
                j += 1
            
            if len(fruit_dict) > 2:
                # move i and remove the lowest value from dict
                min_fruit_idx = min(fruit_dict.values()) # incrementing to next value
                fruit_dict.pop(fruits[min_fruit_idx])
                i = min_fruit_idx + 1
                
            count = max(count, j - i)  
        
        return count

"""
Runtime: 748 ms, faster than 78.36% of Python3 online submissions for Fruit Into Baskets.
Memory Usage: 20.1 MB, less than 68.31% of Python3 online submissions for Fruit Into Baskets.
"""
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = {}
        
        lastTree = 0
        fruitCount = 0
        for tree in range(len(fruits)):
            if len(baskets) <= 2:
                baskets[fruits[tree]] = tree
            
            if len(baskets) > 2:
                lastTree = min(baskets.values())
                baskets.pop(fruits[lastTree])
                
                lastTree += 1
            
            fruitCount = max(fruitCount, tree - lastTree + 1)
        
        return fruitCount