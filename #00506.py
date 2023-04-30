class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        sorted_score = sorted(score, reverse=True)
        rank_dict = {}
        output = []

        for i, s in enumerate(sorted_score):
            if i == 0:
                rank_dict[s] = 'Gold Medal'
            elif i == 1:
                rank_dict[s] = 'Silver Medal'
            elif i == 2:
                rank_dict[s] = 'Bronze Medal'
            else:
                rank_dict[s] = str(i+1)

        for val in score:
            output.append(rank_dict[val])
        return output

sol = Solution()
score = [10, 1, 30, 4]
print(sol.findRelativeRanks(score))
