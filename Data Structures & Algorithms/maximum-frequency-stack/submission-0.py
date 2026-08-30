class FreqStack:
# here pop part will be from group -> rest is supporter
    def __init__(self):
        self.counter = {} # count the frequency 
        self.group = {} # group based on the counter
        self.maxCnt = 0 # current max count 

    def push(self, val: int) -> None:
        valCnt = 1 + self.counter.get(val, 0)
        self.counter[val] = valCnt # store in counter
        if valCnt > self.maxCnt:
            self.maxCnt = valCnt
            self.group[valCnt] = []
        self.group[valCnt].append(val) # store the val in its counter

    def pop(self) -> int:
        res = self.group[self.maxCnt].pop() # pop from group
        self.counter[res] -= 1
        if not self.group[self.maxCnt]:
            self.maxCnt -= 1
        return res

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()