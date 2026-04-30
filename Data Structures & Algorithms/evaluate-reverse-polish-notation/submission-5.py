class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        
        for t in tokens:
            if t == "+":
                s.append(s.pop() + s.pop())
            elif t == "-":
                s.append(-s.pop() + s.pop())
            elif t == "*":
                s.append(s.pop() * s.pop())
            elif t == "/":
                v1, v2 = s.pop(), s.pop()
                s.append(int(v2 / v1))
            else:
                s.append(int(t))

        return s.pop()