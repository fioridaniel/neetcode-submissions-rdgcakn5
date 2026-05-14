class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for num in numsSet:
            if (num - 1) not in numsSet:
                lenght = 1
                while (num + lenght) in numsSet:
                    lenght += 1 
                longest = max(lenght, longest)
        
        return longest
