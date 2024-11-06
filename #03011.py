# You are given a 0-indexed array of positive integers nums.
#
# In one operation, you can swap any two adjacent elements if they have the same number of set bits.
# You are allowed to do this operation any number of times (including zero).
#
# Return true if you can sort the array, else return false.

class Solution:
    def haveSameSetBits(self, a: int, b: int) -> bool:
        # Python equivalent of __builtin_popcount(a) to count set bits
        return bin(a).count('1') == bin(b).count('1')

    def canSortArray(self, nums: list[int]) -> bool:
        N = len(nums)
        times = N

        # Perform bubble sort-like operation with condition on set bits
        for _ in range(times):
            for i in range(N - 1):
                if self.haveSameSetBits(nums[i], nums[i + 1]) and nums[i + 1] < nums[i]:
                    # Swap the elements
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]

        # Check if the array is sorted
        return nums == sorted(nums)