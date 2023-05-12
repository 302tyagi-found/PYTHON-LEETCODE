# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error,
# one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
# You are given an integer array nums representing the data status of this set after the error.
# Find the number that occurs twice and the number that is missing and return them in the form of an array.
class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        count = {}
        n = len(nums)
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        missing_num = repeated_num = 0
        for i in range(1, n+1):
            if i not in count:
                missing_num = i
            elif count[i]== 2:
                repeated_num = i
        return [missing_num, repeated_num]