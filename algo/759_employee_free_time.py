"""
759. Employee Free Time
Hard

978

68

Add to List

Share
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

 

Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
 

Constraints:

1 <= schedule.length , schedule[i].length <= 50
0 <= schedule[i].start < schedule[i].end <= 10^8
Accepted
73,548
Submissions
106,092
"""

"""
Runtime: 72 ms, faster than 98.91% of Python3 online submissions for Employee Free Time.
Memory Usage: 15.7 MB, less than 97.83% of Python3 online submissions for Employee Free Time.
"""

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        calendar = []
        
        for block in schedule:
            for employee in block:
                calendar.append(employee)
        
        
        calendar.sort(key = lambda x:x.start)
        
        busy = [] 
        for event in calendar:
            
            if not busy or event.start > busy[-1].end:
                busy.append(event)
            else:
                busy[-1].end = max(busy[-1].end, event.end)
        
        
        free = []
        for index in range(len(busy) - 1):
            free.append(Interval(busy[index].end, busy[index + 1].start))
                
        return free