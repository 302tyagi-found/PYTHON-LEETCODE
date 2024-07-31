# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built - in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
from typing import List

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Base case: if the array has one or zero elements, it's already sorted
        if len(nums) <= 1:
            return nums

        # Find the midpoint of the array
        mid = len(nums) // 2

        # Recursively split and sort the array
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        # Merge the sorted halves
        return self.merge(left, right)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        sorted_array = []
        i = j = 0

        # Merge the two sorted arrays
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1

        # If there are remaining elements in left or right, add them
        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])

        return sorted_array


solution = Solution()
arr = [5, 2, 3, 1]
print(solution.sortArray(arr))