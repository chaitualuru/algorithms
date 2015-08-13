"""Merge sorted Linked Lists"""

from linkedlist import LLNode
from linkedlist import LinkedList

def merge_lists(A, B):
	result = None
	result_tail = None
	ptr_a = A.head
	ptr_b = B.head
	while ptr_a and ptr_b:
		if ptr_a.data <= ptr_b.data:
			result, result_tail = insert_in_result(ptr_a.data, result, result_tail)
			ptr_a = ptr_a.next
		else:
			result, result_tail = insert_in_result(ptr_b.data, result, result_tail)
			ptr_b = ptr_b.next

	if not ptr_a and ptr_b:
		result_tail.next = ptr_b
		return LinkedList(result)
	if not ptr_b and ptr_a:
		result_tail.next = ptr_a
		return LinkedList(result)

	return LinkedList(result)

def insert_in_result(data, head, tail):
	if not head:
		head = LLNode(data, tail)
	else:
		if not tail:
			tail = LLNode(data, None)
		else:
			tail.next = LLNode(data, None)
			tail = tail.next

	return head, tail


def main():
	print merge_lists(LinkedList(LLNode(2, LLNode(5, LLNode(7, None)))), LinkedList(LLNode(3, LLNode(11, None))))



if __name__ == '__main__':
	main()