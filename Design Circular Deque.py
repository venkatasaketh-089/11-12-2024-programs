class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k 
        self.deque = [0] * k  
        self.front = -1  
        self.size = 0  

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0
            self.rear = 0
        else:
            self.front = (self.front - 1) % self.k
        self.deque[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.k
        self.deque[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear: 
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:  
            self.front = -1
            self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.k) % self.k
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k

# Example usage:
# myCircularDeque = MyCircularDeque(3)
# print(myCircularDeque.insertLast(1))  # return True
# print(myCircularDeque.insertLast(2))  # return True
# print(myCircularDeque.insertFront(3))  # return True
# print(myCircularDeque.insertFront(4))  # return False, the queue is full.
# print(myCircularDeque.getRear())      # return 2
# print(myCircularDeque.isFull())       # return True
# print(myCircularDeque.deleteLast())   # return True
# print(myCircularDeque.insertFront(4))  # return True
# print(myCircularDeque.getFront())     # return 4