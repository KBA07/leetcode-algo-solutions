"""
332. Reconstruct Itinerary
Hard
5K
1.7K
Companies
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

 

Example 1:


Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
Example 2:


Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
 

Constraints:

1 <= tickets.length <= 300
tickets[i].length == 2
fromi.length == 3
toi.length == 3
fromi and toi consist of uppercase English letters.
fromi != toi
Accepted
354K
Submissions
842.4K
Acceptance Rate
42.0%
"""

"""
Runtime: 93ms Beats 45.39% of users with Python3
Memory Usage: 16.53MB Beats 96.49% of users with Python3
"""

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for source, destination in sorted(tickets, reverse=True): # Sort in alphabetically decending
            graph[source].append(destination)

        stack = ["JFK"]
        results = []

        while stack:

            curr_airport = stack[-1]

            while graph[curr_airport]:
                stack.append(graph[curr_airport].pop())
                curr_airport = stack[-1]

            results.append(stack.pop())
        
        return results[::-1]