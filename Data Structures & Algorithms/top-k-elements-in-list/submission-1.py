from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n) for time and space (raw based - best approach)
        # counter_dict = {}
        # for i in nums:
        #     if i in counter_dict:
        #         counter_dict[i] += 1
        #     else:
        #         counter_dict[i] = 1
        
        # # using sorted() inplace method
        # sorted_candidates = sorted(counter_dict.keys(), key=lambda x: counter_dict[x], reverse=True)
        # return sorted_candidates[:k]

        counted_item = Counter(nums)
        count_pair = counted_item.most_common(k)

        result = []
        for i, v in count_pair:
            result.append(i)
        return result
