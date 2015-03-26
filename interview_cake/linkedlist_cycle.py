class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self, head = None):
		self.head = head
		self.size = 0

	def insert(self, node):
		if not self.head:
			self.head = node
		else:
			node.next = self.head
			self.head = node
		self.size += 1

	def size(self):
		return self.size

	def search(self, node):
		if self.head.data == node.data:
			return self.head
		else:
			if self.head.next:
				search(self.head.next, node)
			else:
				raise ValueError("Node not in the LL")


	def delete(self, node):
		if self.size == 0:
			raise ValueError("LL is empty")
		else:
			prev = None
			cur = self.head
			found = False
			while not found:
				if cur.data == node.data:
					found = True
				elif cur == None:
					raise ValueError("Value not in LL")
				else:
					prev = cur
					cur = cur.next
			print "Reached here"
			if prev == None:
				self.head = cur.next
			else:
				prev.next = cur.next

def detect_cycle(l_l):
	slow = l_l.head
	fast = l_l.head
	while fast != None and fast.next != None:
		slow = slow.next
		fast = fast.next.next
		if slow.data == fast.data:
			return True
	return False

aList = LinkedList()
aList.insert(Node(3))
aList.insert(Node(4))
aList.insert(Node(5))
aList.insert(Node(6))
aList.insert(Node(9))
# aList.head.next.next.next.next.next = aList.head.next

print detect_cycle(aList)

# The key insight in the algorithm is that, for any integers 
# i ≥ μ and k ≥ 0, xi = xi + kλ, where λ is the length of 
# the loop to be found and μ is the index of the first element 
# of the cycle. In particular, whenever i = kλ ≥ μ, it follows 
# that xi = x2i. Thus, the algorithm only needs to check for 
# repeated values of this special form, one twice as far from 
# the start of the sequence as the other, to find a period ν 
# of a repetition that is a multiple of λ. Once ν is found, 
# the algorithm retraces the sequence from its start to find 
# the first repeated value xμ in the sequence, using the fact 
# that λ divides ν and therefore that xμ = xμ + v. Finally, 
# once the value of μ is known it is trivial to find the 
# length λ of the shortest repeating cycle, by searching for 
# the first position μ + λ for which xμ + λ = xμ.
# Find the length of the shortest cycle starting from x_μ
# The hare moves one step at a time while tortoise is still.
# lam is incremented until λ is found.
