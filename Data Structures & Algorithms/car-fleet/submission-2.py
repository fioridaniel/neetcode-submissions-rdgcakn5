class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        res = len(position)

        for p, s in pair:
            curr_time = (target - p) / s

            if stack and curr_time <= stack[-1]:
                res -= 1
                
            else: stack.append(curr_time)

        return res