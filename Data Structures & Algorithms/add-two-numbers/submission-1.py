# Definition for singly-linked list.
# class ListListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListListNode], l2: Optional[ListListNode]) -> Optional[ListListNode]:
        res = ListNode()
        dummy = res 
        carry = 0
        
        while l1 or l2 or carry > 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            curSum = val1 + val2 + carry
            carry = curSum // 10
            rem = curSum % 10
            
            if rem == 0 and carry == 0:
                res.next = ListNode(curSum)
            else:
                res.next = ListNode(rem)
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
            res = res.next
                
        return dummy.next