"""
346. Moving Average from Data Stream
Easy

938

94

Add to List

Share
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.
 

Example 1:

Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
 

Constraints:

1 <= size <= 1000
-105 <= val <= 105
At most 104 calls will be made to next.
Accepted
197,106
Submissions
265,001
"""

"""
Runtime: 60 ms, faster than 91.63% of Python3 online submissions for Moving Average from Data Stream.
Memory Usage: 17.1 MB, less than 96.28% of Python3 online submissions for Moving Average from Data Stream.
"""

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.max = size
        self.sum = 0
        self.data = []
        

    def next(self, val: int) -> float:
        if len(self.data) == self.max:
            self.sum -= self.data.pop(0)
        
        self.data.append(val)
        self.sum += val
        return float(self.sum/len(self.data))