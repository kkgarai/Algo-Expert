"""
Meeting Rooms

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],.....],
find the minimum number of conference rooms required.

Example 1:
Input: [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input : [[7,10],[2,4]]
Output: 1
"""


class Solution:
    @classmethod
    def meetingRooms(self, intervals) :
        start = []
        end = []
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        start.sort()
        end.sort()

        s = 0
        e = 0
        numRooms = 0
        available = 0

        while s < len(start):
            if start[s] < end[e]:
                if available:
                    available -= 1
                else:
                    numRooms += 1
                s += 1
            else:
                available += 1
                e += 1
        return numRooms


print(Solution.meetingRooms([[0, 30], [5, 10], [15, 20],[4,6]]))
