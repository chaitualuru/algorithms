"""Linked List"""


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def add(self, node):
        node.next = self.head
        self.head = node
        self.size += 1

    def search(self, node):
        current = self.head
        while current:
            if node.data == current.data:
                return node
            current = current.next

    def remove(self, item):
        current = self.head
        while current:
            if item == current.data:
                current.data = current.next.data
                current.next = current.next.next

    def size(self):
        return self.size


class SLLNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
