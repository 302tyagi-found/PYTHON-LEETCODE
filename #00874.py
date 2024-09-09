/*** 
A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot can receive a sequence of these three possible types of commands:

-2: Turn left 90 degrees.
-1: Turn right 90 degrees.
1 <= k <= 9: Move forward k units, one unit at a time.
Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). If the robot runs into an obstacle, then it will instead stay in its current location and move on to the next command.

Return the maximum Euclidean distance that the robot ever gets from the origin squared (i.e. if the distance is 5, return 25).

Note:

North means +Y direction.
East means +X direction.
South means -Y direction.
West means -X direction.
There can be obstacle in [0,0].
***/

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Define directions as (dx, dy) for North, East, South, and West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Initialize robot's starting position and direction (facing North)
        x, y = 0, 0
        dir_idx = 0
        max_distance_squared = 0
        
        # Convert obstacles list to a set for quick look-up
        obstacle_set = set(map(tuple, obstacles))
        
        for command in commands:
            if command == -2:  # Turn left 90 degrees
                dir_idx = (dir_idx - 1) % 4
            elif command == -1:  # Turn right 90 degrees
                dir_idx = (dir_idx + 1) % 4
            else:  # Move forward k units
                dx, dy = directions[dir_idx]
                for _ in range(command):
                    next_x, next_y = x + dx, y + dy
                    if (next_x, next_y) in obstacle_set:
                        break
                    x, y = next_x, next_y
                    # Compute distance squared from the origin
                    distance_squared = x * x + y * y
                    if distance_squared > max_distance_squared:
                        max_distance_squared = distance_squared
        
        return max_distance_squared