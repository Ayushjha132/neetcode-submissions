class Solution:
    def isValid(self, s: str) -> bool:
        # closing mapping tracking 
        # hash map 
        mapping = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        # build a stack
        stk = []

        for c in s: # direclty get the element
            if c in mapping: 
                if not stk or mapping[c] != stk[-1]:
                    return False
                stk.pop()
            else: 
                stk.append(c)

                # here if the stack it empty only it will be true else fasle
        return not stk

# time : O(n)
# space: O(n)
