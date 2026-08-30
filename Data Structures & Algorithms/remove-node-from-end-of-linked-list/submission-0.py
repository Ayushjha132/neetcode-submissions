# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # rap the with one dummy value
        dummy = ListNode(0, head)
        # two pointer of list slow and fast 
        slow = fast = dummy
        # create gap of n+1 between the slow and fast
        for _ in range(n+1):
            fast = fast.next

        # move while fast reach the end None
        while fast:
            slow = slow.next
            fast = fast.next

        # remove the element from last by n place 
        slow.next = slow.next.next

        return dummy.next