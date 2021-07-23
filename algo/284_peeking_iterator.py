"""
284. Peeking Iterator
Medium

841

584

Add to List

Share
Design an iterator that supports the peek operation on a list in addition to the hasNext and the next operations.

Implement the PeekingIterator class:

PeekingIterator(int[] nums) Initializes the object with the given integer array nums.
int next() Returns the next element in the array and moves the pointer to the next element.
bool hasNext() Returns true if there are still elements in the array.
int peek() Returns the next element in the array without moving the pointer.
 

Example 1:

Input
["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 2, 2, 3, false]

Explanation
PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [1,2,3]
peekingIterator.next();    // return 1, the pointer moves to the next element [1,2,3].
peekingIterator.peek();    // return 2, the pointer does not move [1,2,3].
peekingIterator.next();    // return 2, the pointer moves to the next element [1,2,3]
peekingIterator.next();    // return 3, the pointer moves to the next element [1,2,3]
peekingIterator.hasNext(); // return False
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 1000
All the calls to next and peek are valid.
At most 1000 calls will be made to next, hasNext, and peek.
 

Follow up: How would you extend your design to be generic and work with all types, not just integer?
Accepted
139,862
Submissions
270,736
"""

"""
Runtime: 32 ms, faster than 66.24% of Python3 online submissions for Peeking Iterator.
Memory Usage: 14.2 MB, less than 95.19% of Python3 online submissions for Peeking Iterator.
"""

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.peekValue = None
        self.iterator = iterator
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.peekValue:
            if not self.iterator.hasNext():
                raise StopIteration()
            self.peekValue = self.iterator.next()
            
        return self.peekValue

    def next(self):
        """
        :rtype: int
        """
        if self.peekValue:
            val = self.peekValue
            self.peekValue = None
            return val
        
        if not self.iterator.hasNext():
            raise StopIteration()
        
        return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.peekValue is not None or self.iterator.hasNext()

        
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].