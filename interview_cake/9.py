import sys
import unittest

MAX_INT = sys.maxint
MIN_INT = -sys.maxint - 1

def bst_checker(root):
	nodes = [(root, MAX_INT, MIN_INT)]
	while nodes:
		(node, upper, lower) = nodes.pop()
		if node.value > upper or node.value < lower:
			return False

		if node.right:
			nodes.append((node.right, upper, node.value))

		if node.left:
			nodes.append((node.left, node.value, lower))

	return True



class BSTCheckerTester(unittest.TestCase):
	TEST_DATA = [(),
		()]

	for inp, expected in self.TEST_DATA:
		res = bst_checker(inp)
		self.assertEqual(res, expected)


if __name__ == '__main__':
	unittest.main()
