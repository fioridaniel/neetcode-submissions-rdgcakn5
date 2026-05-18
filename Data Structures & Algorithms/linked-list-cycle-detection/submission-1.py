# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        if not slow:
            return False

        fast = slow.next

        while fast:
            if slow == fast:
                return True
            
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        
        return False
        