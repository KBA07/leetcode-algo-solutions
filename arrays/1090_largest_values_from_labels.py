"""
1090. Largest Values From Labels
Medium

216

481

Add to List

Share
We have a set of items: the i-th item has value values[i] and label labels[i].

Then, we choose a subset S of these items, such that:

|S| <= num_wanted
For every label L, the number of items in S with label L is <= use_limit.
Return the largest possible sum of the subset S.

 

Example 1:

Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit = 1
Output: 9
Explanation: The subset chosen is the first, third, and fifth item.
Example 2:

Input: values = [5,4,3,2,1], labels = [1,3,3,3,2], num_wanted = 3, use_limit = 2
Output: 12
Explanation: The subset chosen is the first, second, and third item.
Example 3:

Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 1
Output: 16
Explanation: The subset chosen is the first and fourth item.
Example 4:

Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 2
Output: 24
Explanation: The subset chosen is the first, second, and fourth item.
 

Note:

1 <= values.length == labels.length <= 20000
0 <= values[i], labels[i] <= 20000
1 <= num_wanted, use_limit <= values.length
Accepted
22,112
Submissions
36,639
"""

"""
Time limit exceeded
79/81 test case passed
"""

class Solution:
    def insert(self, value, label):
        self.data.append([value, label])
        self.count += 1
        
        node_point = self.count
        
        while node_point >= 1:
            if not self.isLeaf(node_point):
                left_index = 2 * node_point
                right_index = 2 * node_point + 1
                
                index = left_index
                if right_index <= self.count and self.data[right_index][0] > self.data[left_index][0]:
                    index = right_index
                
                if self.data[node_point][0] >= self.data[index][0]:
                    break
                    
                self.data[node_point], self.data[index] = self.data[index], self.data[node_point]
                node_point = node_point // 2
            else:
                node_point -= 1
    
    def remove(self):
        if self.count > 0:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            val = self.data.pop()
            self.count -= 1

            node_point = 1

            while node_point <= self.count:
                if not self.isLeaf(node_point):
                    left_index = 2 * node_point
                    right_index = 2 * node_point + 1

                    index = left_index
                    if right_index <= self.count and self.data[right_index][0] > self.data[left_index][0]:
                        index = right_index

                    if self.data[node_point][0] >= self.data[index][0]:
                        break

                    self.data[node_point], self.data[index] = self.data[index], self.data[node_point]
                    node_point = index
                else:
                    node_point += 1
                    
            return val

            
    
    def isLeaf(self, point):
        return 2 * point > self.count
        
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        self.data = ['#']
        self.count = 0
        
        labels_map = {}
        answer = 0
        for index in range(len(values)):
            self.insert(values[index], labels[index])
        
        while self.count > 0 and num_wanted:
            node = self.remove()
            
            try:
                labels_map[node[1]].append(node[0])
            except KeyError:
                labels_map[node[1]] = [node[0]]
            
            if len(labels_map[node[1]]) <= use_limit:
                answer += node[0]
                num_wanted -= 1
        
        return answer


"""
Runtime: 440 ms, faster than 5.40% of Python3 online submissions for Largest Values From Labels.
Memory Usage: 18.5 MB, less than 77.27% of Python3 online submissions for Largest Values From Labels.
"""

# Only traverse the heap till N/2 nodes
class Solution:
    def insert(self, value, label):
        self.data.append([value, label])
        self.count += 1
        
        node_point = self.count // 2
        
        while node_point >= 1:
            if not self.isLeaf(node_point):
                left_index = 2 * node_point
                right_index = 2 * node_point + 1
                
                index = left_index
                if right_index <= self.count and self.data[right_index][0] > self.data[left_index][0]:
                    index = right_index
                
                if self.data[node_point][0] >= self.data[index][0]:
                    break
                    
                self.data[node_point], self.data[index] = self.data[index], self.data[node_point]
                node_point = node_point // 2
            else:
                node_point -= 1
    
    def remove(self):
        if self.count > 0:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            val = self.data.pop()
            self.count -= 1

            node_point = 1
            limit = self.count // 2
            while node_point <= limit:
                if not self.isLeaf(node_point):
                    left_index = 2 * node_point
                    right_index = 2 * node_point + 1

                    index = left_index
                    if right_index <= self.count and self.data[right_index][0] > self.data[left_index][0]:
                        index = right_index

                    if self.data[node_point][0] >= self.data[index][0]:
                        break

                    self.data[node_point], self.data[index] = self.data[index], self.data[node_point]
                    node_point = index
                else:
                    node_point += 1
                    
            return val

            
    
    def isLeaf(self, point):
        return 2 * point > self.count
        
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        self.data = ['#']
        self.count = 0
        
        labels_map = {}
        answer = 0
        for index in range(len(values)):
            self.insert(values[index], labels[index])
        
        while self.count > 0 and num_wanted:
            node = self.remove()
            
            try:
                labels_map[node[1]].append(node[0])
            except KeyError:
                labels_map[node[1]] = [node[0]]
            
            if len(labels_map[node[1]]) <= use_limit:
                answer += node[0]
                num_wanted -= 1
        
        return answer
