class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])

        res = [intervals[0]]  # começa com o primeiro intervalo

        for i in range(1, len(intervals)):
            last = res[-1]        # pega o último intervalo já no resultado
            curr = intervals[i]

            if curr[0] <= last[1]:          # há sobreposição
                last[1] = max(last[1], curr[1])   # extende in-place
            else:
                res.append(curr)            # sem sobreposição, adiciona normalmente

        return res