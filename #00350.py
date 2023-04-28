# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as
# many times as it shows in both arrays and you may return the result in any order.
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        count = {}
        for num in nums1:
            count[num] = count.get(num, 0) + 1
        result = []
        for num in nums2:
            if num in count and count[num] > 0:
                result.append(num)
                count[num] -= 1
        return result
