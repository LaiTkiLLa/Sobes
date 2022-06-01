
class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        if self.stack == []:
            return None
        else:
            self.stack.pop()
            return self.stack

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

