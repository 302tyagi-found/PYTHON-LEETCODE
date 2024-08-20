//Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

//Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

//On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

//The game continues until all the stones have been taken.

//Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

//Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

//On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

//The game continues until all the stones have been taken.

//Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        # Prefix sums to calculate sum of any subarray efficiently
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + piles[i]
        
        # dp[i][M] - Maximum stones Alice can get from index i with max pick limit M
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Fill dp table
        for i in range(n - 1, -1, -1):
            for M in range(1, n + 1):
                max_stones = 0
                # Try picking from 1 to min(2M, remaining piles)
                for X in range(1, min(2 * M, n - i) + 1):
                    picked_sum = prefix_sum[i + X] - prefix_sum[i]
                    remaining_stones = prefix_sum[n] - prefix_sum[i + X]
                    next_M = max(M, X)
                    
                    # Check if the next state is within bounds
                    if i + X <= n:
                        max_stones = max(max_stones, picked_sum + (remaining_stones - dp[i + X][next_M]))
                dp[i][M] = max_stones
        
        return dp[0][1]