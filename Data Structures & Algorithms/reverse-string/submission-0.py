class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        j = l - 1
        for i in range(l):
            if i >= j:
                break
            s[i], s[j] = s[j], s[i]
            j -= 1
        