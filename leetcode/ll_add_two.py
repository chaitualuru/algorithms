# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
	# 3 0 4
	# 2 4
    def addTwoNumbers(self, l1, l2):
		result = ListNode(None)
		while l1:
			if l2:
			result = ListNode(l1.val + l2.val)