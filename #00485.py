# Given a binary array nums, return the maximum number of consecutive 1's in the array.
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count, count, i, n = 0, 0, 0, len(nums)
        while i < n:
            if nums[i] == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
            i += 1
        return max_count

sol = Solution()
nums = [1,0,1,1,0,1]
print(sol.findMaxConsecutiveOnes(nums))