# hare_tortoise 알고리즘 (Floyd's Cycle-Finding)
## 링크드리스트 cycle 판별 알고리즘

## leetcode 
## https://leetcode.com/problems/linked-list-cycle-ii/description/

def detectCycle(head):
    if head is None or head.next is None:
        return None
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next
        if slow == fast:
            slow = head
            while slow!=fast:
                slow = slow.next
                fast = fast.next

            return slow
    
    return None
