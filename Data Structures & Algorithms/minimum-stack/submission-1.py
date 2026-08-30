# maintaining two stacks

class MinStack:

    def __init__(self):
        self.s = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.minStack: # check will be in minStack because it was empty earlier
            self.minStack.append(val)
        elif self.minStack[-1] < val:
            self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.minStack.pop()
        return self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

