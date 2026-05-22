"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        listMap = {}
        ptrMap = {}

        temp = head
        while temp:
            listMap[temp] = Node(temp.val)
            ptrMap[listMap[temp]] = temp.random
            temp = temp.next 

        for node in listMap:
            newNode = listMap[node]
            oldRandom = ptrMap[newNode]
            
            if oldRandom:
                newNode.random = listMap[ptrMap[newNode]]
            else:
                newNode.random = None
            
            if node.next:
                newNode.next = listMap[node.next]
            else:
                newNode.next = None

        return listMap[head]