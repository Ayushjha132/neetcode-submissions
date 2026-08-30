class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 1. Extract values from l1
        cur1 = l1
        ns1 = []
        while cur1:
            ns1.append(str(cur1.val)) # store as strings for joining
            cur1 = cur1.next

        # 2. Extract values from l2
        cur2 = l2
        ns2 = []
        while cur2:
            ns2.append(str(cur2.val)) # store as strings for joining
            cur2 = cur2.next

        # Since the problem stores digits in reverse order, reverse them to get the correct number
        ns1.reverse()
        ns2.reverse()

        # Convert list of strings to actual integers
        n1 = int(''.join(ns1)) if ns1 else 0
        n2 = int(''.join(ns2)) if ns2 else 0

        # Add the two numbers together
        total_sum = n1 + n2 

        # Convert the total sum back to a string of digits
        sum_str = str(total_sum)

        # Build the linked list in reverse order (since LeetCode expects reverse order)
        dummy = ListNode(0)
        curr = dummy
        
        # Loop through the sum string in reverse order
        for char in sum_str[::-1]:
            curr.next = ListNode(int(char))
            curr = curr.next

        return dummy.next