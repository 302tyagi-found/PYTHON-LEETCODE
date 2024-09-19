# Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.
#
# The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}

        # Helper function to compute all results recursively
        def compute(expression: str) -> List[int]:
            # If the expression has been computed before, return the cached result
            if expression in memo:
                return memo[expression]

            # Store the result of all possible computations
            result = []

            # Divide and conquer: split the expression at every operator
            for i in range(len(expression)):
                if expression[i] in "+-*":
                    # Recursively compute the left and right parts
                    left = compute(expression[:i])
                    right = compute(expression[i + 1:])

                    # Combine the results from left and right parts based on the operator
                    for l in left:
                        for r in right:
                            if expression[i] == '+':
                                result.append(l + r)
                            elif expression[i] == '-':
                                result.append(l - r)
                            elif expression[i] == '*':
                                result.append(l * r)

            # Base case: If the expression is just a number, convert it to an integer
            if not result:
                result.append(int(expression))

            # Cache the result for the current expression
            memo[expression] = result
            return result

        # Start the recursive computation for the entire expression
        return compute(expression)
