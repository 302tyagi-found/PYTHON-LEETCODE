# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique
# and you may return the result in any order.
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        output = list(set1.intersection(set2))
        return output