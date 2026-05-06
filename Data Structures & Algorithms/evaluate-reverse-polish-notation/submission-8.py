class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '-':
                stack.append(-stack.pop() + stack.pop())
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == '/':
                v1, v2 = stack.pop(), stack.pop()

                stack.append(int(v2 / v1))
            else:
                stack.append(int(t))

        return stack[-1]