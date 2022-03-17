"""
QUEUE:
    - first in, first out (FIFO)
    - maintains chronological order based least recent

IMPLEMENTATIONS:
    - list
        - insert each new element at index 0
        - not recommended because of list capacity limitation
    - collections.deque
    - queue.LifoQueue
"""

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, val):
        self.queue.appendleft(val)

    def dequeue(self):
        return self.queue.pop()

    def front(self):
        return self.queue[-1]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
   
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())