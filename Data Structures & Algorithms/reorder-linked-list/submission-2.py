# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        curr = head
        prev = None
        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        middle = None

        while fast and fast.next:
            fast = fast.next
            if fast.next:
                slow = slow.next
                fast = fast.next
            else:
                break

        second_half = self.reverseList(slow.next)
        slow.next = None

        l, r = head, second_half
        while r:
            l_next = l.next
            r_next = r.next
            
            l.next = r
            r.next = l_next

            l = l_next
            r = r_next          