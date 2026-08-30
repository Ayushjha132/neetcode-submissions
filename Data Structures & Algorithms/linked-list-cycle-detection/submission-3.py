# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # optimal : Floyd’s tortoise and hair algo
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False



        # not works in all condition - not optimal 
        # time : O(n) and space : (n)
        # visited = set() # note python set can check value in O(1) time
        # curr = head
        # while curr:
        #     if curr.val in visited:
        #         return True
        #     visited.add(curr.val)
        #     curr = curr.next
        
        # return False