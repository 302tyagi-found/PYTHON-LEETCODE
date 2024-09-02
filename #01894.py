// There are n students in a class numbered from 0 to n - 1. The teacher will give each student a problem starting with the student number 0, then the student number 1, and so on until the teacher reaches the student number n - 1. After that, the teacher will restart the process, starting with the student number 0 again.

// You are given a 0-indexed integer array chalk and an integer k. There are initially k pieces of chalk. When the student number i is given a problem to solve, they will use chalk[i] pieces of chalk to solve that problem. However, if the current number of chalk pieces is strictly less than chalk[i], then the student number i will be asked to replace the chalk.

// Return the index of the student that will replace the chalk pieces.


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
    
        # Step 1: Calculate the total chalk needed for one full cycle
        total_chalk = sum(chalk)
        
        # Step 2: Determine how many full cycles can be completed with k pieces of chalk
        k %= total_chalk
        
        # Step 3: Find the student who will replace the chalk
        for i in range(n):
            if k < chalk[i]:
                return i
            k -= chalk[i]

        # If the loop completes, which is theoretically impossible since k < total_chalk after modulo operation
        return -1