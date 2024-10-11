# There is a party where n friends numbered from 0 to n - 1 are attending. There is an infinite number of chairs in this party that are numbered from 0 to infinity. When a friend arrives at the party, they sit on the unoccupied chair with the smallest number.
#
# For example, if chairs 0, 1, and 5 are occupied when a friend comes, they will sit on chair number 2.
# When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at that same moment, they can sit in that chair.
#
# You are given a 0-indexed 2D integer array times where times[i] = [arrivali, leavingi], indicating the arrival and leaving times of the ith friend respectively, and an integer targetFriend. All arrival times are distinct.
#
# Return the chair number that the friend numbered targetFriend will sit on.
import heapq
from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)

        # List of (arrival, leave, friend_index) tuples for all friends
        events = [(times[i][0], times[i][1], i) for i in range(n)]

        # Sort events by arrival time
        events.sort()

        # Min-heap for available chairs
        available_chairs = []

        # We will also store the chair currently assigned to each friend
        friend_chairs = [-1] * n  # Initialize all with -1 (means no chair yet)

        # Min-heap to store (leave_time, chair_index) for friends who will leave
        occupied = []

        # Add all the chair indices to available_chairs heap, assuming infinite chairs
        for i in range(n):
            heapq.heappush(available_chairs, i)

        # Process events in chronological order
        for arrival, leaving, friend in events:
            # Release chairs for friends who have already left by the time of this arrival
            while occupied and occupied[0][0] <= arrival:
                leave_time, chair = heapq.heappop(occupied)
                heapq.heappush(available_chairs, chair)  # This chair becomes available

            # Assign the smallest available chair to the current friend
            chair = heapq.heappop(available_chairs)
            friend_chairs[friend] = chair

            # If this is the targetFriend, return the chair immediately
            if friend == targetFriend:
                return chair

            # Mark this chair as occupied until the friend leaves
            heapq.heappush(occupied, (leaving, chair))

        return -1  # Shouldn't reach here since targetFriend is guaranteed to arrive