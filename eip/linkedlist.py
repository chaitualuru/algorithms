"""Singly Linked List"""

class LinkedList(object):
	def __init__(self, head=None):
		self.head = head

	def __str__(self):
		out = ""
		to_pr = self.head
		while to_pr != None:
			out += str(to_pr.data) + "->"
			to_pr = to_pr.next

		return out


class LLNode(object):
	def __init__(self, data, next):
		self.data = data
		self.next = next

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_next(self, node):
		self.next = node

	def __str__(self):
		return str(self.data)
