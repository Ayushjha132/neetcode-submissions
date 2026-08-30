class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force 
        # res = []
        # for i in range(len(temperatures)):
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             res.append(j-i)
        #             break
        #     else:
        #         res.append(0)
        # return res

        # optimal using stack 
        res = [0] * len(temperatures)
        stack = [] # [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res



                