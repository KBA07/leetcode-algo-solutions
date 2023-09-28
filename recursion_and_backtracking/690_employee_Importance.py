"""
690. Employee Importance
Easy

1186

986

Add to List

Share
You have a data structure of employee information, which includes the employee's unique id, their importance value, and their direct subordinates' id.

You are given an array of employees employees where:

employees[i].id is the ID of the ith employee.
employees[i].importance is the importance value of the ith employee.
employees[i].subordinates is a list of the IDs of the subordinates of the ith employee.
Given an integer id that represents the ID of an employee, return the total importance value of this employee and all their subordinates.

 

Example 1:


Input: employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
Output: 11
Explanation: Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3.
They both have importance value 3.
So the total importance value of employee 1 is 5 + 3 + 3 = 11.
Example 2:


Input: employees = [[1,2,[5]],[5,-3,[]]], id = 5
Output: -3
 

Constraints:

1 <= employees.length <= 2000
1 <= employees[i].id <= 2000
All employees[i].id are unique.
-100 <= employees[i].importance <= 100
One employee has at most one direct leader and may have several subordinates.
id is guaranteed to be a valid employee id.
"""

"""
Runtime: 152 ms, faster than 86.22% of Python3 online submissions for Employee Importance.
Memory Usage: 15.7 MB, less than 37.67% of Python3 online submissions for Employee Importance.
"""


"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # important_employees = [id]
        employee_map = {}
        
        for employee in employees:
            employee_map[employee.id] = [employee.importance, employee.subordinates]
            
        employee_map['ans'] = 0
        
        def helper(emp_id, employee_map):
            employee_map['ans'] += employee_map[emp_id][0]
            
            if not employee_map[emp_id][1]:
                return
            
            for e_id in employee_map[emp_id][1]:
                helper(e_id, employee_map)
        
        helper(id, employee_map)
        
        return employee_map['ans']
            