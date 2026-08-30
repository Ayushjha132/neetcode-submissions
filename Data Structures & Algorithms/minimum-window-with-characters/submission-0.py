class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        # for frequency comparision 
        count1 = Counter(t)
        need = len(count1)

        # for window check
        window = {}
        have = 0 # match the need and currently have frequency of char

        #need to store the minimum length + left + right values
        res = [float('inf'), 0, 0]  # comapre will be done on the length
        left = 0 # start with left part
        
        for right in range(len(s)):
            # add the char in window
            char = s[right]
            window[char] = window.get(char, 0) + 1

            # increase have if that char is also in count1 and count matches what is needed in count1
            if char in count1 and window[char] == count1[char]:
                have += 1
            
            # srink the size of the window if have equals need
            while need == have:
                # add the current best result
                if (right - left + 1) < res[0]:
                    res = [right - left + 1, left , right]
                
                # reduce the side from left
                left_char = s[left]
                window[left_char] -= 1

                # If removing left_char broke a requirement, decrease 'have'
                if left_char in count1 and window[left_char] < count1[left_char]:
                    have -= 1
                
                left += 1 # moving left pointer forward

            
        length, l, r = res
        return s[l:r+1] if res[0] != float('inf') else ""





