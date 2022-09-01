## Add Two Numbers
## https://leetcode.com/problems/add-two-numbers/submissions/

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = ListNode()
        h = c
        while l1:
            c.val = l1.val
            l1 = l1.next
            if not l1: break
            c.next = ListNode()
            c = c.next
        c = h
        while l2 and c:
            c.val += l2.val
            l2 = l2.next
            if not c.next: break
            c = c.next
        if l2:
            c.next = l2
        
        c = h
        while c:
            if c.val>=10:
                c.val -= 10
                if c.next:
                    c.next.val += 1
                else:
                    c.next = ListNode(1)
            c = c.next
        return h
