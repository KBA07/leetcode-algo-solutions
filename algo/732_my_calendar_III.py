"""
732. My Calendar III
Hard

547

128

Add to List

Share
A k-booking happens when k events have some non-empty intersection (i.e., there is some time that is common to all k events.)

You are given some events [start, end), after each given event, return an integer k representing the maximum k-booking between all the previous events.

Implement the MyCalendarThree class:

MyCalendarThree() Initializes the object.
int book(int start, int end) Returns an integer k representing the largest integer such that there exists a k-booking in the calendar.
 

Example 1:

Input
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, 1, 1, 2, 3, 3, 3]

Explanation
MyCalendarThree myCalendarThree = new MyCalendarThree();
myCalendarThree.book(10, 20); // return 1, The first event can be booked and is disjoint, so the maximum k-booking is a 1-booking.
myCalendarThree.book(50, 60); // return 1, The second event can be booked and is disjoint, so the maximum k-booking is a 1-booking.
myCalendarThree.book(10, 40); // return 2, The third event [10, 40) intersects the first event, and the maximum k-booking is a 2-booking.
myCalendarThree.book(5, 15); // return 3, The remaining events cause the maximum K-booking to be only a 3-booking.
myCalendarThree.book(5, 10); // return 3
myCalendarThree.book(25, 55); // return 3
 

Constraints:

0 <= start < end <= 109
At most 400 calls will be made to book.
Accepted
31,535
Submissions
49,330
"""

"""
In progress
"""

class CalendarNode(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
    
    def insert(self, start, end):
        if end <= self.start:
            if not self.left:
                self.left = CalendarNode(start, end)
                return True
            return self.left.insert(start, end)
        elif start >= self.end:
            if not self.right:
                self.right = CalendarNode(start, end)
                return True
            return self.right.insert(start, end)
        else:
            return False
            
            
        
class MyCalendarThree:

    def __init__(self):
        self.k = 1
        self.root = None
        
    def book(self, start: int, end: int) -> int:
        if not self.root:
            self.root = CalendarNode(start, end)
            return self.k
        
        inserted = self.root.insert(start, end)
        print(start, end, 'inserted', inserted)
        if not inserted:
            self.k += 1
        
        return self.k
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)

"""
Runtime: 1352 ms, faster than 63.42% of Python3 online submissions for My Calendar III.
Memory Usage: 14.8 MB, less than 52.14% of Python3 online submissions for My Calendar III.
"""

class MyCalendarThree(object):
    def __init__(self):
        self.delta = collections.Counter()
        
    def book(self, start, end):
        self.delta[start] += 1
        self.delta[end] -= 1
        
        active = ans = 0
        print(self.delta)
        for x in sorted(self.delta):
            print(active)
            active += self.delta[x]
            
            if active > ans:
                ans = active
        
        return ans


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
