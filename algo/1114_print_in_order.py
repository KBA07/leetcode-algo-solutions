"""
1114. Print in Order
Easy

795

139

Add to List

Share
Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

Note:

We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.

 

Example 1:

Input: nums = [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.
Example 2:

Input: nums = [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.
Accepted
85,735
Submissions
126,656
"""

"""
Runtime: 3216 ms, faster than 18.21% of Python3 online submissions for Print in Order.
Memory Usage: 14.8 MB, less than 8.76% of Python3 online submissions for Print in Order.
"""

class Foo:
    def __init__(self):
        self.lock = [1, 1]


    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.lock[0] = 0


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while True:
            if not self.lock[0]:
                break
        printSecond()
        self.lock[1] = 0


    def third(self, printThird: 'Callable[[], None]') -> None:
        while True:
            if not self.lock[1]:
                break
        printThird()