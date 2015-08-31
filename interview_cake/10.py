import unittest
from binarytreenode import BinaryTreeNode

def get_second_largest(root):
	while root:
		if root.right:
			if not root.right.left and not root.right.right:
				return root.value
			else:
				root = root.right
				continue
		else:
			return get_largest(root.left)

def get_largest(root):
	while root.right:
		root = root.right
	return root.value

class SecondLargestElementTester(unittest.TestCase):
	TEST_DATA = [(BinaryTreeNode(5, BinaryTreeNode(3, None, None), BinaryTreeNode(10, BinaryTreeNode(7, None, None), BinaryTreeNode(15, None, None))), 10),
		(BinaryTreeNode(5, BinaryTreeNode(3, None, None), BinaryTreeNode(10, BinaryTreeNode(7, BinaryTreeNode(4, None, None), BinaryTreeNode(8, None, None)), None)), 8)]

	def test(self):
		for inp, expected in self.TEST_DATA:
			res = get_second_largest(inp)
			self.assertEqual(res, expected)

if __name__ == '__main__':
	unittest.main()
