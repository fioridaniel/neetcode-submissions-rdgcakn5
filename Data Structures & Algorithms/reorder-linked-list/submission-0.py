# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [0, n-1, 1, n-2, 2, n-3, ...]

        if not head.next:
            return

        f, s = head.next, head
        while f.next:
            f = f.next
            s = s.next
            
            if f.next:
                f = f.next

        # invert the ptrs on the fast 'section'
        prev, curr = None, s.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # merge two halfs
        b, e = head, prev
        s.next = None
        while e:
            aux1, aux2 = b.next, e.next
            b.next = e
            e.next = aux1
            b, e = aux1, aux2
            