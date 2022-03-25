"""
1094. Car Pooling
Medium

There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.



Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false

Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true



Constraints:

    1 <= trips.length <= 1000
    trips[i].length == 3
    1 <= numPassengersi <= 100
    0 <= fromi < toi <= 1000
    1 <= capacity <= 105

Accepted
145,739
Submissions
249,605
"""

"""
Runtime: 115 ms, faster than 42.32% of Python3 online submissions for Car Pooling.
Memory Usage: 14.5 MB, less than 53.65% of Python3 online submissions for Car Pooling.
"""

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timeline = []

        for trip in trips:
            passengers, from_, to = trip
            timeline.append([from_, 1, passengers])
            timeline.append([to, 0, passengers])

        timeline.sort()

        for trip in timeline:
            _, entry, passengers = trip

            if entry:
                capacity -= passengers
            else:
                capacity += passengers

            if capacity < 0:
                return False

        return True
