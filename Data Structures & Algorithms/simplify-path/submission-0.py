class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split('/') # list of array split at /
        stack = []

        for i in components:
            if i == "" or i == ".":
                continue
            elif i == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        
        return "/" + "/".join(stack)