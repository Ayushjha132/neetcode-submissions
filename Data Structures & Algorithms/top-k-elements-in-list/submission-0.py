class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n) for time and space
        counter_dict = {}
        for i in nums:
            if i in counter_dict:
                counter_dict[i] += 1
            else:
                counter_dict[i] = 1
        
        # using sorted() inplace method
        sorted_candidates = sorted(counter_dict.keys(), key=lambda x: counter_dict[x], reverse=True)
        return sorted_candidates[:k]