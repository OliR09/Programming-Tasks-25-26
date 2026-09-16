"""
TASK: 03 Queue Simulation

# Queue Simulation using OOP
Make a Queue class with:
- enqueue, dequeue, peek, size  
Simulate customers joining/leaving.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():

    class CircularQueue:
        def __init__(self,maxItems):
            self.items = [None]*maxItems
            self.front = 0
            self.rear = -1
            self.queueSize = 0
            self.maxSize = maxItems

        def enQueue(self,item):
            if self.queueSize == self.maxSize:
                print("Queue is at full size =", self.queueSize)
            else:
                self.rear = (self.rear + 1)%(self.maxSize)
                self.queueSize += 1
                self.items[self.rear] = items
    
        def deQueue(self):
            if (self.queueSize == 0):
                return "Queue Empty"
            else:
                first = self.items[self.front]
                self.queueSize -= 1
                self.front = (self.front + 1)%(self.maxSize)
                return first

        def peek(self):
            if self.queueSize == 0:
                return "Queue empty"
            else:
                return self.items[self.front]
    
        def size(self):
            return self.queueSize

queue = CircularQueue(5)

queue.enQueue("Customer 1")
queue.enQueue("Customer 2")
queue.enQueue("Customer 3")

print("Next customer:", queue.peek())
print("Queue size:", queue.size())

print("Leaving:", queue.deQueue())
print("Leaving:", queue.deQueue())

print("Next customer:", queue.peek())
print("Queue size:", queue.size())

    pass


if __name__ == "__main__":
    main()
