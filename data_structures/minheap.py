"""Min Binary Heap"""


class MinHeap:
    def __init__(self, root=None):
        self.root = root
        self.left = None
        self.right = None

    def getMin(self):
        return self.root

    def isEmpty(self):
        return not self.root
