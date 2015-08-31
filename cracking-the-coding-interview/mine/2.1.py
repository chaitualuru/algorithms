from llnode import LLNode
import unittest

def remove_duplicates(head):
	node_set = set([])
	ll = head
	while ll != None:
		cur_data = ll.data
		if cur_data in node_set:
			head = delete_node(head, cur_data)
		else:
			node_set.add(cur_data)
		ll = ll.next
	return head

def delete_node(head, data):
	if head.data == data:
		return head.next
	else:
		copy = head
		while copy.next != None:
			if copy.next.data == data:
				copy.next = copy.next.next
				copy = copy.next

	return head


class RemoveDuplicatesTester(unittest.TestCase):
	TEST_DATA = [(LLNode(2, LLNode(3, LLNode(2, None))), LLNode(3, LLNode(2, None))),
		(LLNode(1, LLNode(1, None)), LLNode(1, None)),
		(LLNode(1, None), LLNode(1, None))]

	def run_tests(self):
		for inp, expected in self.TEST_DATA:
			res = remove_duplicates(inp)
			self.assertEqual(res, expected)

if __name__ == '__main__':
	unittest.main()
