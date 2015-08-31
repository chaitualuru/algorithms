"""Binary Tree"""


class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        self.left = None
        self.right = None

    def insertLeft(self, item):
        if not self.left:
            self.left = BinaryTree(item)
        else:
            leftChild = BinaryTree(item)
            leftChild.left = self.left
            self.left = leftChild

    def insertRight(self, item):
        if not self.right:
            self.right = BinaryTree(item)
        else:
            rightChild = BinaryTree(item)
            rightChild.right = self.right
            self.right = rightChild

# Tree Traversal

# def preorder(tree):
#     if tree:
#         print(tree.getRootVal())
#         preorder(tree.getLeftChild())
#         preorder(tree.getRightChild())

# def postorder(tree):
#     if tree != None:
#         postorder(tree.getLeftChild())
#         postorder(tree.getRightChild())
#         print(tree.getRootVal())

# def inorder(tree):
#   if tree != None:
#       inorder(tree.getLeftChild())
#       print(tree.getRootVal())
#       inorder(tree.getRightChild())
