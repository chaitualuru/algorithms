class Stack:
    # intialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items: return None

        return self.items.pop()

    # see what the last item is
    def peek(self):
        # if the stack is empty, return None
        if not self.items: return None

        return self.items[len(self.items)-1]


class MaxStack:
    def __init__(self):
        self.stack = Stack()
        self.max_stack = Stack()

    def get_max(self):
        if not self.max_stack.items: return None

        return self.max_stack.peek()

    def push(self,item):
        self.stack.items.append(item)
        if item >= self.get_max():
            self.max_stack.items.append(item)

    def pop(self):
        if self.stack.peek() == self.get_max():
            self.max_stack.pop()
        return self.stack.items.pop()

    def peek(self):
        if not self.stack.items: return None

        return self.stack.items[-1]