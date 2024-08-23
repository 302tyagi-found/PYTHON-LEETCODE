# Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.
#
# The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.
from math import gcd
import re


class Solution:
    def fractionAddition(self, expression: str) -> str:
        def lcm(a, b):
            return abs(a * b) // gcd(a, b)

        # Parse the expression using regex to find all fractions
        fractions = re.findall(r'[+-]?\d+/\d+', expression)

        # Initialize numerator and denominator of the result
        numerator = 0
        denominator = 1

        for frac in fractions:
            num, denom = map(int, frac.split('/'))

            # Calculate the new denominator as the least common multiple of current and new denominator
            new_denom = lcm(denominator, denom)

            # Adjust numerators to have the same denominator
            numerator = numerator * (new_denom // denominator) + num * (new_denom // denom)
            denominator = new_denom

        # Simplify the fraction
        common_divisor = gcd(abs(numerator), denominator)
        numerator //= common_divisor
        denominator //= common_divisor

        # Return the result as a string
        return f"{numerator}/{denominator}"