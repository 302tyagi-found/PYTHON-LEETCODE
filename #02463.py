# There are some robots and factories on the X-axis. You are given an integer array robot where robot[i] is the position of the ith robot. You are also given a 2D integer array factory where factory[j] = [positionj, limitj] indicates that positionj is the position of the jth factory and that the jth factory can repair at most limitj robots.
#
# The positions of each robot are unique. The positions of each factory are also unique. Note that a robot can be in the same position as a factory initially.
#
# All the robots are initially broken; they keep moving in one direction. The direction could be the negative or the positive direction of the X-axis. When a robot reaches a factory that did not reach its limit, the factory repairs the robot, and it stops moving.
#
# At any moment, you can set the initial direction of moving for some robot. Your target is to minimize the total distance traveled by all the robots.
#
# Return the minimum total distance traveled by all the robots. The test cases are generated such that all the robots can be repaired.
#
# Note that
#
# All robots move at the same speed.
# If two robots move in the same direction, they will never collide.
# If two robots move in opposite directions and they meet at some point, they do not collide. They cross each other.
# If a robot passes by a factory that reached its limits, it crosses it as if it does not exist.
# If the robot moved from a position x to a position y, the distance it moved is |y - x|.
#

from typing import List
from functools import lru_cache


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # Sort robots and factories based on their positions
        robot.sort()
        factory.sort()

        # Extract factory positions and limits into separate lists
        factory_positions = [f[0] for f in factory]
        factory_limits = [f[1] for f in factory]

        # Memoized recursive function
        @lru_cache(None)
        def dp(robot_idx: int, factory_idx: int) -> int:
            # If all robots are assigned, no more distance to add
            if robot_idx == len(robot):
                return 0
            # If we run out of factories, return an arbitrarily large number (infeasible path)
            if factory_idx == len(factory_positions):
                return float('inf')

            # Option 1: Move to the next factory without assigning the current robot to this factory
            min_distance = dp(robot_idx, factory_idx + 1)

            # Option 2: Assign robots to this factory up to its limit
            total_distance = 0
            for i in range(factory_limits[factory_idx]):
                # Calculate distance if we assign `robot[robot_idx + i]` to `factory[factory_idx]`
                if robot_idx + i < len(robot):
                    total_distance += abs(robot[robot_idx + i] - factory_positions[factory_idx])
                    # Recursive call to check further assignments
                    min_distance = min(min_distance, total_distance + dp(robot_idx + i + 1, factory_idx + 1))
                else:
                    break

            return min_distance

        # Start the recursion from the first robot and first factory
        return dp(0, 0)