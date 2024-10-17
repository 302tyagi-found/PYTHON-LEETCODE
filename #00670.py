# You are given an integer num. You can swap two digits at most once to get the maximum valued number.
#
# Return the maximum valued number you can get.

class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))

        # Create an array to track the index of the maximum digit from right to left
        max_idx = len(digits) - 1
        max_digit = [0] * len(digits)
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] > digits[max_idx]:
                max_idx = i
            max_digit[i] = max_idx

        # Try to find the first place where a swap will give a higher number
        for i in range(len(digits)):
            if digits[i] != digits[max_digit[i]]:
                # Swap the current digit with the maximum digit found later
                digits[i], digits[max_digit[i]] = digits[max_digit[i]], digits[i]
                break

        # Convert the list of digits back to a number
        return int(''.join(digits))