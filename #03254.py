# You are given an array of integers nums of length n and a positive integer k.
#
# The power of an array is defined as:
#
# Its maximum element if all of its elements are consecutive and sorted in ascending order.
# -1 otherwise.
# You need to find the power of all subarrays of nums of size k.
#
# Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].
#


class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        def is_consecutive_and_sorted(subarray):
            # Check if the subarray is sorted and consecutive
            return all(subarray[i] + 1 == subarray[i + 1] for i in range(len(subarray) - 1))

        n = len(nums)
        result = []

        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            if is_consecutive_and_sorted(subarray):
                result.append(max(subarray))
            else:
                result.append(-1)

        return result