# You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.
#
# The chemistry of a team is equal to the product of the skills of the players on that team.
#
# Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.
from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)

        # Sort the array to form pairs from smallest and largest
        skill.sort()

        # The target sum of skills for each team (sum of the first pair)
        target_sum = skill[0] + skill[-1]

        chemistry_sum = 0

        # Try to form teams
        for i in range(n // 2):
            # Pair the ith smallest and ith largest players
            if skill[i] + skill[n - 1 - i] != target_sum:
                return -1  # Teams cannot be formed with equal total skill

            # Add the product (chemistry) of the current team
            chemistry_sum += skill[i] * skill[n - 1 - i]

        return chemistry_sum
