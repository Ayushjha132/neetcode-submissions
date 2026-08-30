class Solution:
    def validPalindrome(self, s: str) -> bool:
        # build the string
        d1 = ""
        for c in s:
            if c.isalnum():
                d1 += c.lower()

        i = 0
        j = len(d1) - 1
        
        while i < j:
            if d1[i] == d1[j]:
                i += 1
                j -= 1
            else:
                # mismatch 
                # if remove the first left and check till j
                skip_left = s[i+1 : j+1]
                # if remove the first right and check from i
                skip_right = s[i : j]

                # this is the reverse step
                return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]

        return True

