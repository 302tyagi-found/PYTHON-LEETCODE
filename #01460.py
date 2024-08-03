# You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray of arr and reverse it. You are allowed to make any number of steps.
#
# Return true if you can make arr equal to target or false otherwise.
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        arrFreq = {}
        for num in arr:
            arrFreq[num] = arrFreq.get(num, 0) + 1

        for num in target:
            if num not in arrFreq:
                return False

            arrFreq[num] -= 1
            if arrFreq[num] == 0:
                del arrFreq[num]
        return len(arrFreq) == 0


solution = Solution()
arr = [2, 4, 1, 3]
target = [2, 4, 3, 1]
print(solution.canBeEqual(target, arr))
