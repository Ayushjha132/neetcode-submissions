class Solution:
    def isPalindrome(self, s: str) -> bool:
        # build string and remove non alpha numeric by isalnum() function.
        d1 = ""
        for c in s:
            if c.isalnum():
                d1 += c.lower()

    
        # build the reverse 
        d2 = ""
        for i in range(len(d1)-1, -1, -1):
            d2 += d1[i]
        

        return d1 == d2
            
# time O(n) space O(n)

        