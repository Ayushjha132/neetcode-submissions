class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1])

        minHeap = []
        curPass = 0
        for t in trips:
            numPass, start, end = t

            # drop point removal of passangers
            while minHeap and minHeap[0][0] <= start:
                curPass -= minHeap[0][1] #reduce the number of passangers from the heap
                heapq.heappop(minHeap)
            
            curPass += numPass
            if curPass > capacity:
                return False
            heapq.heappush(minHeap, [end, numPass])
        return True