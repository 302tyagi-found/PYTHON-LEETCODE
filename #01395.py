# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.
#
# You have to form a team of 3 soldiers amongst them under the following rules:
#
# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k])
# where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).
from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        res = 0
        for i in range(n):
            left_less = left_more = right_less = right_more = 0
            for j in range(i):
                if rating[j] < rating[i]:
                    left_less += 1
                else:
                    left_more += 1
            for k in range(i + 1, n):
                if rating[k] < rating[i]:
                    right_less += 1
                else:
                    right_more += 1

            res += left_less * right_more + left_more * right_less
        return res


solution = Solution()

rating = [2, 5, 3, 4, 1]
print(solution.numTeams(rating))
