class Solution:
    def binarySearch(self, nums, l, r, target):
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        if nums[l] <= nums[r]:
            return self.binarySearch(nums, l, r, target)

        while l <= r:
            mid = (l + r) // 2

            if abs(l - r) == 1:
                break
            elif nums[mid] < nums[l]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid
        
        # left-portion
        ll, lr = 0, l
        print(f'll: {ll}, lr: {lr}')

        if nums[ll] <= target <= nums[lr]:
            return self.binarySearch(nums, ll, lr, target)

        # right-portion
        rl, rr = r, len(nums) - 1
        print(f'rl: {rl}, rr: {rr}')
        return self.binarySearch(nums, rl, rr, target)