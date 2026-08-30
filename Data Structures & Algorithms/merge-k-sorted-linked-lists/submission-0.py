# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # brute force - time exceeds error 
        # nodes = []
        # for lst in lists:
        #     while lst:
        #         nodes.append(lst.val)
        # nodes.sort()
        # res = ListNode(0)
        # cur = res
        # for n in nodes:
        #     cur.next = ListNode(n)
        #     cur = cur.next
        # return res.next

        # optimal approach
        # heap 
        if len(lists) == 0: return None

        res = ListNode(0)
        cur = res
        minHeap = []

        # among k lists first nodes maintian heap and then 
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(minHeap, (lst.val, i, lst))
            
        counter = len(lists)
        while minHeap:
            val, i, node = heapq.heappop(minHeap)
            cur.next = node
            cur = cur.next

            if node.next:
                heapq.heappush(minHeap, (node.next.val, counter, node.next))
                counter += 1

        return res.next
    




