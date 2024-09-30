# Design a stack that supports increment operations on its elements.
#
# Implement the CustomStack class:
#
# CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
# void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
# int pop() Pops and returns the top of the stack or -1 if the stack is empty.
# void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, increment all the elements in the stack.
#


class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.increment_value = [0] * maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
        else:
            pass

    def pop(self) -> int:
        if not self.stack:
            return -1
        idx = len(self.stack) - 1
        res = self.stack.pop() + self.increment_value[idx]
        if idx > 0:
            self.increment_value[idx - 1] += self.increment_value[idx]
        self.increment_value[idx] = 0
        return res

    def increment(self, k: int, val: int) -> None:
        num_element = min(k, len(self.stack))
        if num_element > 0:
            self.increment_value[num_element - 1] += val
