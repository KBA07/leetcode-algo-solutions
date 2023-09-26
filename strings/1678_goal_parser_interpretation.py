"""
1678. Goal Parser Interpretation
Easy
1.4K
85
Companies
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

 

Example 1:

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
Example 2:

Input: command = "G()()()()(al)"
Output: "Gooooal"
Example 3:

Input: command = "(al)G(al)()()G"
Output: "alGalooG"
 

Constraints:

1 <= command.length <= 100
command consists of "G", "()", and/or "(al)" in some order.
Accepted
207.5K
Submissions
239.2K
Acceptance Rate
86.8%
"""

"""
Runtime: 43ms Beats 20.63% of users with Python3
Memory Usage: 16.13MB Beats 81.42% of users with Python3
"""

class Solution:
    def interpret(self, command: str) -> str:
        # replace () with o and (al) with al
        result = ''
        i = 0
        command_len = len(command)
        while i < command_len:

            if i+4 <= command_len and command[i:i+4] == "(al)":
                result += "al"
                i += 4
                continue

            if i+2 <= command_len and command[i:i+2] == "()":
                result += "o"
                i += 2
                continue
            
            result += command[i]
            i += 1
        
        return result
