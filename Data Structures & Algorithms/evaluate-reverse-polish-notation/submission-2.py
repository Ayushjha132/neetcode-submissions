class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # using math lib operator 
        import operator
        s = []

        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b)
        }

        for i in tokens:
            if i in ops:
                a, b = s[-2:]
                del s[-2:]
                s.append(ops[i](a,b))
            else:
                s.append(int(i))
        return s[0]
        