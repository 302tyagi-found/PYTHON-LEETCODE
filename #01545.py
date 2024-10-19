# Given two positive integers n and k, the binary string Sn is formed as follows:
#
# S1 = "0"
# Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
# Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).
#
# For example, the first four strings in the above sequence are:
#
# S1 = "0"
# S2 = "011"
# S3 = "0111001"
# S4 = "011100110110001"
# Return the kth bit in Sn. It is guaranteed that k is valid for the given n.
#
#

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Helper function to invert the bit
        def invert(bit):
            return '0' if bit == '1' else '1'

        # Base case: S1 is "0"
        if n == 1:
            return '0'

        # Calculate the length of Sn, which is 2^n - 1
        length = (1 << n) - 1  # This is 2^n - 1

        # Middle element is always 1, check if k is the middle
        mid = (length // 2) + 1
        if k == mid:
            return '1'

        # If k is in the left half, it corresponds to Sn-1
        if k < mid:
            return self.findKthBit(n - 1, k)

        # If k is in the right half, it corresponds to reverse-inverted Sn-1
        # Calculate the mirror position in Sn-1
        mirror_pos = length - k + 1
        return invert(self.findKthBit(n - 1, mirror_pos))