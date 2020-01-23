class Stack:

    def __init__(self):
        self._stack = []
        self.len = 0

    def push(self, item):
        self._stack.append(item)
        self.len += 1

    def pop(self):
        if self.len == 0:
            raise Exception("Stack is empty")
        self.len -= 1
        return self._stack.pop()

    def top(self):
        if self.len == 0:
            raise Exception("Stack is empty")
        return self._stack[-1]

    def is_empty(self):
        return self.len == 0
