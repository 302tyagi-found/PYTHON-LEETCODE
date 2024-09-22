# Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(curr, n):
            steps = 0
            first = curr
            last = curr
            while first <= n:
                steps += min(last, n) - first + 1
                first *= 10
                last = last * 10 + 9
            return steps

        curr = 1
        k -= 1  # We treat k as 0-indexed

        while k > 0:
            steps = count_steps(curr, n)
            if steps <= k:
                curr += 1  # Move to the next prefix
                k -= steps
            else:
                curr *= 10  # Go deeper into the current prefix
                k -= 1

        return curr