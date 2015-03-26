# O(n) dequeue, if element exists in deque stack, return it
# else, while enqueue stack not empty, pop and move to deque stack
# pop and return from deque stack
# O(1) enqueue, just add to enqueue stack

# O(n) enqueue, move to outStack and add the item then move back to
# inStack
# O(1) dequeue, remove from inStack

class Stack:
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		if not self.items: return None

		return self.items.pop()

class Queue:
	def __init__(self):
		self.enqueue_stack = Stack()
		self.deque_stack = Stack()

	def enqueue(self, item):
		self.enqueue_stack.items.append(item)

	def dequeue(self):
		if self.deque_stack.items:
			return self.deque_stack.pop()
		else:
			while self.enqueue_stack.items:
				self.deque_stack.items.append(self.enqueue_stack.items.pop())

		return self.dequeue_stack.pop()

class Queue2:
	def __init__(self):
		self.inStack = Stack()
		self.outStack = Stack()

	def dequeue(self):
		if self.inStack.items:
			return self.inStack.pop()
		else:
			raise Empty

	def enqueue(self, item):
		while self.inStack.items:
			self.outStack.items.append(self.inStack.items.pop())
		self.inStack.items.append(item)
		while self.outStack.items:
			self.inStack.items.append(self.outStack.items.pop())