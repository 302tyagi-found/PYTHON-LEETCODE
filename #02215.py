# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.
class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        answer = [[], []]
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        for num in set_nums1-set_nums2:
            answer[0].append(num)
        for num in set_nums2-set_nums1:
            answer[1].append(num)
        return answer


sol = Solution()
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
print(sol.findDifference(nums1, nums2))