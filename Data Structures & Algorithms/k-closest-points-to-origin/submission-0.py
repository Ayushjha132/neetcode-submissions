class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in points:
            euc_dis = math.sqrt(((0-i[0])**2) + ((0-i[1])**2))
            heap.append((euc_dis, i))
        
        heapq.heapify(heap)

        res = []

        while k > 0:
            val = heapq.heappop(heap)
            res.append(val[1])
            k -= 1
        
        return res