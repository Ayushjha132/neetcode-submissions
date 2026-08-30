# smartly using same sapce
class MinStack:

    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        if not self.s:
            self.s.append((val, val))
        else:
            self.s.append((val, min(self.s[-1][1], val)))

    def pop(self) -> None:
        return self.s.pop()

    def top(self) -> int: # remeber top will come from tuple
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]     
