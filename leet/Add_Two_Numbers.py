## Add Two Numbers
## https://leetcode.com/problems/add-two-numbers/submissions/
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h = l1 ## head node 고정
        
        ## l1에 l2를 더하기
        ## l2가 더 길면 l1뒤에 이어붙이기
        while l2 and l1:
            l1.val += l2.val
            l2 = l2.next
            if not l1.next: break
            l1 = l1.next
        if l2:
            l1.next = l2
        
        ## 각 노드 값이 10 이상이면,
        ## 현재 노드의 next에 1 더하기 (next가 없으면 추가)
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
