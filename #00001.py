# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        output = {}

        for i in range(len(numbers)):
            diff = target - numbers[i]
            if(diff in output):
                return [output[diff], i]
            else:
                output[numbers[i]] = i


print(Solution.twoSum(self=True, numbers=[5, 4, 3, 2, 1], target=5))
