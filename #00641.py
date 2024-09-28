# Design your implementation of the circular double-ended queue (deque).
#
# Implement the MyCircularDeque class:
#
# MyCircularDeque(int k) Initializes the deque with a maximum size of k.
# boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
# boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
# boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
# boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
# int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
# int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
# boolean isEmpty() Returns true if the deque is empty, or false otherwise.
# boolean isFull() Returns true if the deque is full, or false otherwise.

class MyCircularDeque:

    def __init__(self, k: int):
        """Initialize the deque with a maximum size of k."""
        self.k = k
        self.deque = [0] * k  # Fixed size array to store elements
        self.size = 0         # Track the current number of elements
        self.front = 0        # Points to the front of the deque
        self.rear = 0         # Points to the next insertion point at the rear

    def insertFront(self, value: int) -> bool:
        """Adds an item at the front of the deque. Returns true if successful."""
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.k) % self.k  # Move front pointer back in circular manner
        self.deque[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """Adds an item at the rear of the deque. Returns true if successful."""
        if self.isFull():
            return False
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.k  # Move rear pointer forward in circular manner
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        """Deletes an item from the front of the deque. Returns true if successful."""
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k  # Move front pointer forward
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        """Deletes an item from the rear of the deque. Returns true if successful."""
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.k) % self.k  # Move rear pointer back
        self.size -= 1
        return True

    def getFront(self) -> int:
        """Gets the front item from the deque. Returns -1 if empty."""
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self) -> int:
        """Gets the last item from the deque. Returns -1 if empty."""
        if self.isEmpty():
            return -1
        return self.deque[(self.rear - 1 + self.k) % self.k]

    def isEmpty(self) -> bool:
        """Checks whether the deque is empty."""
        return self.size == 0

    def isFull(self) -> bool:
        """Checks whether the deque is full."""
        return self.size == self.k
