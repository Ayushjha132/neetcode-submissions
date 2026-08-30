# towards zero or +ve infinity i.e. int(-5/2) = 2
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i == '+':
                b = s.pop()
                a = s.pop() 
                r = a + b
                s.append(r)
            elif i == '-':
                b = s.pop()
                a = s.pop()
                r = a - b
                s.append(r)
            elif i == '*':
                a, b = s[-2], s[-1]
                del s[-2:]
                r = a * b
                s.append(r)
            elif i == '/':
                b = s.pop() 
                a = s.pop()
                r = int(a/b)
                s.append(r)
            else:
                s.append(int(i))

        return s[0]