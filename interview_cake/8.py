import unittest
from binarytreenode import BinaryTreeNode

def is_superbalanced(root):
	depth_list = list([])
	nodes = list([])
	nodes.append((root, 0))
	while nodes:
		node, depth = nodes.pop()
		if not node.left and not node.right:
			if depth not in depth_list:
				depth_list.append(depth)
				if len(depth_list) > 2 or (len(depth_list) == 2 and abs(depth_list[0] - depth_list[1]) > 1):
					return False
		else:
			if node.right:
				nodes.append((node.right, depth + 1))
			if node.left:
				nodes.append((node.left, depth + 1))

	return True

class SuperBalanceTester(unittest.TestCase):
	TEST_DATA = []

	def test(self):
		for inp, expected in self.TEST_DATA:
			res = is_superbalanced(inp)
			self.assertEqual(res, expected)

if __name__ = '__main__':
	unittest.main()
