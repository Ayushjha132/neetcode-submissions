class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for i in asteroids:
            # when asteroid will be distroyed 
            # 1. someting in stack 2. top of the stack is +ve and i is -ve
            while s and i < 0 < s[-1]:
                diff = i + s[-1]
                if diff < 0:
                    s.pop()
                elif diff > 0:
                    break
                else:
                    s.pop()
                    break
            else:
                s.append(i)
        return s

