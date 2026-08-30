class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        # taking s1 is smaller a/c to question
        l1, l2 = len(s1), len(s2)
        count1 = Counter(s1)

        # range can be reduces with the smaller length 
        for i in range(l2 - l1 + 1):
            # frequency in that window should be matched with the shorter string
            window = s2[i : i + l1] # all char inside the window
            count2 = Counter(window) # contain the frequency of chars
            if count1 == count2:
                return True
        return False
            
            
