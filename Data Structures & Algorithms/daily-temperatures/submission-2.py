class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * (len(temperatures))

        for i in range(len(temperatures)):
            pair = (i, temperatures[i])
            
            while stack and stack[-1][1] < temperatures[i]:
                idx, temp = stack.pop()
                res[idx] = i - idx
            
            stack.append(pair)

        return res