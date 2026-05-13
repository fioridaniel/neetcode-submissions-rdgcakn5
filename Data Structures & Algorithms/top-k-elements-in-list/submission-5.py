class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        buckets = [[] for i in range(0, len(nums) + 1)]    

        for n in count:
            freq = count[n]
            buckets[freq].append(n)
        
        res = []
        i = len(buckets) - 1
        while k > 0:
            for b in buckets[i]:
                res.append(b)
                k -= 1
            i -= 1

        return res