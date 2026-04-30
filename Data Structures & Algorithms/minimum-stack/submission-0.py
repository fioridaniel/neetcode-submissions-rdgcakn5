class Node:
    def __init__(self, val: int, next: Node):
        self.val = val
        self.next = next

class MinStack:

    def __init__(self):
        self.head = None
        self.minVals = []

    def push(self, val: int) -> None:
        self.head = Node(val, self.head)
        
        if self.minVals:
            val = min(self.minVals[-1], val)
            self.minVals.append(val)
        else:
            self.minVals.append(val)

    def pop(self) -> None:
        val = self.head.val
        self.head = self.head.next
        self.minVals.pop()

    def top(self) -> int:
        return self.head.val
        
    def getMin(self) -> int:
        return self.minVals[-1]
