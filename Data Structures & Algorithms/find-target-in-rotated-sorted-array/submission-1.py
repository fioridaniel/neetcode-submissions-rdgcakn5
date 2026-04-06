class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # retornar o index de target
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            m = l + (r - l) // 2
            
            # achou
            if nums[m] == target:
                return m

            # nums[m] esta na direita
            if nums[m] < nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            
            # nums[m] esta na esquerda
            else:
                if nums[m] > target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
        return -1