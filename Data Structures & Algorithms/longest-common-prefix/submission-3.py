class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # best approch 
        # time O(S): no. of chars space O(1)
        # if list is empty 
        # if not strs:
        #     return ""
        # start_string = strs[0]
        # prefix = ""
        # # approch here is match the char from the list strings
        # for i, char in enumerate(start_string):
        #     for s in strs:
        #         # index value of a char is more than the length of a string or string doesn't contain that char
        #         if i >= len(s) or s[i] != char:
        #             return prefix
        #     prefix += char
        # return prefix 


        # sorting method
        # If the First string and the Last string share a prefix, every string in between them must also share that prefix.
        # Why? Because the list is sorted! You don't need to check the middle ones.
        if not strs:
            return ""
        strs.sort()
        first = strs[0]
        last = strs[-1]

        i = 0
        while i < len(first) and len(last):
            if first[i] != last[i]:
                break
            i += 1
        return first[:i]

            


