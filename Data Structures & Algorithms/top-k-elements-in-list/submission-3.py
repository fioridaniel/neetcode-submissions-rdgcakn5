class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        n = len(nums)

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        print(count)

        freq = [[] for _ in range(n + 1)]

        for c in count:
            freq[count[c]].append(c)

        print(freq)

        check_k = 0
        res = []
        
        for i in range(n, 0, -1):
            while freq[i]:
                check_k += 1
                elem = freq[i].pop()
                res.append(elem)
                if check_k >= k:
                    return res

        return res