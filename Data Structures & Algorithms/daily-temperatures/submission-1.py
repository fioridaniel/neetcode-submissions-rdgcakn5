class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [(0, temperatures[0])] # pair: idx, val

        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                idx, val = stack.pop()
                res[idx] = i - idx
                
            stack.append((i, temperatures[i]))
        
        return res