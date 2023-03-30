class PriorityQueueArrayOrdered:

    # Constructor, Time O(1), Space O(1)
    def __init__(self, capacity):
        self.maxSize = capacity
        self.Array = {}
        self.length = 0

    # Add by moving the biggest at the end, Time O(n), Space O(1), n is priority queue length
    def enqueue(self, value):
        if self.length == self.maxSize:
            print("priority queue is full, cannot enqueue " + str(value))
            return
        i = self.length - 1
        while i >= 0 and value < self.Array[i]:  # biggest put at the end
            self.Array[i + 1] = self.Array[i]
            i -= 1
        self.Array[i + 1] = value
        self.length += 1

    # Remove from the end, Time O(1), Space O(1)
    def dequeue(self):
        if self.isEmpty():
            print("queue is empty")
            return None
        item = self.Array[self.length - 1]
        self.length -= 1
        return item

    # Return the end value, Time O(1), Space O(1)
    def peek(self):
        if self.isEmpty():
            print("queue is empty")
            return None
        return self.Array[self.length - 1]

    # print all, they are sorted, Time O(n), Space O(1)
    def print(self):
        line = "Priority Queue: "
        for i in range(0, self.length):
            line += str(self.Array[i]) + " "
        print(line)

    # Return the length, Time O(1), Space O(1)
    def size(self):
        return self.length

    # Check empty, Time O(1), Space O(1)
    def isEmpty(self):
        return self.length == 0


pq = PriorityQueueArrayOrdered(5)
pq.enqueue(30)
pq.enqueue(12)
pq.enqueue(20)
pq.enqueue(15)
pq.enqueue(54)
pq.enqueue(66)
pq.print()
print("size: " + str(pq.size()))
print("peek: " + str(pq.peek()))

# dequeue
pq.dequeue()
pq.print()
print("size: " + str(pq.size()))
print("peek: " + str(pq.peek()))

pq.enqueue(66)
pq.enqueue(98)
pq.print()
print("size: " + str(pq.size()))
print("peek: " + str(pq.peek()))
