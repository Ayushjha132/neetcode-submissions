
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

# brute force time  O(n^2) 
        # from collections import Counter
        # if not strs:
        #     return [[""]]
        # return_list = []
        # visted_list = [False] * len(strs)
        # for i, val in enumerate(strs):
        #     if visted_list[i]:
        #         continue
        #     tem_list = [val]
        #     visted_list[i] = True
        #     for j in range(i+1, len(strs)):
        #         if not visted_list[j]:
        #             if Counter(val) == Counter(strs[j]):
        #                 tem_list.append(strs[j])
        #                 visted_list[j] = True
        #     return_list.append(tem_list)
        # return return_list

# using hash map time O(nlogn) space O(n)
# using defaultdict() from collections
# using sort()
        from collections import defaultdict 
        container = defaultdict(list)
        for val in strs:
            container_key = tuple(sorted(val))
            container[container_key].append(val)
        return list(container.values())






