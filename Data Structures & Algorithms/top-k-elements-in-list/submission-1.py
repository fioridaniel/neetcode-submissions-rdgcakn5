class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        res = []
        for i in range(k):
            # encontrar a chave com o valor maximo
            max_key = max(count, key=count.get)
            res.append(max_key)
            del count[max_key]

        return res