class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:              # < em vez de <=, para não passar do ponto
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:
                # mínimo está à direita do mid
                l = mid + 1
            else:
                # mínimo está no mid ou à esquerda
                r = mid

        return nums[l]            # l == r, ambos apontam pro mínimo