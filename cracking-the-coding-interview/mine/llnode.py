"""LinkedList Node"""

class LLNode(object):
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

	def __str__(self):
		return str(self.data)

	def __hash__(self):
		return hash(self.data)

	def __eq__(self, other):
		while self.next != None and other.next != None:
			if self.data != other.data:
				return False
			self = self.next
			other = other.next
		if self.data == other.data:
			return True
		return False

	def appendToTail(self, data):
		end = LLNode(data)
		cur = self
		while cur.next != None:
			cur = cur.next
		cur.next = end

