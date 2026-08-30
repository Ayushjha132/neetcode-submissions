class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # time O(NlogN) space O(N)

        # if len(s) != len(t):
        #     return False
        # return sorted(s) == sorted(t)

        # this will compare and return True or False
        
        # time O(N) and space O(1)
        # hash map still space is O(1) because of limit of a-z

        # if len(s) != len(t):
        #     return False

        # letter = {}

        # for char in s:
        #     letter[char] = letter.get(char, 0) + 1

        # for char in t:
        #     # not foound in dict
        #     if char not in letter:
        #         return False
        #     #  reduce the count of char
        #     letter[char] -= 1
        #     # when uneven no. of chars
        #     if letter[char] < 0:
        #         return False
        #     # else it is a anagram
        # return True


        # Counter() class 
        # time O(N) and space O(1) as limited no of char
        from collections import Counter
        return Counter(s) == Counter(t)
        