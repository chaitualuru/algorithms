"""Queue"""
from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.popleft()

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return not self.queue
