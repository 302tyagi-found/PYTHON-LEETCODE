# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, return the Hamming distance between them.
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        x_binary = format(x, 'b')
        y_binary = format(y, 'b')
        max_len = max(len(x_binary), len(y_binary))
        x_binary = x_binary.zfill(max_len)
        y_binary = y_binary.zfill(max_len)
        for i in range(max_len):
            if x_binary[i] != y_binary[i]:
                count += 1
        return count
