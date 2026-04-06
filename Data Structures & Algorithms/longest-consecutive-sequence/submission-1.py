class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maior_seq = 0

        for n in nums:
            if n - 1 not in numsSet: # achamos o comeco de uma sequencia
                curr = n
                seq = 0
                while curr in numsSet:
                    seq += 1
                    curr += 1
                maior_seq = max(maior_seq, seq)
        
        return maior_seq