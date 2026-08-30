class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # brut force time O(n^2) space O(1)
        # if list is empty 
        if not strs:
            return ""
        start_string = strs[0]
        prefix = ""
        # approch here is match the char from the list strings
        for i, char in enumerate(start_string):
            for s in strs:
                # index value of a char is more than the length of a string or string doesn't contain that char
                if i >= len(s) or s[i] != char:
                    return prefix
            prefix += char
        return prefix 
